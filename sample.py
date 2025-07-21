a = bytearray(b'Hello')
m = memoryview(a)
m[0] = 65
print(m)
print(m[4])
print(a)
print(type(m))
