import sys
from typing import TextIO

def number_lines(file: TextIO, number_all_lines=False) -> None:
    line_number = 1
    for line in file:
        if line.strip() or number_all_lines:
            print(f'{line_number}\t{line}', end='')
            line_number += 1

def main():
    number_all_lines = False
    file_index = 1

    if len(sys.argv) > 1 and sys.argv[1] == '-b':
        if len(sys.argv) > 2 and sys.argv[2] == 'a':
            number_all_lines = True
            file_index = 3

    if len(sys.argv) > file_index:
        with open(sys.argv[file_index], 'r') as file:
            number_lines(file, number_all_lines)
    else:
        number_lines(sys.stdin, number_all_lines)

if __name__ == '__main__':
    main()