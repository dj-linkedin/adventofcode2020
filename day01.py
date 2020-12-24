#!/usr/bin/env python3

import util

def part1(data, verbosity):
    data = [int(x) for x in data]
    for amount in data:
        complement = 2020 - amount
        if complement in data:
            if verbosity > 0:
                print(f'amount {amount} complement {complement}')
            result = amount * complement
    print(f'part1: {result}')

def part2(data, verbosity):
    data = [int(x) for x in data]
    i = 0
    j = 1
    k = 2
    while i < len(data):
        while j < len(data):
            while k < len(data):
                if (data[i] + data[j] + data [k] == 2020):
                    result = data[i] * data[j] * data [k]
                    if verbosity > 0:
                        print(f'{data[i]} {data[j]} {data [k]}')
                k += 1
            j += 1
            k = j + 1
        i += 1
        j = i + 1
        k = j + 1
    print(f'part2: {result}')

if '__main__' == __name__:
    args = util.parse_args()
    if args.verbosity > 0:
        print('in main')
    with open(args.input, 'r') as f:
        data = f.read().splitlines()
    part1(data, args.verbosity)
    part2(data, args.verbosity)
