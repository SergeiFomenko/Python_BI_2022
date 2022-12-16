#!/usr/bin/env python
import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('args', nargs=argparse.REMAINDER)
parser.add_argument('stdin', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args().args
data = []


if not sys.stdin.isatty():
    data = parser.parse_args().stdin.read().splitlines()
else:
    for file in args:
        try:
            with open(file, 'r') as r:
                data += r.read().splitlines()
        except FileNotFoundError:
            print(f"sort.py cannot access {file}: No such file or directory")
            
            
for line in sorted(data):
    print(line, file=sys.stdout)