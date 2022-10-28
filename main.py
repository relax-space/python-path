from a1.a1 import hello_a1


def main() -> str:
    print(hello_a1('main'))
    with open('base/hello_b1.txt', mode='r', encoding='utf8') as f:
        print(f.read())


if __name__ == '__main__':
    main()
