from base.b1 import hello


def test_hello():
    print(1)
    assert 'hello test => b1' == hello('test'),'test error'