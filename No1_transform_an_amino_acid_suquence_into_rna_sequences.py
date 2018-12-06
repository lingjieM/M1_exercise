# M1 question No.1
# transform an Amino Acid Sequence into RNA sequences
# read the genetic code table as csv


import csv
import time


# build the dictionary of genetic code


def build_code_dict():
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No1/standardgencode.csv", "r") as infile1:
        reader1 = csv.reader(infile1)
        aa = [row[0] for row in reader1]
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No1/standardgencode.csv", "r") as infile2:
        reader2 = csv.reader(infile2)
        code = [row[1] for row in reader2]
    length = len(aa)
    code_dict = {}
    x = 0
    y = 0
    while y < length:
        if aa[y] == aa[x]:
            code_dict.setdefault(aa[x], []).append(code[y])
            y = y + 1
        else:
            x = y
            code_dict.setdefault(aa[x], []).append(code[y])
            y = y + 1
    print("Dictionary of Genetic Code is ready:")
    for key, value in code_dict.items():
        print("{key}:{value}".format(key=key, value=value))
    return code_dict


# read the Amino acid codes table as csv and build the dictionary of Amino acid codes

def build_abbrev_dict():
    abbrev_dict = {}
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No1/amino_name.csv", "r") as infile:
        reader = csv.reader(infile)
        for row in reader:
            abbrev_dict[row[0]] = row[1]
    return abbrev_dict

# Reverse translate


def re_trans(x, y):
    ps = str.upper(input("\nPlease enter the protein sequence:", ))
    length = len(ps)
    ns = [""]
    i = 0
    start = time.process_time()
    while i < length:
        amino1 = ps[i]
        amino2 = y[amino1]
        if amino2 in x.keys():
            print(amino2)
            next_ns = [m + n for m in ns for n in x[amino2]]
            ns = next_ns
            i = i + 1
        else:
            print("Could not find %s in genetic code dictionary" % amino1)
            break
    end = time.process_time()
    print(end - start, "seconds")
    return ns

# main function


def main():
    x = build_code_dict()
    y = build_abbrev_dict()
    result = re_trans(x, y)
    count = len(result)
    print("\nThere are " + str(count) + " possible RNA sequence patterns:\n")
    for i in result:
        print(i)


main()
