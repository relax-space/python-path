from base.b1 import hello


def test_hello():
    print(1)
    assert 'hello test => b1' == hello('test'), 'test error'

def test_file():
    with open('base/hello_b1.txt', mode='r', encoding='utf8') as f:
        assert 'hello file b1' == f.read(), 'file error'
