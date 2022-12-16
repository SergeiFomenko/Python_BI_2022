#!/usr/bin/env python
import sys
import os
import argparse
from collections import deque
from pathlib import Path
import stat

f = Path(os.path.realpath(__file__))
f.chmod(f.stat().st_mode | stat.S_IEXEC)

def tail(filename, n):
    with open(filename) as f:
        return deque(f, n)

    
def print_stdout(data):
    for line in data:
        print(line, file=sys.stdout, end='')
   

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="number of lines at the end of file to show", default=10)
parser.add_argument('files', nargs=argparse.REMAINDER)
parser.add_argument('stdin', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args()

if not sys.stdin.isatty():
    data = args.stdin.readlines()[-1*int(args.n):]
    print_stdout(data)
else:
    for file in args.files:
        if len(args.files) > 1:
            print(f'==>{file}<==', file=sys.stdout)
        try:
            data = tail(file, int(args.n))
            print_stdout(data)
        except FileNotFoundError:
            print(f"tail.py cannot access {file}: No such file or directory")
