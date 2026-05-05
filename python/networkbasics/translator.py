# -------------------------
# title: Translator
# -------------------------
# ----------------------------------------
# Description:
# Translating from any supported language.
# to any supported language.
# ----------------------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Sea Greenberg.
# AI2 InfinityLabs.
# ----------------------------
import requests


def main():
    translated_output = []
    translate_input(translated_output)
    PrintColors.print_yellow("Thanks for using Google Translate.\n"
                             " The translated queries are:")
    print_list(translated_output, 2)
    PrintColors.print_red("Done.")


def translate_input(translated: list) -> None:
    """
    User interface for connecting to translate service.
    Receive user input of languages to translate to and from.
    Receive translatable text.
    :return: None
    """
    PrintColors.print_yellow("Welcome to Google Translate service.\n"
                             "Type the language you want to translate from and to.\n"
                             "To view all supported languages again, type Languages.\n"
                             "To quit the translator, type Kill as input.\n\n"
                             "Please select languages from the following list to translate from and to:")
    languages_dict = supported_languages()
    languages = list(languages_dict)
    print_list(languages)

    while True:
        fr = input("Translate from:").capitalize()
        if fr == "Kill":
            PrintColors.print_red("Translator has been terminated successfully.")
            return
        elif fr == "Languages":
            PrintColors.print_yellow("Available languages are:")
            print_list(languages)
        elif fr not in languages:
            PrintColors.print_yellow("Chosen language seems to not be supported.\n"
                                     "Please review supported languages by typing languages"
                                     " and try again.")
        else:
            break

    while True:
        to = input("Translate to:").capitalize()
        if to == "Kill":
            PrintColors.print_red("Translator has been terminated successfully.")
            return
        elif to == "Languages":
            PrintColors.print_yellow("Available languages are:")
            print_list(languages)
        elif to not in languages:
            PrintColors.print_yellow("Chosen language seems to not be supported.\n"
                                     "Please review supported languages by typing Languages"
                                     " and try again.")
        else:
            break

    while True:
        text = input("Enter text to translate:")
        if text.capitalize() == "Kill":
            PrintColors.print_red("Translator terminated successfully.")
            return
        translated.append(text_translate(text, languages_dict[fr], languages_dict[to]))
        PrintColors.print_green(translated[-1])


def text_translate(text: str, fr="auto", to="en") -> str:
    """
    Establish a connection with Google Translate API.
    Translate requested text to requested languages.
    :param text: Text to be translated.
    :param fr: Language name to translate from.
    :param to: Language name to translate to.
    :return: Translated string.
    """
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

    payload = {"from": fr,
               "to": to,
               "text": text}

    headers = {"x-rapidapi-key": "99f6c46785msha9c694fc1e55690p165ac2jsn0ce651f62cd1",
               "x-rapidapi-host": "google-translate113.p.rapidapi.com",
               "Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    check_success(response)
    return response.json()["trans"]


def supported_languages() -> dict:
    """
    Establishes a connection with Google Translate API.
    :return: A dictionary of supported languages.
    """
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/support-languages"

    headers = {"x-rapidapi-key": "99f6c46785msha9c694fc1e55690p165ac2jsn0ce651f62cd1",
               "x-rapidapi-host": "google-translate113.p.rapidapi.com"}

    response = requests.get(url, headers=headers)
    check_success(response)
    languages = {}
    for elem in response.json():
        languages[elem["language"]] = elem["code"]
    return languages


def check_success(response: requests) -> None:
    success, failure = 200, 300
    if failure <= response.status_code < success:
        raise ConnectionError("Connection couldn't be established.")


def print_list(ls: list, per_line=20) -> None:
    for i in range(0, len(ls), per_line):
        PrintColors.print_cyan(str(ls[i:i + per_line])[1:-1].replace("'", ""))


class PrintColors:
    """
    Print methods to print in color.
    """

    def print_red(self: any): print("\033[91m {}\033[00m".format(self))

    def print_green(self: any): print("\033[92m {}\033[00m".format(self))

    def print_yellow(self: any): print("\033[93m {}\033[00m".format(self))

    def print_light_purple(self: any): print("\033[94m {}\033[00m".format(self))

    def print_purple(self: any): print("\033[95m {}\033[00m".format(self))

    def print_cyan(self: any): print("\033[96m {}\033[00m".format(self))

    def print_light_gray(self: any): print("\033[97m {}\033[00m".format(self))

    def print_black(self: any): print("\033[98m {}\033[00m".format(self))


if __name__ == '__main__':
    main()
