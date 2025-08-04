def get_book_text(file_path) -> str:
    with open(file_path) as file:
        contents = file.read()
    return contents


def number_of_words(text: str) -> int:
    word_count = len(text.split())
    return word_count


def number_of_characters(text: str) -> dict[str:int]:
    text_lower = text.lower()
    char_counts = {}

    for char in text_lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_on(items):
    return items["num"]


def desc_num_of_characters(n) -> list[dict]:
    l = []

    for pair in n:
        if pair.isalpha():
            l.append({"char": pair, "num": n[pair]})

    l.sort(reverse=True, key=sort_on)

    return l
