from bank import value

def main():
    test_value()

def test_value():
    assert value("HELLO") == 0
    assert value("what's up") == 100
    assert value ("hola") == 20

if __name__ == "__main__":
    main()
