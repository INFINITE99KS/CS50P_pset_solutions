import sys
import csv

if len(sys.argv) <3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    students = []
    with open(f"{sys.argv[1]}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(',')
            first = first.strip()
            students.append({"first": first, "last": last, "house": row["house"]})
    with open(f"{sys.argv[2]}", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
