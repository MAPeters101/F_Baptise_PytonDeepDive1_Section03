
a = 10
print(type(a))
b = int(10)
print(b)
print(type(b))
#help(int)
#print(help(int))


c = int()
print(c)

c = int('101', base=2)
print(c)

def square(a):
    return a ** 2

print(type(square))
print(hex(id(square)))

f = square
print(hex(id(f)))
print(f is square)
print(f(2))

def cube(a):
    return a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

f = select_function(1)
print(f is square)
print(f(2))
print()

f = select_function(2)
print(f is cube)
print(f(2))
print()
