def create_phone_number(n):
    #your code here
    Phone_no = "("
    for i in range(len(n)):
        if i == 5:
            Phone_no += str(n[i]) + "-"
        elif i < 3:
            Phone_no += str(n[i])
            if i == 2:
                Phone_no += ") "
        elif i >= 3:
            Phone_no += str(n[i])


    return Phone_no
  
  
  ''' Efficient way 
  
  def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
 
  '''
