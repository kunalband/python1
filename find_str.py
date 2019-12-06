import string
s1=input("enter the string:")
s2=input("enter the sub-string that you have to find:")
i=0
count=0
while i !=-1:
    i=s1.find(s2,i)
    if i == -1:
        break;
    print(s2,i)
    i+=1
    count+=1
print(count)

 

