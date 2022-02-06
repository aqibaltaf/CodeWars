def count_positives_sum_negatives(arr):    
    if(len(arr) == 0):
        return arr
    else:
        a = [0,0]
        for number in arr:
            if(number>0):
                a[0] += 1
            elif(number<0):
                a[1] += number

    return a
