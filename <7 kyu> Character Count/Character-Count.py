def validate_word(word):
    #your code here
    word = word.lower()
    uniue_char = list(set(word))
    a = []

    for letter in uniue_char:
        a.append(word.count(letter))

    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            return False

    return True
  
  
  ''' Efficient way
  
  def validate_word(word):
    word = word.lower()
    return len(set(word.count(c) for c in word)) == 1
  '''
