#6. Кортежи
f = ('s',);
print(f)
print ('\n')
h = tuple('Hello, Ciao')
print(h)
print('\n')

#7. Множества
a = (set('Hello my friend'))
print (a)

words = ['Hello', 'Hello', 'Nice']
print(set(words))
print ('\n')

#8. Байтовые строки
print('привет как дела'.encode('utf-8'))
print (b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82 \xd0\xba\xd0\xb0\xd0\xba \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0'.decode('utf-8'))
b = bytearray(b'hello!')
print(b[3])