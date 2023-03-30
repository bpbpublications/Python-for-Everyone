import os
try:
    print("inside try")
    print("hello there")
    os._exit(0)
except ValueError:
    print("inside except")
finally:
    print("inside finally")
