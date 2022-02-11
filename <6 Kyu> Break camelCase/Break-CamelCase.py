def solution(s):
    new = ""
    for letter in s:
        new += letter
        if letter.isupper():
            new = new[:-1] + " " + letter 

    return new
