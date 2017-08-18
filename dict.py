s=input("enter the string by using ; as seperator between two datas : ")
d=dict(z.split('=') for z in s.split(';'))
print(d) 
