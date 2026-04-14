def main():
    print(value(input()))


def value(greeting):
    if greeting.lower().strip()[0] == 'h':
        altered = greeting.lower().split()
        if "hello" in altered[0]:
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()
