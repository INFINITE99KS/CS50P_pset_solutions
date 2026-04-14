from random import randint
def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1: raise ValueError
            x = randint(1, level)
        except ValueError:
            pass
        else:
            break

    while True:
        try:
            usr_input = int(input("Guess: "))
            if usr_input < 1:
                continue
            if usr_input < x:
                print("Too small!")
            elif usr_input > x:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
