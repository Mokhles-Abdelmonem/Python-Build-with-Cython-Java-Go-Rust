import ctypes
from datetime import datetime

# Load the shared library
example = ctypes.CDLL('./example.so')

# Define the argument and return types of the Add function
example.Add.argtypes = (ctypes.c_int, ctypes.c_int)
example.Add.restype = ctypes.c_int

# Call the Add function and print the result
now = datetime.now()
result = example.Add(1, 10**9)
after = datetime.now()
print("test takes:", after - now)
print(f"Sum: {result}")
