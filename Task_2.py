# Задача B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random


def create_coeff(k):
    list_coeff = [random.randint(0, 100) for i in range(k + 1)]
    return list_coeff


def create_str_eq(line_eq):
    list_coeff = line_eq[::-1]
    equantion = ''
    if len(list_coeff) < 1:
        equantion = 'x = 0'
    else:
        for i in range(len(list_coeff)):
            if i != len(list_coeff) - 1 and list_coeff[i] != 0 and i != len(list_coeff) - 2:
                equantion += f'{list_coeff[i]}x^{len(list_coeff) - i - 1}'
                if list_coeff[i + 1] != 0 or list_coeff[i + 2] != 0:
                    equantion += ' + '
            elif i == len(list_coeff) - 2 and list_coeff[i] != 0:
                equantion += f'{list_coeff[i]}x'
                if list_coeff[i + 1] != 0 or list_coeff[i + 2] != 0:
                    equantion += ' + '
            elif i == len(list_coeff) - 1 and list_coeff[i] != 0:
                equantion += f'{list_coeff[i]} = 0'
            elif i == len(list_coeff) - 1 and list_coeff[i] == 0:
                equantion += ' = 0'
    return equantion


def select_pow(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def get_coeff(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def decon_equation(equantion):
    equantion = equantion[0].replace(' ', '').split('=')
    equantion = equantion[0].split('+')
    list_eq = []
    l = len(equantion)
    k = 0
    if select_pow(equantion[-1]) == -1:
        list_eq.append(int(equantion[-1]))
        l -= 1
        k = 1
    i = 1
    ii = l - 1
    while ii >= 0:
        if select_pow(equantion[ii]) != -1 and select_pow(equantion[ii]) == i:
            list_eq.append(get_coeff(equantion[ii]))
            ii -= 1
            i += 1
        else:
            list_eq.append(0)
            i += 1
    return list_eq


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

k1 = int(input("Введите натуральную степень первого многочлена k: "))
k2 = int(input("Введите натуральную степень второго многочлена k: "))
koef1 = create_coeff(k1)
koef2 = create_coeff(k2)
write_file("file1.txt", create_str_eq(koef1))
write_file("file2.txt", create_str_eq(koef2))

with open('file1.txt', 'r') as data:
    st1 = data.readlines()
with open('file2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = decon_equation(st1)
lst2 = decon_equation(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file("file_summ.txt", create_str_eq(lst_new))
with open('file_summ.txt', 'r') as data:
    st3 = data.readlines()
print(f"Сумма многочленов:  {st3}")