def main():
    eq = input("Expression: ")
    eq = eq.split()
    match eq[1]:
        case "*":
            print((float(eq[0]) * float(eq[2])))
        case "+":
            print((float(eq[0]) + float(eq[2])))
        case "-":
            print((float(eq[0]) - float(eq[2])))
        case "/":
            print((float(eq[0]) / float(eq[2])))
        case _:
            print("Invalid")
main()
