collections={1,2,3}
print(collections)

var ={2,4,"heloo","heloo",5,6,2}
print(var)      #it eliminates the duplicate value
print(len(var)) 

#empty set
var =set()
print(type(var))

#set is immutable but sets is mutuable

#methods
arr =set()
arr.add(2)
arr.add(3)
print(arr)

arr.remove(2)
print(arr)


arr.add("string")
arr.add((1,2,3))
#but we cannot add list because lisy is mutuable

print(arr)


array={"hello","bye","see you","take care"}
# array ={33,2,3,45,66,}
print(array.pop())   #it popped the element randomly


#union and intersection

set1={1,2,3}
set2={3,2,4}
print(set1.union(set2))
print(set1.intersection(set2))