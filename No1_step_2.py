import csv
import os, sys
import pandas

codedict = {'Phe': ['UUU', 'UUC'], 'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'Ile': ['AUU', 'AUC', 'AUA'], 'Met': ['AUG'], 'Val': ['GUU', 'GUC', 'GUA', 'GUG'], 'Ser': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'Pro': ['CCU', 'CCC', 'CCA', 'CCG'], 'Thr': ['ACU', 'ACC', 'ACA', 'ACG'], 'Ala': ['GCU', 'GCC', 'GCA', 'GCG'], 'Tyr': ['UAU', 'UAC'], 'Stop': ['UAA', 'UAG', 'UGA'], 'His': ['CAU', 'CAC'], 'Gln': ['CAA', 'CAG'], 'Asn': ['AAU', 'AAC'], 'Lys': ['AAA', 'AAG'], 'Asp': ['GAU', 'GAC'], 'Glu': ['GAA', 'GAG'], 'Cys': ['UGU', 'UGC'], 'Trp': ['UGG'], 'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Gly': ['GGU', 'GGC', 'GGA', 'GGG']}
namedict = {}
with open("./amino_name.csv", "r") as infile:
    reader = csv.reader(infile)
    for row in reader:
        namedict[row[0]] = row[1]


def re_treans():
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

def main():
    ns = re_treans()
    print(ns)

main()



