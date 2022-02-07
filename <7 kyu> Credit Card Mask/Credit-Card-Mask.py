# return masked string
def maskify(cc):
    if len(cc)<=4: 
        return cc
    else:
        s = (len(cc)-4)*"#" + cc[-4:]            
    return s
