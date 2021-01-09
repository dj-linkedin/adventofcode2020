#!/usr/bin/env python3

import util

def part1(data):
    total = 0
    for group in data:
        s = set()
        for person in group.splitlines():
            if person != '':
                for box in person:
                    s.add(box)
        total = total + len(s)
    print(f'part1: {total}')

def part2(data):
    total = 0
    for group in data:
        s = set()
        people_count = 0
        for person in group.splitlines():
            t = set()
            if person != '':
                people_count += 1
                for box in person:
                    t.add(box)
            if not s and people_count == 1:
                s = t
            s = s & t
        total = total + len(s)
    print(f'part2: {total}')

if '__main__' == __name__:
    args = util.parse_args()
    if args.verbosity > 0:
        print('in main')
    with open(args.input, 'r') as f:
        data = f.read().split('\n\n')
    part1(data)
    part2(data)
