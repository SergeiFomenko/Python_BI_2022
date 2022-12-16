#!/usr/bin/env python
import sys
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("-r", help="remove directory with all containing files recursively", 
                    action="store_true")
parser.add_argument('paths', nargs=argparse.REMAINDER)
args = parser.parse_args()

for path in args.paths:
    if not os.path.isdir(path):
        try:
            os.remove(path)
        except FileNotFoundError:
            print(f'rm: cannot remove {path}: No such file or directory')
    elif args.r:
        try:
            shutil.rmtree(path)
        except FileNotFoundError:
            print(f'rm: cannot remove {path}: No such file or directory')       
    else:
        print(f'rm: cannot remove {path}: Is a directory')