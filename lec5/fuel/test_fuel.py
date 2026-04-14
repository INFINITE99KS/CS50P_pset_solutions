from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("-2/3")
    with pytest.raises(ValueError):
        convert("2.5/3")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(30) == "30%"


if __name__ == "__main__":
    main()
