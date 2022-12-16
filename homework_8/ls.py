#!/usr/bin/env python
import sys
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-a", help="display hidden files", 
                    action="store_true")
parser.add_argument('paths', nargs=argparse.REMAINDER)
args = parser.parse_args()
mult_paths = len(args.paths) > 1
if args.paths == []:
    dirs = os.listdir(os.getcwd())
    for dir in dirs:
        if not dir.startswith('.') or args.a:
            print(dir, file=sys.stdout)
else:    
    for path in args.paths:
        if mult_paths:
            print(f'{path}:')
        try:
            for dir in os.listdir(path):
                if not dir.startswith('.') or args.a:
                    print(dir, file=sys.stdout)
        except FileNotFoundError:
                print(f'ls.py cannot access {path}: No such file or directory', file=sys.stderr)
        if mult_paths:
            print('\n')
        