# Reviewer: Netta
import os
import sys
import stat


def main():
    # path = find_files("temp.txt", "//wsl.localhost/Ubuntu/home")
    file_name = sys.argv[1]
    p = find_files(file_name, "/home")
    exe_file(p)


def find_files(filename, search_path):
    for root, folder, files in os.walk(search_path):
        if filename in files:
            result = os.path.join(root, filename)
            return result


def exe_file(path):
    if os.stat(path).st_mode & stat.S_IXUSR and os.stat(path).st_mode & stat.S_IXGRP:
        print("Permission is already executable.")
        print(oct(os.stat(path).st_mode)[-3:])
    else:
        print("Permission changed to executable.")
        os.chmod(path, os.stat(path).st_mode | stat.S_IXUSR | stat.S_IXGRP)
        print(oct(os.stat(path)[0])[-3:])


if __name__ == '__main__':
    main()
