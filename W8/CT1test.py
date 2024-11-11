from CT1 import *


def test_zero():
    assert not is_prime(0)


def test_one():
    assert is_prime(1)


def test_two():
    assert not is_prime(2)


def test_seven():
    assert is_prime(7)


def test_thirty_nine():
    assert not is_prime(39)


def test_neg_prime():
    assert is_prime(-37)


def test_neg_nonprime():
    assert not is_prime(-45)


def test_all():
    test_one()
    test_zero()
    test_two()
    test_seven()
    test_thirty_nine()
    test_neg_prime()
    test_neg_nonprime()


test_all()
