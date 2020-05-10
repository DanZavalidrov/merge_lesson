"""
1. Ключевые слова, встроенные функции (для ознакомления, знать,
как не стоит называть переменные)
"""
print ('\033[1m' + 'Hello world!')
print ('\n')
"""
complex([real[, imag]]) 
dict([object]) 
float([X]) 
frozenset([последовательность]) 
int([object], [основание системы счисления]) 
list([object]) 
memoryview([object]) 
object() 
range([start=0], stop, [step=1]) 
и так далее.
"""



#2. Числа
print(pow(3, 2, 2))
print(6+6,'  ',  5/5,'  ',  6%5,'  ', 5**2)
print(divmod(9,2))
print ('\n')

#3. Строки

print('My name is {}'.format('Dan'))
print('Age %i' % 18)
print ('\n')

#4. Списки (массивы)
a = ['a' , 'c' , 'd']
print(list(a))
a.remove('d')
print(list(a))
print ('\n')

#5. Индексы и срезы
c = [1, 2 , 10 , 'b']
print(c[3])
print(c[::2])