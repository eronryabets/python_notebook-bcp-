
"""
i = 5
j = 3
print  (id(i))
print  (id(j))
j = j + 1
print (hex(id(j)))
print(int(0x1de2a4c0))

# 501392544
# 501392544
# 0x1de2a4c0
# 501392576

"""

"""
a = 5
b = 5.0

print(5, 5.0)
print("id:", "\na:", id(a), "\nb:", id(b))
print("hex", "\na:", hex(a), "\nb:", float.hex(b))
print(int(0x5))

"""

a = 5
print(a) #a
print(id(a)) #501392608
print(hex(a)) #0x5
print(hex(id(a))) #0x1de2a4e0
print(int(0x5)) #5
print(int(0x1de2a4e0)) #501392608 если заИнтить Хексовое значение, то вернеться ИД

print(ctypes.string_at(id(0x1de2a4e0)))

