with open("hello.txt","w") as file:
    file.write("this is a sample text\n")

with open("hello.txt","a") as file:
    file.write("using append\n")

with open("hello.txt","r") as file:
    print(file.read())
