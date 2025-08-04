import sys
from stats import (
    get_book_text,
    number_of_words,
    number_of_characters,
    desc_num_of_characters,
)


def main():
    if len(sys.argv) != 2:
        print(
            "Please pass a book path in the form of 'books/book_title.txt', Usage: python3 main.py <path_to_book>"
        )
        sys.exit(1)
    else:
        pass

    book = get_book_text(sys.argv[1])  # "books/frankenstein.txt"

    words = number_of_words(book)
    # print(f"{words} words found in the document\n")

    character_counts = number_of_characters(book)
    # print(character_counts)

    output = desc_num_of_characters(character_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for character in output:
        print(f"{character['char']}: {character['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
