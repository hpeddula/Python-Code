n=int(input("Enter the number"))
A=set()
m=int(input("Enter the number"))
B=set()
C=set()
D=[]
count=0
for i in range(n):
    A.add(input("Enter the roll numbers for English"))
for i in range(m):
    B.add(input("Enter the roll numbers for French"))
C=A ^ B
for i in C:
    D.append(int(i))
D.sort()
for i in count:
    count +=1
print(count)
    
    
