def count_characters(word):

    char_count = {}

    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


if __name__ == "__main__":
    word = "Happiness"

    print(count_characters(word))
