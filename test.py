from datetime import datetime

def add(a, b):
    res = 0
    for i in range(a, b):
        res += i
    return res

now = datetime.now()
add(1, 10**9)
after = datetime.now()

print("test takes:", after - now)