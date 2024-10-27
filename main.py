path_to_file = "books/frankenstein.txt"

def get_file_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def print_file_contents_to_console(file_contents):
    print(file_contents)

def count_words(file_contents):
     return len(file_contents.split())

def count_characters(string):
    lowered_string = string.lower()

    character_counts = {}
    for char in lowered_string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def print_word_count_report(dict):
    for key in dict:
        print(f"The '{key} character was found {dict[key]} times" )


def main():
    frankenstein_file_contents = get_file_contents(path_to_file)
    print_file_contents_to_console(frankenstein_file_contents)
    print(count_words(frankenstein_file_contents))
    fstein_dict = count_characters(frankenstein_file_contents)
    print_word_count_report(fstein_dict)


main()