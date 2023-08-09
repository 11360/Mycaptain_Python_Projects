n=int(input("Enter a number: "))
a=0
b=1
if n<0:
    print("No Fibonacci series")
elif n==0:
    print("The fibonacci series is 0")
elif n==1:
    print("The fibonacci series is 0 and 1")
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(b)
