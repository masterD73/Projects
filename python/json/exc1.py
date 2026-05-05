# ------------------------
# title: JSON Parser
# ------------------------
# ------------------------
# Description:
# Lexer & Parser for JSON.
# ------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Daniel Braunstain.
# AI2 InfinityLabs.
# ----------------------------
import re
import json
from dataclasses import dataclass


@dataclass
class Tokens:
    kind: str = ""
    value: any = 0


def lex(characters, token_tuple):
    pos = 0
    while pos < len(characters):
        for category, pattern, action in token_tuple:
            pattern_c = re.compile(pattern)
            match = pattern_c.match(characters, pos)
            if match:
                text = match.group(0)
                pos = match.end(0)
                if category != "white space":
                    yield Tokens(category, action(text))
                break
        else:
            raise ValueError(f"Unexpected character '{characters[pos]}' at position {pos}")


def number_t(text: str):
    if "." in text:
        return float(text)
    return int(text)


def string_t(text: str) -> str:
    return text[1:-1]


def empty_t(text: str) -> None:
    return None


def bool_t(text: str) -> bool:
    return text == "true"


class JSONParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        """Advance to the next token."""
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        """Parsing The token generator."""
        match self.current_token.kind:
            case "open curly bracket":
                return self.parse_object()
            case "open square bracket":
                return self.parse_array()
            case "string":
                return self.parse_value()
            case _:
                raise ValueError(f"Unexpected token: {self.current_token}")

    def parse_object(self):
        """Parse a JSON object."""
        obj = {}
        self.next_token()
        while self.current_token and self.current_token.kind != "closed curly bracket":
            key = self.expect("string").value
            self.expect("colon")
            value = self.parse_value()
            obj[key] = value

            if self.current_token and self.current_token.kind == "comma":
                self.next_token()

        self.expect("closed curly bracket")
        return obj

    def parse_array(self):
        """Parse a JSON array"""
        arr = []
        self.next_token()
        need_value = False

        while self.current_token and self.current_token.kind != "closed square brackets":
            arr.append(self.parse_value())
            need_value = False

            if self.current_token and self.current_token.kind == "comma":
                self.next_token()
                need_value = True
        if need_value:
            raise ValueError(f"Expected value, but got {self.current_token}")
        self.expect("closed square brackets")
        return arr

    def parse_value(self):
        """Parse a JSON value."""
        match self.current_token.kind:
            case "string" | "number" | "bool":
                return self.consume_value()
            case "open curly bracket":
                return self.parse_object()
            case "open square bracket":
                return self.parse_array()
            case _:
                raise ValueError(f"Unexpected token: {self.current_token}")

    def consume_value(self):
        """Consume the current token and return its value."""
        value = self.current_token.value
        self.next_token()
        return value

    def expect(self, kind):
        """Ensure the current token matches the expected kind."""
        if self.current_token and self.current_token.kind == kind:
            token = self.current_token
            self.next_token()
            return token
        else:
            raise ValueError(f"Expected {kind}, but got {self.current_token}")


tokens = {
    ("white space", r"[ \n\r\t]+", empty_t),
    ("string", r"\"([^\\\"]|\\.)*\"", string_t),
    ("colon", ":", string_t),
    ("open curly bracket", r"\{", empty_t),
    ("closed curly bracket", r"\}", empty_t),
    ("number", r"-?0(?!0)(\.[0-9]*)?([eE][+-]?\d+)?|"
               r"-?[1-9][0-9]*\.?[0-9]*([eE][+-]?\d+)?", number_t),
    ("open square bracket", r"\[", empty_t),
    ("closed square brackets", r"\]", empty_t),
    ("comma", r",", empty_t),
    ("bool", r"true|false", bool_t)
}


def main():
    # Test 1:
    with open("example.txt", "r") as file:
        json_file = file.read()
    parsed_json1 = json.loads(json_file)
    token_stream1 = lex(json_file, tokens)
    parsed_input1 = JSONParser(token_stream1).parse()
    assert parsed_input1 == parsed_json1

    # Test 2:
    string = '"hello"'
    parsed_json2 = json.loads(string)
    token_s2 = lex(string, tokens)
    parsed_input2 = JSONParser(token_s2).parse()
    assert parsed_input2 == parsed_json2

    print("Done.")


if __name__ == '__main__':
    main()
