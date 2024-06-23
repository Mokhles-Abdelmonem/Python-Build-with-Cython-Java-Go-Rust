import example
from datetime import datetime

now = datetime.now()
example.add(1, 10**9)
after = datetime.now()

print("test takes:", after - now)
