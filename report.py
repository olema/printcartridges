#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def data_list(filename):
    f = open(filename, 'r')
    l = []
    for line in f:
        l.append([i.strip() for i in line.strip().split(',')])
    f.close()
    return l


def make_cartridge_report(data):
    cart_dict = dict()
    for i in data:
        if i[0] in cart_dict:
            cart_dict[i[0]] += 1
        else:
            cart_dict[i[0]] = 1
    return cart_dict

def make_place_dict(data):
    place_dict = dict()
    for i in data:
        if i[3] in place_dict:
            place_dict[i[3]].append([i[0], i[1], i[2]])
        else:
            place_dict[i[3]] = [[i[0], i[1], i[2]]]
    return place_dict

def make_printer_dict(data):
    printer_dict = {}
    for i in data:
        if i[2] in printer_dict:
            printer_dict[i[2]].append([i[0], i[1], i[3]])
        else:
            printer_dict[i[2]] = [[i[0], i[1], i[3]]]
    return printer_dict

def main():
    filename = 'cartidge_replacement.txt'
    data = data_list(filename)
    cd = make_cartridge_report(data)
    cd_t = cd.items()
    for key in sorted(cd_t, key=lambda key: key[1], reverse=True):
        print('{:<4} = {:>3}'.format(key[0], key[1]))
#    f = open('place.report', 'w')
#    Отчет в разрезе мест установки принтера
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
    print('\n***')
    print('*** В разрезе принтеров')
    print('***')
    for key in sorted(d_print):
        print('=' * 5)
        print(' -> {}'.format(key))
        d = 1
        for i in d_print[key]:
            print('   {:>3}. {}'.format(d, ', '.join(i)))
            d += 1

if __name__ == '__main__':
    main()
