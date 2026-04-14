import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length
    if not (2 <= len(s) <= 6):
        return False

    # First two must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Only letters and digits
    if not s.isalnum():
        return False

    digit_seen = False

    for c in s:
        if c.isdigit():
            if not digit_seen:
                # first digit cannot be zero
                if c == "0":
                    return False
                digit_seen = True
        else:
            # letter after a digit → invalid
            if digit_seen:
                return False

    return True

if __name__ == "__main__":
    main()
