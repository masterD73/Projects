# reviewer: anan.
def char_count(string, char):
    return string.count(char)


tests = {"Hello": "l",
         "Barbara": "a",
         "lullaby": "l"}

assert char_count("Hello", "l") == 2
for key in tests.keys():
    print(f'Word: {key}. letter: {tests[key]}. count: {char_count(key, tests[key])}')
