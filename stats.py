def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(text: str) -> int:
    return len(text.split())

def count_character_frequency(text: str) -> dict:
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_counts(char_counts: dict) -> list:
    sorted_list = [{'char': char, 'count': count} for char, count in char_counts.items()]
    sorted_list.sort(key=lambda x: x['count'], reverse=True)
    return sorted_list

def analyze_and_print(path: str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    book_contents = get_book_text(path)
    word_count = get_num_words(book_contents)
    char_counts = count_character_frequency(book_contents)
    sorted_chars = sort_character_counts(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for entry in sorted_chars:
        char = entry['char']
        count = entry['count']
        if char.isalpha():  # only include alphabetic characters
            print(f"{char}: {count}")

    print("============= END ===============")
