def main():
    take_word = input("Input: ")
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        take_word = take_word.replace(vowel, "")
        take_word = take_word.replace(vowel.upper(), "")
    print(f"Output: {take_word}")
main()
