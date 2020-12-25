#!/usr/bin/env python3

import util

def is_valid_v1(mn, mx, char, passwd):
    times = passwd.count(char)
    return mn <= times and times <= mx

def is_valid_v2(p1, p2, char, passwd):
    satisfied = 0
    if passwd[p1 - 1] == char:
        satisfied += 1
    if passwd[p2 - 1] == char:
        satisfied += 1
    return satisfied == 1

def part1(data, verbosity):
    valid = 0
    for line in data:
        assert ':' in line
        count, char, passwd = line.split(' ')
        mn, mx = count.split('-')
        char = char[0]
        if is_valid_v1(int(mn), int(mx), char, passwd):
            valid += 1
    print(f'part1: {valid}')

def part2(data, verbosity):
    valid = 0
    for line in data:
        assert ':' in line
        count, char, passwd = line.split(' ')
        p1, p2 = count.split('-')
        char = char[0]
        if is_valid_v2(int(p1), int(p2), char, passwd):
            valid += 1
    print(f'part2: {valid}')

if '__main__' == __name__:
    args = util.parse_args()
    if args.verbosity > 0:
        print('in main')
    with open(args.input, 'r') as f:
        data = f.read().splitlines()
    part1(data, args.verbosity)
    part2(data, args.verbosity)
