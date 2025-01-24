# Book paths defined
path_to_frankenstein = "books/frankenstein.txt"

# alphabet list defined
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Counts the number of characters in a text
def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    

# Counts the number of words in a text
def count_words(text):
    words = text.split()
    return len(words)

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

# Print a report of the book
def print_report(words, characters):
    print(f"--- Begin report of {path_to_frankenstein} ---")
    print(f"{words} words found in the document")
    list_of_chars = [{"character":key,"num":value} for key, value in characters.items()]
    list_of_chars.sort(reverse=True, key=sort_on)
    print("")
    for char_dict in list_of_chars:
        current_character = char_dict["character"]
        current_num = char_dict["num"]
        if current_character in alphabet:
            print(f"The '{current_character}' character was found {current_num} times")
    print("--- End report ---")
    


# Main function
def main():
    with open(path_to_frankenstein) as f:
        file_contents = f.read()
        total_words = count_words(file_contents)
        total_characters = count_characters(file_contents)
        print_report(total_words, total_characters)

main()