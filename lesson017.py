import sys
import ctypes

my_var = 10000
print(sys.getrefcount(my_var))

other_var = my_var

print(sys.getrefcount(my_var))

a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a))

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

print('b'*10)
b = a
print(id(b))
print(sys.getrefcount(b))
print(ref_count(id(b)))

print('c'*10)
c = a
print(id(c))
print(sys.getrefcount(c))
print(ref_count(id(c)))

print('-'*10)
c = 10
print(id(a))
print(sys.getrefcount(a))
print(ref_count(id(a)))

print('='*10)
b = None
print(id(b))
print(sys.getrefcount(a))
print(ref_count(id(a)))

print('+'*10)
a_id = id(a)
a = None
print(id(a))
print(sys.getrefcount(a_id))
print(ref_count(id(a_id)))



