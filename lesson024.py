a = 10
b = a

print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print(a == b)
print()

a = 50000000000
b = 50000000000
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print(a == b)
print()

a = [1, 2, 3]
b = [1, 2, 3]
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print(a == b)
print('-'*10)

a = 10
b = 10.0
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print(a == b)
print()

a = 10 + 0j
b = 10.0
print(hex(id(a)))
print(hex(id(b)))
print(a is b)
print(a == b)
print()

print(hex(id(None)))
print(type(None))
a = None
b = None
c = None
print(hex(id(None)))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))







