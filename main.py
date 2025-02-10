def count_letters(text):
    letters = {}
    for letter in text:
        letters[letter] = letters.get(letter, 0) + 1
    return letters

def sort_letters(dict_text):
    list_dicts = [{"letter" : letter, "count": count} for letter, count in dict_text.items() if letter.isalpha()]
    list_dicts.sort(reverse=True, key=lambda d: d["count"])
    return list_dicts

def print_report(letter_list):
    print("--- Start of report ---")
    for item in letter_list:
        letter = item["letter"]
        count = item["count"]
        print(f"The '{letter}' character was found {count} times")
    print("--- End of report ---")

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        words = len(file_contents.split())

        lowercase_file_contents = file_contents.lower()
        dict_letters = count_letters(lowercase_file_contents)
        sorted_letters = sort_letters(dict_letters)
        print_report(sorted_letters)

if __name__ == "__main__":
    main()
