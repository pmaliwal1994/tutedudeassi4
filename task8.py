#Task 2: Write and Append Data to a File
a="output.txt"
fo=open(a,"w")
txt=input("Enter the text for write: ")
res=txt +"\n"
fo.write(res)
fo.close()

fo=open(a,"a")
txt=input("Enter the text for append: ")
res=txt +"\n"
fo.write(res)
fo.close()

try:
    fileread=open(a,'r')
    f=fileread.readlines()
    for i in f:
        print(i,end=" ")
except :
    print(f'{a} File not found')
