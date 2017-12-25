def rangoli(size,line):
    res=''
    res1=''
    for i in range(size-1,size - line -1,-1):
        res=res+chr(i+97)
        res1 =res[::-1]
    res=res+res1[1:]
    res='-'.join(res)
    w1=rangoli_addline(size)
    print(res.center(w1,'-'))
    


def rangoli_addline(size):
    n=97
    size +=n
    res=''
    res1=''
    for i in range(n,size):
        res =chr(i)+res
        res1 =res[::-1]
    res=res+res1[1:]
    res='-'.join(res)
    width=len(res)
    return width
def printing(size):
    for i in range(1,size+1):
        rangoli(size,i)
    for i in range(size - 1,0,-1):
        rangoli(size,i)



printing(26)