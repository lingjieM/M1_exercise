import csv
import os, sys
import pandas

with open("./standardgencode.csv", "r") as infile:
    reader = csv.reader(infile)
    aa = [row[0] for row in reader]

with open("./standardgencode.csv", "r") as infile:
    reader = csv.reader(infile)
    code = [row[1] for row in reader]


lenght = len(aa)


def build_dict():
    codedict = {}
    codedict = {aa[0]: [code[0]]}
    x = 1
    y = 1
    while y < lenght:
        if aa[y] == aa[x]:
            codedict.setdefault(aa[x], []).append(code[y])
            y = y + 1
        else:
            x = y
            codedict.setdefault(aa[x], []).append(code[y])
            y = y + 1
    return codedict

codedict = build_dict()
print(codedict)


