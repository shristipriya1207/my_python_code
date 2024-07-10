#Reading from the file
'''f=open("demo.txt","r")
# data=f.read()
# data=f.read(5)
data=f.readline()
print(data)
# print(type(data))
data=f.readline()
print(data)

f.close()
'''

#writing to the file
# f=open("demo.txt","w")
# f=open("demo.txt","a")
# f.write("this is my secnd line")
# f.close()



# file i/o using with

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w") as f:
#         f.write("new data")



#deleting file

import os
os.remove("sample.txt")