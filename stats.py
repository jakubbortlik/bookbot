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
