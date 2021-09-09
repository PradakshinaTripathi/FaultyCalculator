print("Enter the first number")
a=int(input())
print("Enter the second number")
b=int(input())
print("Operator you want to use")
c=input()
if(a==45 and b==3 and c=='*'):
    print("555")
elif(a==56 and b==9 and c=='+'):
    print("77")
elif(a==56 and b==6 and c=='/'):
    print("4")
elif(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    print(a/b)
else:
    ("Enter the correct Operator!")
input()

