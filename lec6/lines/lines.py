import sys

if len(sys.argv) <2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
    
try:
    with open(f"{sys.argv[1]}") as file:
        line_count = 0
        for line in file:
            line = line.lstrip()
            if (not line.startswith("#") and line != "") or (not line.startswith("") and line != ""):
                line_count += 1
        print(line_count)
except FileNotFoundError:
    sys.exit("File does not exist")

