def main():
    with open("./books/frankensein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        unique_letters = count_unique_letters(file_contents)

        print(
            f"{word_count} words found in the document",
        )

        for letter, count in unique_letters.items():
            print(f"The '{letter}' character was found {count} times")


def count_words(file_contents):
    return len(file_contents.split())


def count_unique_letters(file_contents):
    lower_case = file_contents.lower()
    letters_set = set(lower_case)
    letter_count = {}

    for letter in letters_set:
        if letter.isalpha():
            letter_count[letter] = lower_case.count(letter)

    return letter_count


if __name__ == "__main__":
    main()
