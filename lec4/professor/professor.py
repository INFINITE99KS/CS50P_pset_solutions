import random

def main():
    x_y = generate_integer(get_level())
    wrong_counter = 0
    ans_correct = 0
    for i in range(10):
        x = x_y[2*i]
        y = x_y[2*i+1]
        while True:
                try:
                    if wrong_counter == 3:
                        print(f"{x} + {y} = {x+y}")
                        wrong_counter = 0
                        break
                    else:
                        print(f"{x} + {y} = ", end="")
                    ans = int(input())
                    if ans != (x+y):
                        print("EEE")
                        wrong_counter += 1
                    if ans == (x+y):
                        ans_correct += 1
                        break
                except ValueError:
                    pass
    print("Score:", ans_correct)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    x_y = []
    for i in range(20):
        if level == 1:
            x_y.append(random.randint(pow(10, (level-1))-1, pow(10, level) - 1))
        else:
            x_y.append(random.randint(pow(10, (level-1)), pow(10, level) - 1))
    return x_y

if __name__ == "__main__":
    main()
