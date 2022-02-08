def is_isogram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
        if string.lower().count(letter) > 1:
            return False
    return True
