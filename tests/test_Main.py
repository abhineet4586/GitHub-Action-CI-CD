from src.main import add,sub,multiply


def testAdd():
    assert add(2,3) == 5
    assert add(0,0) == 0
    assert add(1,7) == 8

def testSub():
    assert sub(5,3) == 2
    assert sub(0,0) == 0
    assert sub(3,5) == -2

def testMultiply():
    assert multiply(2,3) == 6
    assert multiply(2,0) == 0
    assert multiply(3,-4) == -12