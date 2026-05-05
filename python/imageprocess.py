# Reviewer: Alex.
def read_n_lines(file_name, n=1):
    """Read and print n number of lines."""
    with open(file_name, 'r') as file:
        for i in range(n):
            line = file.readline()
            if len(line) == 0:
                break
            print(line)


def main():
    file = "text.txt"
    n = 0
    read_n_lines(file, n)


if __name__ == '__main__':
    main()
