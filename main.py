import string

def main():
    path = "books\\frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    words = words_in_text(file_contents)
    chars = chars_in_text(file_contents)
    sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    report(path, words, sorted_chars)


def report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{len(words)} words found in the document")
    print("")
    for char in chars:
        print(f"The '{char}' character was found {chars[char]} times")


def words_in_text(input):
    words = input.split()
    return words 

def chars_in_text(input):
    words = input.split()
    letters = {}
    for word in words:
        for letter in word:
            if letter in string.ascii_letters:
                letter_lower = letter.lower()
                if letter_lower in letters:
                    letters[letter_lower] += 1
                else:
                    letters[letter_lower] = 1
    return letters

main()