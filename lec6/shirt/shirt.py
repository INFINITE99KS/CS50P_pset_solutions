import sys
from PIL import Image, ImageOps
allowed_extensions = [".jpg", '.jpeg', '.png']

def main():
    if len(sys.argv) <3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if not check(sys.argv[1]) or not check(sys.argv[2]):
        sys.exit("Invalid Output")
    if (sys.argv[1].split('.'))[1] != (sys.argv[2].split('.'))[1]:
        sys.exit("Input and output have different extensions")
    try:
        with Image.open(f"{sys.argv[1]}") as image:
            shirt = Image.open("shirt.png")
            fitted_image = ImageOps.fit(image, shirt.size)
            fitted_image.paste(shirt, (0,0), shirt)
            fitted_image.save(f"{sys.argv[2]}")

    except FileNotFoundError:
        sys.exit("Input does not exist")


def check(n):
    for ext in allowed_extensions:
        if n.endswith(ext):
            is_within = True
            break
    return is_within

if __name__ == "__main__":
    main()
