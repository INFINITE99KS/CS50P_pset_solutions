def main():
    greeting = input("Greeting: ")
    if greeting.lower().strip()[0] == 'h':
        altered = greeting.lower().split()
        if "hello" in altered[0]:
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

main()
