# Search restriction enzyme sites and count the length of digested fragments

import csv
import os
import re


# build the dict of restriction enzyme


def enzyme_dict():
    enzyme = {}
    if os.path.exists("/Users/menglingjie/PycharmProjects/M1_exercise/No2/List_of_Restriction_Enzymes.csv"):
        with open("/Users/menglingjie/PycharmProjects/M1_exercise/No2/List_of_Restriction_Enzymes.csv", "r") as infile:
            reader = csv.reader(infile)
            for row in reader:
                enzyme[row[0]] = row[1]
        infile.close()
    else:
        print("Enzyme List file could not be found.")
    return enzyme


# input the path of FASTA, read and revise the file


def input_fasta():
    fastapath = str(input("Please enter the path of fasta file:", ))
    if os.path.exists(fastapath):
        with open(fastapath, "r") as infile:
            outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No2/outfile.fasta.txt", "w")
            line = infile.read()
            line = line[line.find("\n") + 1: line.rfind("\n") - 1]
            line = line.replace("\n", "")
            outfile.write(line)
            outfile.close()
    else:
        print("FASTA file could not be found.")


# find restriction enzyme site, cut the FASTA apart, count the length of every fragment


def input_enzyme(x, y):
    if x in y.keys():
        site = {x: str(y[x])}
        site1 = site[x]
        site2 = site1.replace(" ", "")
        with open("/Users/menglingjie/PycharmProjects/M1_exercise/No2/outfile.fasta.txt", "r") as infile:
            line = infile.read()
            line1 = re.sub(site2, site1, line)
            line2 = re.split(" ", line1)
        infile.close()
        return line2
    else:
        print("Please confirm the enzyme name in the Reference Enzyme List.")
        return "none"


def main():
    endict = enzyme_dict()
    input_fasta()
    ename = str(input("Please enter enzyme name:", ))
    ensearch = input_enzyme(ename, endict)
    if ensearch == "none":
        return
    else:
        length = len(input_enzyme(ename, endict))
        result_dict = {}
        i = 0
        while i < length:
            result_dict[str("fragment" + str(i + 1))] = str(len(ensearch[i]))
            i = i + 1
        print("\nYour FASTA can be digested to " + str(i) + " fragments")
        print("\nLength of each fragment")
        print(result_dict)


main()









