def main():
    print(f"{shorten(input())}")


def shorten(word):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        word = word.replace(vowel, "")
        word = word.replace(vowel.upper(), "")
    return word


if __name__ == "__main__":
    main()
