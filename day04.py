#!/usr/bin/env python3

import util
import re

input='''
'''

def part1(passports):
    valid = 0
    for passport in passports:
        req = 0
        fields = passport.split()
        for field in fields:
            if ('byr:' in field):
                req += 1
            if ('iyr:' in field):
                req += 1
            if ('eyr:' in field):
                req += 1
            if ('hgt:' in field):
                req += 1
            if ('hcl:' in field):
                req += 1
            if ('ecl:' in field):
                req += 1
            if ('pid:' in field):
                req += 1
        # cid: optional
        if (req == 7):
            valid += 1
    print(f'part1: {valid}')

def part2(passports):
    valid = 0
    for passport in passports:
        req = 0
        fields = passport.split()
        for field in fields:
            if ('byr:' in field):
                (_, y) = field.split(':')
                if (y.isdigit() and int(y) >= 1920 and int(y) <= 2002):
                    req += 1
            if ('iyr:' in field):
                (_, y) = field.split(':')
                if (y.isdigit() and int(y) >= 2010 and int(y) <= 2020):
                    req += 1
            if ('eyr:' in field):
                (_, y) = field.split(':')
                if (y.isdigit() and int(y) >= 2020 and int(y) <= 2030):
                    req += 1
            if ('hgt:' in field):
                (_,h) = field.split(':')
                if (
                        (h.endswith('cm') and h[:-2].isdigit() and
                         (int(h[:-2]) >= 150) and (int(h[:-2]) <= 193)) or
                        (h.endswith('in') and h[:-2].isdigit() and
                         (int(h[:-2]) >=  59) and (int(h[:-2]) <=  76))
                ):
                    req += 1
            if ('hcl:' in field):
                (_,h) = field.split(':')
                if (re.search("^#[0-9a-f]{6}$", h)):
                    req += 1
            if ('ecl:' in field):
                (_,e) = field.split(':')
                if (
                        e == 'amb' or
                        e == 'blu' or
                        e == 'brn' or
                        e == 'gry' or
                        e == 'grn' or
                        e == 'hzl' or
                        e == 'oth'
                ):
                    req += 1
            if ('pid:' in field):
                (_,i) = field.split(':')
                if (re.search("^[0-9]{9}$", i)):
                    req += 1
        if req == 7:
            valid += 1
    print(f'part2: {valid}')

if '__main__' == __name__:
    args = util.parse_args()
    if args.verbosity > 0:
        print('in main')
    with open(args.input, 'r') as f:
        passports = f.read().split('\n\n')
    num_passports = len(passports)
    if args.verbosity > 0:
        print('number of passports:{}'.format(num_passports))
    part1(passports)
    part2(passports)
