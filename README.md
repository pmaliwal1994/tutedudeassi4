# tutedudeassi4
ASSIGNMENT 4: Files, Exceptions, and Errors in Python
# Task 1: Read a File and Handle Errors 
a="abc.txt"
try:
    fileread=open(a,'r')
    f=fileread.readlines()
    for i in f:
        print(i,end=" ")
except :
    print(f'{a} File not found')


#Task 2: Write and Append Data to a File
fo=open("output.txt","w")
txt=input("Enter the text for write: ")
res=txt +"\n"
fo.write(res)
fo.close()

fo=open("output.txt","a")
txt=input("Enter the text for append: ")
res=txt +"\n"
fo.write(res)
fo.close()

