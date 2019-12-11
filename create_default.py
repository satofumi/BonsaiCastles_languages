import sys
import codecs


def replace_token(line):
    if len(line) > 0 and line[0] == '"':
        tokens = line.split(', ')
        return tokens[0] + ', ' + tokens[0] + '\n'

    return line


def main():
    with codecs.open('Japanese.txt', 'r', 'utf-8') as f:
        line = f.readline()
        while line:
            print(replace_token(line), end='')
            line = f.readline()


if __name__ == "__main__":
    main()
