class order():
    def __init__(self):
        self.ord={}
        self.price=0
    def add(self,s,amount):
        self.ord[s]=amount
    def show(self):
        for i,j in self.ord.items():
            print(i,j)
    def __setitem__(self,s,n):
        self.ord[s]=n
        self.price+=n*veg.mymenu[s]
        
    
class menu():
   # mymenu={}# this is a class variable.
    def __init__(self):
        self.mymenu={}
    def add(self,s,n):
            self.mymenu[s]=n
    def show(self):
            print(self.mymenu)
    def __add__(self,s):
            self.mymenu[s[0]]=s[1]
            return self
            
            
veg=menu()
veg + ["dosa",50] + ("chapathi",40)
veg.add("vada",20)
veg.add("idly",35)
veg.add("idiyappam",40)
veg.add("pongal",30)
x=order()
while True:
    veg.show()
    a=str(input("enter item name or exit:"))
    if a=="exit":
        break
    elif a not in veg.mymenu:
        print("item is not there in menu")
        continue
    x[a]=int(input("enter quantity :"))
print("your order : ")
x.show()
print("total amount : ",x.price)

