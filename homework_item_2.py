# Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей.

d1 = int(input('Specify the size of the diagonal 1:'))
d2 = int(input('Specify the size of the diagonal 2:'))

square = (d1 * d2)/2

print(f'Rhombus area = {square}')

