def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    given = fraction.split("/")
    if len(given) != 2:
        raise ValueError

    num = int(given[0])
    denom = int(given[1])

    if denom == 0:
        raise ZeroDivisionError
    if num > denom:
        raise ValueError
    if num < 0 or denom < 0:
        raise ValueError

    return round(num / denom * 100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
