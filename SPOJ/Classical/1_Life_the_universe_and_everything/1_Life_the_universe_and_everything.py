import sys

def main():
    for line in sys.stdin:
        if int(line) == 42:
            break
        print(line, end='', flush=True)

if __name__ == '__main__':
    main()
