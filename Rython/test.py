import rust_example
from datetime import datetime

now = datetime.now()
result = rust_example.add(1, 10**9)
after = datetime.now()
print("test takes:", after - now)
print(f"Sum: {result}")
