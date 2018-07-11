import fibo

def test_fibo_10():
    result = fibo.fib2(10)
    expected_result = [0, 1, 1, 2, 3, 5, 8]
    assert result == expected_result


def test_fibo_0():
    result = fibo.fib2(0)
    expected_result = []
    assert result == expected_result

def test_fibo_negative():
    result = fibo.fib2(-1)
    expected_result = []
    assert type(result) == list