#Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр.
#Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24.


number = int(input('Please enter a four-digit number:'))

oneNumber = number // 1000
twoNumber = number % 1000 // 100
threeNumber = number % 100 // 10
fourNumber = number % 10

multiplication = oneNumber * twoNumber * threeNumber * fourNumber
print(f'Multiplication = {multiplication}')


