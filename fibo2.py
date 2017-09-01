class fibo():
    def __init__(self):
        self.a=self.b=0
    def __iter__(self):
        return self
    def __next__(self):
        if c==1:
            return self.a
        if c==2:
            return self.b
        y=self.a+self.b
        self.a=self.b
        self.b=y
        return y

f=fibo()
c=1
f.a=int(input("enter the first number in the series : "))
f.b=int(input("enter the second number in the series : "))
n=int(input("enter the number of terms needed : "))
x=iter(f)
while True:
    if c>n:
        break      
    print(next(x))
    c+=1
