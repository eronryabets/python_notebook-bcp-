#LECTURE #
"""
alian = print(type(32))
alian
balian = type(32)
print(balian)
"""
"""
print(id(3))
alian = 3
print(id(alian))
"""
"""
print(float(99/100))
a = 50.0 #class float
b = 50 #class int
print(type(a))
print(type(b))

print(a + b)
c = a + b
print(type(c))

print('word.............................')

print(str(555) + "word") # = print(format(555) + "word")
#format(555) = str(555) Форматирование (обычно форматирование строки).
"""

"""
a = 50
print(type(a)) #int
f = float(a)
print(f) #float 50.0
print(type(f)) #float

print(1 + 2 * float(3) / 4 - 5 - 2.5) #  =  (1 + (2 * float(3) / 4) - 5 - 2.5) = 1 + (1.5) - 5 - 2.5  = -5.0
"""

"""
#Python также может преобразовывать числа с плавающей точкой в целые числа
#(помните, что число обрезается до целой части):
print(int(3.9999999)) # int = 3
print(int(-2.3)) # int = -2
"""

"""
#Конвертация типов
#float преобразуем в число с плав.точкой
print(float(50))
print(float('3.14'))
#str преобразуем в строчку
print(str(50))
print(str(3.14))
"""

"""

alian = "123"
print(type(alian)) #str
#print(alian + 1) #error
balian = int(alian)
print(type(balian)) #int
print(balian + 1 ) # = 124 преобразовали значение в Инт и выполнили сложение 123 + 1
#calian = "hello"
#dalian = int(calian) ValueError: invalid literal for int() with base 10: 'hello'

"""
"""
#приведение типов ( можем решить проблему целоисленного деления)
minute = 59
print(float(minute/60)) # прошла 0.9833333333333333 ая часть часа
#другой вариант ввести плав.точку
minute = 59
print(minute/60.0)
#Пример неявного преобразования типа
"""




