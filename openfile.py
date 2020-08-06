file = open('demo.txt') ## opens demo.txt file
read = file.readlines() ## this command read the lines of demo.txt and stores in "read" variable
print(read)  ## prints the lines of demo.txt
print("\n As you all can see when we type some stuff in text editor the enter is considered as \\n ")
print("\n It adds new line to a program : ")
print("\n")

for r in read :  ## loop for printing the lines in sequence.
    print(r)
