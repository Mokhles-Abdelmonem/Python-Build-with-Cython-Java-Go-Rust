# example.pyx
def add(int a, int b):
    cdef int i
    cdef int sum = 0
    for i in range(a, b):
        sum += i
    return sum
