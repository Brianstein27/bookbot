def count_book_words(book):
    return len(book.split())

def get_book_text(path):
    with open(path) as book:
        return book.read()

def count_character_occurences(book):
    letters = list(book)
    character_occurences = {}

    for letter in letters:
        if letter.isalpha():
            lowered_letter = letter.lower()

            if lowered_letter in character_occurences:
                character_occurences[lowered_letter] += 1
            else:
                character_occurences[lowered_letter] = 1

    return character_occurences

def sort_character_occurences(dict):
    occurence_list = []

    for entry in dict:
        if entry != " ":
            occurence_list.append({"character": entry, "num": dict[entry]})

    def sort_on(dict):
        return dict["num"]

    occurence_list.sort(reverse=True, key=sort_on)

    return occurence_list

frankenstein = get_book_text('./books/frankenstein.txt')
word_count = count_book_words(frankenstein)
character_occurences = count_character_occurences(frankenstein)
sorted_character_occurences = sort_character_occurences(character_occurences)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
print("")

for entry in sorted_character_occurences:
    print(f"The '{entry['character']}' character was found {entry['num']} times")

print("--- End report ---")
