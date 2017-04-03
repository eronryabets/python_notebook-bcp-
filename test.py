
i = 42
number = '42'
pi = 3.14
Flag = True
# все выше значения - не изменяемые
print(type(i), type(number), type(pi), type(Flag))
# type - выводит тип (класс) переменной
print(id(number), id(i))
#id - выводит
number = i
print(id(number), id(i))
#питон перезаписал обьекты, тоесть отменил ссылку на i
# (перменные это всеголишь адресса), дые переменные могут смотреть на один и тот же адресс
i = 2
print(number)
print(id(i))

# память подразделяется на два типа - изменяеммая (mutable) и нe изменяемая (immutable -скорость выше)
# проштудировать изменяемые и не зименяемые переменные (!)
#pep0008 - свод правил написания, общепринятые ( рекомендации к выполнению)

number = "42"
print(number, type(number))

number = int(number)
print(number, type(number))

print(number + 6)

#next

i = 42
print(str(42)+str(8))