import os
import sys


def main():
    print(hello('a2'))


if __name__ == '__main__':
    sys.path.insert(
        0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from base.b1 import hello
    main()
