import csv
import os, sys
import pandas

with open("./standardgencode.csv", "r") as infile:
    reader = csv.reader(infile)
    aa = [row[0] for row in reader]

with open("./standardgencode.csv", "r") as infile:
    reader = csv.reader(infile)
    code = [row[1] for row in reader]


codedict = {}
def build_dict():
    codedict = {aa[0]: code[0]}
    lenght = len(aa)
    x = 1
    y = 1
    while y < lenght:
        if aa[y] = aa[x]:
            print("y")
            y = y + 1
        else:
            print("n")
            y = y + 1
            x = y




