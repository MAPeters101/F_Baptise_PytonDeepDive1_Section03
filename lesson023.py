a = 'hello'
b = a
c = 'hello'

print(f'a: {hex(id(a))}')
print(f'b: {hex(id(b))}')
print(f'c: {hex(id(c))}')
print()

b = "hello world"
print(f'a: {hex(id(a))}')
print(f'b: {hex(id(b))}')
print(f'c: {hex(id(c))}')
print()

a = [1, 2, 3]
b = a
print(f'a: {hex(id(a))}')
print(f'b: {hex(id(b))}')
print()
b.append(100)
print(f'a: {hex(id(a))}')
print(f'b: {hex(id(b))}')
print(f'a: {a}')
print(f'b: {b}')
print()

a = 10
b = 10
print(f'a: {hex(id(a))}')
print(f'b: {hex(id(b))}')
print(f'a: {a}')
print(f'b: {b}')

print()

a = 5000000000000
b = 5000000000000
print(f'a: {hex(id(a))}')
print(f'b: {hex(id(b))}')
print(f'a: {a}')
print(f'b: {b}')






