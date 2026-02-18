import sys

from stats import get_char_stats, get_number_of_words


def main(filename) -> None:
    with open(filename) as f:
        text = f.read()
    print(f"--- Begin report of {filename} ---")
    print(f"Found {get_number_of_words(text)} total words in the document\n")
    for char in get_char_stats(text):
        print(f"Character count {char['name']}: {char['num']} times")
    print("--- End report ---")


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(args[1])
