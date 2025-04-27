#empty list
print([])

#making list
a=["marium","aftab","marium","khan","ahmed","marium"]
print(a)
print(a[0])

#change the value
a[2]="arshia"
print(a)

#sorting
a.sort()
print(a)

#reverse
a.reverse()
print(a)

#append
a.append("afifa")
print(a)

#insert at specific index
a.insert(1,"Ali")
print(a)

#remove specific value
a.remove("Ali")
print(a)

#remove at specific index
a.pop(2)
print(a)

#count a specific value at list
counting=a.count("marium")
print(counting)

a.clear()
print(a)