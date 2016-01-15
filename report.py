#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def data_list(filename):
    f = open(filename, 'r')
    l = []
    for line in f:
        temp_l = line.strip().split(',')
        l.append([ i.strip() for i in temp_l])
    f.close()
    return l

def make_cartridge_report(data_list):
    cart_dict = dict()
    for i in data_list:
        if i[0] in cart_dict:
            cart_dict[i[0]] += 1
        else:
            cart_dict[i[0]] = 1
    return cart_dict

def main():
    filename = 'cartidge_replacement.txt'
    data = data_list(filename)
    cd = make_cartridge_report(data)
    print(cd)

if __name__ == '__main__':
    main()
