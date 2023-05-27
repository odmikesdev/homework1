# Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел. Результат вычислений вывести на экран.

oneNumber = int(input('Please enter a First number: '))
twoNumber = int(input('Please enter a Second number: '))
threeNumber = int(input('Please enter a Third number: '))

multiplicationNumber = oneNumber * twoNumber * threeNumber
sumNumber = oneNumber + twoNumber + threeNumber

print(f'Sum of numbers: {sumNumber} \nMultiplication of numbers: {multiplicationNumber}')