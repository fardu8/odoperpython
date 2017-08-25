class order():
    def __init__(self):
        self.ord={}
    def add(self,s,amount):
        self.ord[s]=amount
    def show(self):
        print(self.ord)
        
    
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
            
            
veg=menu()
#non=menu()
veg + ["dosa",50]
#veg.add("sfe",345)
veg.add("vada",20)
veg.add("idly",35)
veg.add("idiyappam",40)
veg.add("pongal",30)
#non.add("idly",30)
#non.show()
x=order()
while True:
#    if str(input("")) is exit
#        break
    veg.show()
    a=str(input("enter item name or exit:"))
    if a=="exit":
        break
    x.add(a,int(input("enter amount:")))

x.show()
