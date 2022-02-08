"""Just me messing around with wordle.

Not really intended to cheat or whatever, I just wanted a program to play around with word comprehension a bit
because I was a bit rusty. So I made this and it's not really meant to be used for anything.
"""


def refresh_word_list() -> list:
    """Get the system dictionary and remove invalid words."""
    with open("/usr/share/dict/cracklib-small", "r") as file_data:
        dictionary = file_data.read().splitlines()

    dictionary = [word for word in dictionary if len(word) == 5]
    dictionary = [word for word in dictionary if not any(char.isdigit() for char in word)]
    dictionary = [word for word in dictionary if "'" not in word]
    return dictionary


def letters_to_exclude(word_list: list, exclude_list: list) -> list:
    """Remove words from word_list if they are in exclude_list of characters and return."""
    return [word for word in word_list if all(char not in exclude_list for char in word)]


def known_letters(word_list: list, letters: list) -> list:
    """Make a new list if all the letters are in the world_list."""
    return [word for word in word_list if all(letter in word for letter in letters)]


def known_letters_by_pos(words: list, letters: list) -> list:
    """Remove words from word_list that don't have letters in the letter position in the letters list and return."""
    # if all letters are @ return the word list
    if all(letter == "@" for letter in letters):
        return words
    new_word_list = []
    # check if all of the letters in letters are in the word in the correct positions and add to new_word_list
    for word in words:
        remove = any(letters[i] != "@" and word[i] != letters[i] for i in range(len(word)))

        if not remove:
            new_word_list.append(word)

    return new_word_list


def split_by_pos(data_input: str) -> list:
    """Split a string data_input by position"""
    return list(data_input)


def input_clean(message: str) -> str:
    """Remove all invalid characters and spaces, new lines, and make lowercase."""
    while True:
        data_input = input(message)
        data_input.replace("\n", "").replace(" ", "").lower().strip()
        if len(data_input) <= 5:
            break
        print("Input must be less than 5 characters long.")
    return data_input


def solve(exclude: list, known_pos: list, known: list):
    """Solve the wordle."""
    words = refresh_word_list()
    words = letters_to_exclude(words, exclude)
    words = known_letters_by_pos(words, known_pos)
    words = known_letters(words, known)
    print(f"Your word options are: {words}")


def main():
    print(
        "Start with: raise\n"
        "Input for valid letters is just letters you know without spaces.\n"
        "Same for letters to exclude.\n"
        "For position letters looks more like @@if@ where in pos 3 and 4 has i and f respectively.\n\n"
        "Sample input would be... known ise, exclude xyz, pos @@@i@. Will result in words that have ise"
        " without xyz and with i in pos 4.\n"
        "Keep going until you have the solution.\n"
    )
    exclude: list = []
    known: list = []
    while True:
        known.extend(split_by_pos(input_clean("All valid letters: ")))
        exclude.extend(split_by_pos(input_clean("Letters to exclude: ")))
        known_pos_letters = split_by_pos(input_clean("Known position letters (if unknown leave @): "))
        solve(exclude, known_pos_letters, known)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        pass
