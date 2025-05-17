# Task 1: Read a File and Handle Errors 
a="abc.txt"
try:
    fileread=open(a,'r')
    f=fileread.readlines()
    for i in f:
        print(i,end=" ")
except :
    print(f'{a} File not found')
