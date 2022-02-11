def get_count(sentence):
    vowels = "aeiou"
    count = 0

    for letter in vowels:
        count += sentence.count(letter)

    return count
