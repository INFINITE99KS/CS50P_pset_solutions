import inflect
p = inflect.engine()

def main():
    name_list = []
    while True:
        try:
            s = input("Name: ")
            name_list.append(s)
        # Casue control+d triggers an EOF Error.
        except EOFError:
            print()
            break
    output = "Adieu, adieu, to " + p.join(name_list)
    print(output)

if __name__ == "__main__":
    main()
