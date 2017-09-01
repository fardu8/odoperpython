def fibo(n,a,b):
    s=[a,b]
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        s.append(c)
    return s
    
a=int(input("enter the first number in the series : "))
b=int(input("enter the second number in the series : "))
n=int(input("enter the number of terms needed : "))
print(fibo(n,a,b))
