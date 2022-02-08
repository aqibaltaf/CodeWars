def get_middle(s):
    length = int(len(s)/2)
    if len(s)%2 == 0: return(s[length-1: length+1]) 

    return(s[length:length+1])
