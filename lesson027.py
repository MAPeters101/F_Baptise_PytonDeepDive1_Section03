a = 'hello'
b = 'hello'
print(hex(id(a)))
print(hex(id(b)))
print(a == b)
print(a is b)
print()

a = 'hello world'
b = 'hello world'
print(hex(id(a)))
print(hex(id(b)))
print(a == b)
print(a is b)
print()

a = '123, hello world adgsdgadgs asdgasdg agdfgasdgjdhhjghdst'
b = '123, hello world adgsdgadgs asdgasdg agdfgasdgjdhhjghdst'
print(hex(id(a)))
print(hex(id(b)))
print(a == b)
print(a is b)
print()

a = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
b = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
print(hex(id(a)))
print(hex(id(b)))
print(a == b)
print(a is b)
print()

import sys
a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
print(a == b)
print(a == c)
print(a is b)
print(a is c)
print()

a = 'a long string that is not interned' * 200
b = 'a long string that is not interned' * 200
print(hex(id(a)))
print(hex(id(b)))
print(a == b)
print(a is b)
print()






def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass

import time
start = time.perf_counter()
compare_using_equals(10_000_000)
end = time.perf_counter()
print('equality', end-start)

start = time.perf_counter()
compare_using_interning(10_000_000)
end = time.perf_counter()
print('equality', end-start)



