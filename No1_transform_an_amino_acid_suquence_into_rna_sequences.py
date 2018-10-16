# M1 question No.1
#transform an Amino Acid Sequence into RNA sequences

#read the genetic code table as csv
import csv
import os, sys
import pandas

with open("./standardgencode.csv", "r") as infile:
    reader = csv.reader(infile)
    aa = [row[0] for row in reader]

with open("./standardgencode.csv", "r") as infile:
    reader = csv.reader(infile)
    code = [row[1] for row in reader]

#build the dictionary of genetic code


def build_dict():
    lenght = len(aa)
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

#read the Amino acid codes table as csv and build the dictionary of Amino acid codes
namedict = {}
with open("./amino_name.csv", "r") as infile:
    reader = csv.reader(infile)
    for row in reader:
        namedict[row[0]] = row[1]

#Reverse translate


def re_treans():
    codedict = build_dict()
    ps = str(input("please enter the protein sequence(upper-case letter):", ))
    length = len(ps)
    ns = [""]
    i = 0
    while i < length:
        amino1 = ps[i]
        amino2 = namedict[amino1]
        next_ns = [m + n for m in ns for n in codedict[amino2]]
        ns = next_ns
        i = i + 1
    return ns

#main function


def main():
    ns = re_treans()
    print(ns)

main()
