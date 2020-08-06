file = open('demo.txt')
read = file.readlines()
print(read)
print("\n As you all can see when we type some stuff in text editor the enter is considered as \\n ")
print("\n It adds new line to a program : ")
print("\n")

for r in read :
    print(r)