import sys
import codecs
import re


def first_token(line):
    if len(line) > 0 and line[0] == '"':
        tokens = re.split(',\s*', line)
        return tokens[0]
    return ''


def parse_to_dictionary(lines):
    dic = {}
    for line in lines:
        if len(line) > 0 and line[0] == '"':
            tokens = re.split(',\s*', line)
            if len(tokens) >= 2:
                dic[tokens[0]] = line
    return dic


def main():
    if len(sys.argv) < 2:
        print('usage:\n\tpython {} <language.txt>'.format(__file__))
        return
    target_path = sys.argv[1]

    original_lines = codecs.open('Japanese.txt', 'r', 'utf-8').readlines()
    target_lines = codecs.open(target_path, 'r', 'utf-8').readlines()
    if len(target_lines) <= 0:
        return

    target_tokens = parse_to_dictionary(target_lines)

    # output first language line
    print(target_lines[0], end='')

    for line in original_lines:
        token = first_token(line)
        if token in target_tokens:
            print(target_tokens[token], end='')

        else:
            if len(line) > 0 and line[0] == '#':
                print()
                print(line, end='')


if __name__ == "__main__":
    main()
