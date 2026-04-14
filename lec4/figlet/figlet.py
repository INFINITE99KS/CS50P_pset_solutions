from sys import argv, exit
from pyfiglet import Figlet
import random

figlet = Figlet()

def main():
    font_list = figlet.getFonts()
    if len(argv) == 3:
        if(argv[1] == '-f' or argv[1] == '--font') and argv[2] in font_list:
            f = argv[2]
            figlet.setFont(font=f)
            s = input("Input: ")
            print("Output: ")
            print(figlet.renderText(s))
        else:
            exit("Invalid usage")
    elif len(argv) == 1:
        f = random.choice(font_list)
        figlet.setFont(font=f)
        s = input("Input: ")
        print("Output: ")
        print(figlet.renderText(s))
    else:
        exit("Invalid usage")

if __name__ == "__main__":
    main()
