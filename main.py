def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def print_report(file_path, word_count, char_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    sorted_chars = sorted(char_counts.items(), key=lambda x: x[0])
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    word_count = count_words(text)
    char_counts = char_count(text)
    print_report(path, word_count, char_counts)

if __name__ == "__main__":
    main()
