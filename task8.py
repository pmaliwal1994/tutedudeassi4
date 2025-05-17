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
