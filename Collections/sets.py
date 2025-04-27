
#empty set consider as tuple
a={}
print(type(a))

#initialize empty set as
a=set()
print(a)

#making set (set sort by default ascending)
a={2,5,"marium",3,7,2,5,1}
print(a)

#adding value
a.add(120)
print(a)

#pop -- pop remove value from start
a.pop()
print(a)

a.remove(3)
print(a)

print(len(a))