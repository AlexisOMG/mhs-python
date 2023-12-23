import sys
from typing import TextIO, Tuple

def count_words(file: TextIO) -> Tuple[int, int, int]:
    line_count = word_count = byte_count = 0
    for line in file:
        line_count += 1
        word_count += len([word for word in line.split() if word])
        byte_count += len(line.encode('utf-8'))
    return line_count, word_count, byte_count

def main():
    if len(sys.argv) > 1:
        total_lines = total_words = total_bytes = 0

        for file_name in sys.argv[1:]:
            with open(file_name, 'r') as file:
                lines, words, bytes = count_words(file)
                print(f"{lines} {words} {bytes} {file_name}")
                total_lines += lines
                total_words += words
                total_bytes += bytes

        if len(sys.argv) > 2:
            print(f'{total_lines} {total_words} {total_bytes} total')
    else:
        lines, words, bytes = count_words(sys.stdin)
        print(f'{lines} {words} {bytes}')

if __name__ == '__main__':
    main()
