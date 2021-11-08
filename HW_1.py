# 1. Создать переменную типа String
print('Hello World')
# 2. Создать переменную типа Integer
x = 1
print(x)
# 3. Создать переменную типа Float
y = 1.5
print(y)
# 4. Создать переменную типа Bytes
by = bytes(25)
print(by)
# 5. Создать переменную типа List
elements = [1, 85, 'wow', 'mik']
print(elements)
# 6. Создать переменную типа Tuple
cort = (5, 45, 58, 'fol')
print(cort)
# 7. Создать переменную типа Set
s = {'1', '5', '15', '28'}
print(s)
# 8. Создать переменную типа Frozen set
fs = {'wof', '4', 'Julia', '24'}
print(fs)
# 9. Создать переменную типа Dict
dic = {'key': '1245', 'name': 'Julia'}
print(dic)
# 10. Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type('Hello World'))
x = 1
print(type(x))
y = 1.5
print(type(y))
by = bytes(25)
print(type(by))
elements = [1, 85, 'wow', 'mik']
print(type(elements))
cort = (5, 45, 58, 'fol')
print(type(cort))
s = {'1', '5', '15', '28'}
print(type(s))
fs = {'wof', '4', 'Julia', '24'}
print(type(fs))
dic = {'key': '1245', 'name': 'Julia'}
print(type(dic))
# 11. Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
s_1 = 'Python '
s_2 = 'язык программирования'
s_3 = s_1 + s_2
print(s_3)
# 12. Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print('Hello World', str(1))
# 13. Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print('Hello World ' + str(1))