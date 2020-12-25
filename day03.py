#!/usr/bin/env python3

import util

def collision(lines, row, col):
    if lines[row][col] == '#':
        return True
    else:
        assert lines[row][col] == '.'
        return False

def count_a_slope(lines, num_rows, num_cols, right, down):
    row = 0
    col = 0
    trees = 0
    while row < num_rows:
        if collision(lines, row, col):
            trees += 1
        row += down
        col += right
        col = col % num_cols
    return trees

def part1(lines, num_rows, num_cols):
    trees = count_a_slope(lines, num_rows, num_cols, 3, 1)
    print(f'part1: {trees}')

def part2(lines, num_rows, num_cols):
    trees = (
        count_a_slope(lines, num_rows, num_cols, 1, 1) *
        count_a_slope(lines, num_rows, num_cols, 3, 1) *
        count_a_slope(lines, num_rows, num_cols, 5, 1) *
        count_a_slope(lines, num_rows, num_cols, 7, 1) *
        count_a_slope(lines, num_rows, num_cols, 1, 2)
    )
    print(f'part2: {trees}')

if '__main__' == __name__:
    args = util.parse_args()
    if args.verbosity > 0:
        print('in main')
    with open(args.input, 'r') as f:
        lines = f.read().splitlines()
    num_rows = len(lines)
    if args.verbosity > 0:
        print('rows:{}'.format(num_rows))
    num_cols = len(lines[0])
    if args.verbosity > 0:
        print('cols:{}'.format(num_cols))
    for line in lines:
        assert len(line) == num_cols
    part1(lines, num_rows, num_cols)
    part2(lines, num_rows, num_cols)
