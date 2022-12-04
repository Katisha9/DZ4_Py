 # B. Даны два файла, в каждом из которых находится запись многочлена.
 # Задача - сформировать файл, содержащий сумму многочленов.

import random
size1 = int(input('Введите натуральную степень первого многочлена k: '))
size2 = int(input('Введите натуральную степень второго многочлена k: '))


def create_eq(size):
    koef = {}
    for i in range(size+1):
        koef[i] = random.randint(0,100)
    print(koef)

    equation = ''
    for i in range(size, -1, -1):
        if koef[i] != 0:
            if koef[i] == 1:
                if i == 1:
                    equation += f'x + '
                elif i == 0:
                    equation += f'1 '
                else:
                    equation += f'x**{i} + '
            else:
                if i == 1:
                    equation += f'{koef[i]}*x + '
                elif i == 0:
                    equation += f'{koef[i]} '
                else:
                    equation += f'{koef[i]}*x**{i} + '
    print(equation + ' = 0')
    return equation + ' = 0'

# print(create_eq(size1))
# print(create_eq(size2))

data1 = open('file1.txt', 'w')
data1.writelines(create_eq(size1))
data1.close()
data2 = open('file2.txt', 'w')
data2.writelines(create_eq(size2))
data2.close()



path1 = 'file1.txt'
data1 = open(path1, 'r')
for line in data1:
    equation1 = line
    print(equation1)
data1.close()
path2 = 'file2.txt'
data2 = open(path2, 'r')
for line in data2:
    equation2 = line
    print(equation2)
data2.close()

def read_equation(equation)
equation = equation.replace(' ', '')
equation = equation[:-2].split('+')
new_equation = []
for i in range(size + 1):
        koef[i] = random.randint(0, 100)
    print(koef)

