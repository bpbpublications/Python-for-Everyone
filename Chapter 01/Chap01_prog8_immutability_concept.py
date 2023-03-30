a1 = 'python'
a2 = 'python'
a3 = 'python'
a4 = 'python'

#we have created 1 python object and 4 references
print(id(a1))
print(id(a2))
print(id(a3))
print(id(a4))

a1 = 'python2'
print(id(a1))


print(a1 is a2)
print(a2 is a3)
print(a3 is a4)
