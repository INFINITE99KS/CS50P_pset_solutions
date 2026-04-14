def main():
    my_answer = input("What's the answer to the Great Question of Life, the Universe, and Everything? ")
    if my_answer.strip() == "42" or my_answer.strip().lower() == "forty-two" or my_answer.strip().lower() == "forty two":
        print("Yes")
    else:
        print("No")

main()
