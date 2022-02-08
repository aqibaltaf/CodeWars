def array(string):
    #your code here
    arr = string.split(",")
    if(len(arr) <= 2): return None
    
    return " ".join(arr[1:-1])
