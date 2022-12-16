# Bash functions analogs in Python
## Welcome!
This repository contains analogs of bash functions written in Python.\
List of functions:
1. Ls
2. Rm
3. Sort
4. Tail 
5. Wc
## Installation
Clone this repository to your computer. You can run functions with following command in terminal: ```/full/path/to/function/function_name.py```\
On Linux you can add folder with functions to your PATH variable with following command:\
```export PATH=$PATH:/full/path/to/functions```\
Now you can run functions from terminal by just typing function_name.py
Or you can execute in terminal: ```/full/path/to/function/install.py``` for automatic adding of functions to your PATH variable
## Function list
### 1. LS
Show list of all files and directories at the specified paths. Do not show hidden files by default. You can give several paths to ls.\
Syntaxis: ```ls -a(optional) /path/to/directory/ /another/path/to/another/directory```
optional arguments: -a (show hidden files)\
Example use:\
```./ls.py mnt/c/Users ./```\
Output:\
mnt/c/Users:
1.txt\
discret_math

./:
2.txt

### 2. RM
Delete files at the specified paths. Do not delete folders by default.\
With argument -r delete all files and subfolders at the specified paths recursively.
Example use:\
```./rm.py ./1.txt``` > file 1.txt deleted\
```./rm.py ./``` > ERROR cannot remove ./: Is a directory\
```./rm.py -r ./``` > folder with all files and subfolders deleted

### 3. SORT
Sort file lines in alphanumerical order. Can get input from pipe (i.e. cat 1.txt | ./sort.py)  
If several files provided sort.py will combine them in one output. You can also save output to file (>file.txt)  
Examples
File 1.txt consist of 2 lines (123 and 456)
```./sort.py 1.txt 1.txt``` > 123 123 456 456

### 4. TAIL
Acts like tail from bash. By default shows last 10 lines of file. You can change number of lines with -n argument
### 5. WC
Acts like wc from bash.\
By default count number of lines, words and bytes in file. -w shows only number of words, -c shows only bytes, -l shows only lines\
Works with pipes and you can save output to other files.
