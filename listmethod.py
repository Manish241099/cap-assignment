list1=[1,2,"red",4.5]
list2=["hii",300,8.5,"black"]
list3=[1,3,4,2,5]
#append method
list1.append("yo")
print(list1)

#clear method
list1.clear()
print(list1)

#copy method
y=list2.copy()
print(y)

#count method
c=list2.count("black")
print(c)

#extend method
list1.extend(list2)
print(list2)

#index method
z=list2.index("black")
print(z)

#insert method
list2.insert(2,"sheesh")
print(list2)

#pop method
list2.pop(2)
print(list2)

#remove method
list2.remove("hii")
print(list2)

#reverse method
list2.reverse()
print(list2)

#sort method
list3.sort()
print(list3)


