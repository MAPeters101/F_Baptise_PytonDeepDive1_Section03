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




