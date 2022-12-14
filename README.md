# python-path

主要知识点: 
- `正常引用` 
- `main在文件夹内` 
- `单元测试`

## 1.正常引用

main.py在根目录,依赖文件夹也在根目录
``` python
python-path
├── a1/
|  └── a1.py
├── base/
|  ├── b1.py
|  └── hello_b1.txt
├── LICENSE
├── main.py
└── README.md
```
b1.py
``` python
def hello(mod: str) -> str:
    return f'hello {mod} => b1'

```
a1.py
``` python
from base.b1 import hello

def hello_a1(mod: str) -> str:
    return hello(f'{mod} => a1')

```

main.py
``` python
from a1.a1 import hello_a1


def main() -> str:
    print(hello_a1('main'))
    with open('base/hello_b1.txt', mode='r', encoding='utf8') as f:
        print(f.read())


if __name__ == '__main__':
    main()

```
输出
``` python
$ python main.py
hello main => a1 => b1
hello file b1
```

## 2 main在文件夹内
### 2.1 main.py在文件夹内,依赖文件夹也在文件夹内
1. 把依赖文件夹目录, 添加到系统路径
2. 如果要访问文件, 需要设置工作空间`os.chdir`
``` python
python-path
├── a2/
|  ├── base/
|  |  ├── b2.py
|  |  └── hello_b2.py
|  └── main.py
├── LICENSE
└── README.md

```
b2.py
``` python
def hello(name: str) -> str:
    return f'hello {name}'

```
main.py
``` python
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

```

### 2.2 main.py在文件夹内,依赖文件夹在根目录
把依赖文件夹目录, 添加到系统路径, 可以正常访问文件
``` python
python-path
├── a3/
|  └── main.py
├── base/
|  ├── b1.py
|  └── hello_b1.txt
├── LICENSE
└── README.md

```
b1.py

``` python
def hello(mod: str) -> str:
    return f'hello {mod} => b1'

```
main.py
``` python
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

```

## 3. 单元测试
把依赖文件夹目录, 添加到系统路径
``` python
python-path
├── base/
|  ├── b1.py
|  └── hello_b1.txt
├── LICENSE
├── README.md
└── tests/
   ├── conftest.py
   └── test_base.py
```
b1.py
``` python
def hello(mod: str) -> str:
    return f'hello {mod} => b1'

```
conftest.py
``` python
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

```
test_base.py

``` python
from base.b1 import hello


def test_hello():
    print(1)
    assert 'hello test => b1' == hello('test'), 'test error'

def test_file():
    with open('base/hello_b1.txt', mode='r', encoding='utf8') as f:
        assert 'hello file b1' == f.read(), 'file error'

```
运行
``` python
$ py.test.exe -vs .\tests\test_base.py
collected 2 items

tests/test_base.py::test_hello 1
PASSED
tests/test_base.py::test_file PASSED
```
