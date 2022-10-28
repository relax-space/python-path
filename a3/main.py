import os
import sys


def main():
    print(hello('a2'))
    with open('base/hello_b1.txt',mode='r',encoding='utf8') as f:
        print(f.read())


if __name__ == '__main__':
    sys.path.insert(
        0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from base.b1 import hello
    main()
