from emoji import emojize

def main():
    usr = input("Input: ")
    print("Ouput:", emojize(usr, language='alias'))

if __name__ == "__main__":
    main()
