def get_number_of_words(text) -> int:
    words = text.split()
    return len(words)


def get_char_stats(text) -> list[dict[str, int | str]]:
    text = text.lower()
    char_stats: dict[str, int] = {}
    for char in text:
        if not char.isalpha():
            continue
        char_stats[char] = char_stats.get(char, 0) + 1
    return sorted(
        ({"name": key, "num": val} for key, val in char_stats.items()),
        reverse=True,
        key=lambda x: x["num"],
    )


def main() -> None:
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        text = f.read()
    print(f"--- Begin report of {filename} ---")
    print(f"{get_number_of_words(text)} wors found in the document\n")
    for char in get_char_stats(text):
        print(f"The '{char['name']}' character was found {char['num']} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
