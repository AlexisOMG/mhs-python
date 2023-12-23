import sys
from typing import TextIO

def tail(file: TextIO, num_lines=10) -> None:
    lines = file.readlines()
    for line in lines[-num_lines:]:
        print(line, end='')

def main():
    num_lines = 10
    if len(sys.argv) == 1:
        num_lines = 17
        tail(sys.stdin, num_lines)
    else:
        for i, file_name in enumerate(sys.argv[1:], 1):
            if len(sys.argv) > 2:
                print(f'==> {file_name} <==')
            
            with open(file_name, 'r') as file:
                tail(file, num_lines)

            if i < len(sys.argv) - 1:
                print()

if __name__ == '__main__':
    main()
