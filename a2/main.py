import os
import sys

from base.b2 import hello


def main() -> str:
    print(hello('b2'))
    with open('base/hello_b2.txt',mode='r',encoding='utf8') as f:
        print(f.read())


if __name__ == '__main__':
    p = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, p)
    os.chdir(p)
    main()
