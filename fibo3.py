def fibo(n,a,b):
    for i in range(n):
        if i==0: yield a
        elif i==1: yield b
        else:
            c=a+b
            a=b
            b=c
            yield c
    
a=int(input("enter the first number in the series : "))
b=int(input("enter the second number in the series : "))
n=int(input("enter the number of terms needed : "))
for x in fibo(n,a,b):
    print(x)
