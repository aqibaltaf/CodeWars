def well(x):
    count = x.count('good')
    if count > 2:
        return "I smell a series!"
    elif count == 0:
        return "Fail!"

    return "Publish!"
