import jpype
import jpype.imports
from jpype.types import *
from datetime import datetime

classpath = '/home/mokhles/TW-Project/LanguagesTest/Jython'

jpype.startJVM(classpath=[classpath])

Example = jpype.JClass('Example')

example = Example()

now = datetime.now()
result = example.add(1, 10**9)
after = datetime.now()
print("test takes:", after - now)

print(f"Sum: {result}")

jpype.shutdownJVM()
