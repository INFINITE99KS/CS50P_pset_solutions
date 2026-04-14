def main():
    my_str = input("camelCase: ")
    for c in my_str:
        if c.isupper():
            index = my_str.find(c)
            my_str = my_str[:index] + "_" + c.lower() + my_str[index+1:]
    print(my_str)

main()
