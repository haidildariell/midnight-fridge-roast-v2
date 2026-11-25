import os

ENTRY = "At 12:03 my fridge beeped, locked, and displayed a tiny padlock, like a nightclub bouncer guarding three yogurts and a jar of pickles."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(text, path):
    validated = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(validated)


def main():
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
