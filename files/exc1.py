# Reviewer: Alex.
def gen_az_file():
    """Generates files named A-Z holding their respective letter."""
    alphabet_list = [chr(letter) + ".txt" for letter in range(65, 90)]

    for letter in alphabet_list:
        with open(letter, 'a') as file:
            file.write(letter)


def main():
    gen_az_file()


if __name__ == '__main__':
    main()
