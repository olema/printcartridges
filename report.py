#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import time

# Функция создания списка из текстового файла
def data_list(filename):
    '''Формирует и возвращает список списков замен из текстового файла

        Структура вложенного списка:
            0. Код картриджа
            1. Дата замены
            2. Тип принтера
            3. Место установки
    '''
    f = open(filename, 'r')
    l = []
    for line in f:
        l.append([i.strip() for i in line.strip().split(',')])
    f.close()
    return l

# Функция создания словаря в разрезе типов картриджей и кол-ва замен
def make_cartridge_report(data):
    '''Формирует и возвращает словарь с кол-вом замен по типам картриджей

       Структура словаря: ключ - код картриджа; значение - кол-во
    '''
    cart_dict = dict()
    for i in data:
        if i[0] in cart_dict:
            cart_dict[i[0]] += 1
        else:
            cart_dict[i[0]] = 1
    return cart_dict

# Функция формирования словаря в разрезе места установки принтера
def make_place_dict(data):
    '''Формирует словарь в разрезе по местам установки принтера

       Структура словаря: ключ - место установки принтера;
                       значение - список со списками:
                           0. Код картриджа;
                           1. Дата замены ('дд.мм.гггг');
                           2. Тип принтера.
    '''
    place_dict = dict()
    for i in data:
        if i[3] in place_dict:
            place_dict[i[3]].append([i[0], i[1], i[2]])
        else:
            place_dict[i[3]] = [[i[0], i[1], i[2]]]
    return place_dict

# Функция формирования словаря в разрезе типа принтера
def make_printer_dict(data):
    '''Формирует и возвращает словарь в разрезе типов принтеров

       Структура словаря: ключ - тип принтера;
                          значение список со списками:
                              0. Тип картриджа;
                              1. Дата замены;
                              2. Место установки принтера.
    '''
    printer_dict = {}
    for i in data:
        if i[2] in printer_dict:
            printer_dict[i[2]].append([i[0], i[1], i[3]])
        else:
            printer_dict[i[2]] = [[i[0], i[1], i[3]]]
    return printer_dict

# Вывод отчета по картриджам (кол-во замен)
def cart_out(cdict, pathtofolder):
    ''' Функция выводит список картриджей с кол-вом замен

        Выводит отчет в файл cart.report. Структура ф-ла:
            картридж - кол-во замен
    '''
    f = open(pathtofolder + os.sep + 'cart.report', 'w')
    f.write('Report time: {}\n'.format(time.strftime('%a, %d %b %Y %H:%M')))
    f.write('---\n')
    cdict_t = cdict.items()
    for key in sorted(cdict_t, key=lambda key: key[1], reverse=True):
        f.write(' {:<4} = {:>3}\n'.format(key[0], key[1]))
    f.write('---')
    f.close()


def main():
    dirname = os.path.dirname(sys.argv[0])
    filename = 'cartidge_replacement.txt'
    data = data_list(filename)
    cd = make_cartridge_report(data)
#   Отчет список картриджей с количеством замен
    cd_t = cd.items()
    cart_out(cd, dirname)
    for key in sorted(cd_t, key=lambda key: key[1], reverse=True):
        print('{:<4} = {:>3}'.format(key[0], key[1]))
#   Отчет в разрезе мест установки принтера
    pr = make_place_dict(data)
    for key in sorted(pr):
        print('=' * 5)
        print(' -> {}'.format(key))
        d = 1
        for i in pr[key]:
            print('   {:>3}. {}'.format(d, ', '.join(i)))
            d += 1
#   Отчет в разрезе типов принтеров
    d_print = make_printer_dict(data)
    print('\n' + '*' * 60)
    print('*** В разрезе принтеров')
    print(('*' * 60) + '\n')
    for key in sorted(d_print):
        print('=' * 5)
        print(' -> {}'.format(key))
        d = 1
        for i in d_print[key]:
            print('   {:>3}. {}'.format(d, ', '.join(i)))
            d += 1

if __name__ == '__main__':
    main()
