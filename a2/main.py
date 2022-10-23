import os
import sys

from base.b2 import hello


def main() -> str:
    print(hello('b2'))


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
