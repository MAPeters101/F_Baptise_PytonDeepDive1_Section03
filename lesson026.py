a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))
print()

a = 500000000000000000000
b = 500000000000000000000
print(hex(id(a)))
print(hex(id(b)))
print()

a = -500000000000000000000
b = -500000000000000000000
print(hex(id(a)))
print(hex(id(b)))
print()

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(hex(id(d)))
print()


