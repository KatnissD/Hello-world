#!/usr/bin/python
#coding:utf-8
import os


print(os.getcwd())              # get current path
print(os.listdir('.'))          # get all files of current path (list)
print(os.listdir(os.getcwd()))  # quality (list)

items = os.listdir(os.getcwd())     # one by one
for item in items:
    if os.path.isfile(item):
        print(item)

syst = platform.system()            # transform path
        if syst == "Windows":
            os.chdir('.\\')
            the_path = '.\\a\\b\\'
        elif syst == "Linux":
            os.chdir('./')
            the_path = './a/b/'

if os.path.exists('{}{}'.format(the_path, "hello.txt")):
    c = open('{}{}'.format(the_path, "hello.txt"), 'r')



