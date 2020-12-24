#!/usr/bin/env python3

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='file containing input')
    parser.add_argument('-v', '--verbosity', action='count', default=0,
                        help='increase output verbosity')
    args = parser.parse_args()
    return args

if '__main__' == __name__:
    print('this is util')
    args = parse_args()
    print(args)
