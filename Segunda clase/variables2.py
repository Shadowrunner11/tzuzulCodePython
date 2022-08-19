import sys

size_integer = sys.getsizeof(12)

size_integer_2 = sys.getsizeof(1232423)

print('primer entero')
print(size_integer)
print('segundo entero')
print(size_integer_2)

# A python le da lo mismo si escribes 12 o 1232423
# ambos ocupan el mismo espacio

size_float = sys.getsizeof(12.4)

print(size_float)

size_boolean = sys.getsizeof(True)
# Los booleanos en python en realidad son enteros
print(size_boolean)

