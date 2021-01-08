#!/usr/bin/env python3

import util

def get_row(datum):
    chunk = 64
    mn = 0
    mx = 127
    for d in datum:
        if (d == 'F'):
            mx = mx - chunk
            chunk /= 2
            continue
        if (d == 'B'):
            mn = mn + chunk
            chunk /= 2
            continue
        break
    assert mn == mx
    return int(mn)

def get_col(datum):
    chunk = 4
    mn = 0
    mx = 7
    for d in datum:
        if (d == 'L'):
            mx = mx - chunk
            chunk /= 2
            continue
        if (d == 'R'):
            mn = mn + chunk
            chunk /= 2
            continue
    assert mn == mx
    return int(mn)

def get_seatid(row, col):
    return (row * 8) + col

def part1(data):
    total = 0
    mn = None
    mx = None
    for datum in data:
        if (len(datum) > 0):
            row = get_row(datum)
            col = get_col(datum)
            s = get_seatid(row, col)
            if mn is None:
                mn = s
            if mx is None:
                mx = s
            if mn > s:
                mn = s
            if mx < s:
                mx = s
            total = total + s
    print(f'part1: {mx}')

def part2(data):
    total = 0
    mn = None
    mx = None
    for datum in data:
        if (len(datum) > 0):
            row = get_row(datum)
            col = get_col(datum)
            s = get_seatid(row, col)
            if mn is None:
                mn = s
            if mx is None:
                mx = s
            if mn > s:
                mn = s
            if mx < s:
                mx = s
            total = total + s
    i = mn
    newtotal = 0
    while (i <= mx):
        newtotal = newtotal + i
        i += 1
    print(f'part2: {newtotal-total}')

if '__main__' == __name__:
    args = util.parse_args()
    if args.verbosity > 0:
        print('in main')
    with open(args.input, 'r') as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)
