items=['Harsha','is dead',25]
name,action,date=['Harsha','is dead',25]
print(name,action,date)
def first_last(grades):
    first,*middle,last=grades
    avg=sum(middle)//len(grades)
    print(avg)

first_last([23,45,66,66,77,55])