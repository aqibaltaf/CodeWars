def length(head): 
    # your code here
    count = 0
    while head:
        count += 1
        head = head.next

    return count
