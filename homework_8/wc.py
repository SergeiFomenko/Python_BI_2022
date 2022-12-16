#!/usr/bin/env python
import sys
import os
import argparse

f = Path(os.path.realpath(__file__))
f.chmod(f.stat().st_mode | stat.S_IEXEC)

parser = argparse.ArgumentParser()
parser.add_argument("-w", help="count words in file", 
                    action="store_true")
parser.add_argument("-l", help="count lines in file", 
                    action="store_true")
parser.add_argument("-c", help="count file size in bytes", 
                    action="store_true")
parser.add_argument('files', nargs=argparse.REMAINDER)
parser.add_argument('stdin', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args()


def lwc_count(l, w, c, text, file_name=''):
    result = []
    lwc = False
    if not (l and w and c):
        lwc = True
    if l or lwc:
        result.append(len(data.splitlines()))
    if w or lwc:
        result.append(len(data.split()))
    if file_name == '' and (c or lwc):
        result.append(len(data))
    elif c or lwc:
        result.append(os.path.getsize(file_name))
    if file_name != '':
        result.append(file_name)         
    return result

    
if not sys.stdin.isatty():
    data = args.stdin.read()
    print('\t'.join(
        map(str, lwc_count(args.l, args.w, args.c, data))), 
        file=sys.stdout)   
else:
    for file in args.files:
        try:
            with open(file, 'r') as r:
                data = r.read()
                file_count = lwc_count(args.l, args.w, args.c, data, file_name=file)
                print('\t'.join(map(str, file_count)), file=sys.stdout)
        except FileNotFoundError:
            print(f"sort.py cannot access {file}: No such file or directory")
