def disemvowel(string_):
    vowels = ["a","e","i","o","u", "A" , "E", "I", "O", "U"]
    
    '''Check if any letter from the array is in the string then remove it'''
    for letter in vowels:
        if letter in string_:
            string_ = string_.replace(letter,"")
            
    return string_
