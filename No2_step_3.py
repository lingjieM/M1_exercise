# find restriction enzyme site, cut the FASTA apart, count the length of every fragment


import re


site = {"EcoRI": "G AATTC"}
site1 = site["EcoRI"]
site2 = site1.replace(" ", "")

with open("./outfile.fasta.txt", "r") as infile:
    line = infile.read()
    line1 = re.sub(site2,site1,line)
    line2 = re.split(" ", line1)


print(line1)
print(line2)
infile.close()

length = len(line2)


def count():
    result_dict = {}
    i = 0
    while i < length:
        result_dict[str("fragment" + str(i + 1))] = str(len(line2[i]))
        i = i + 1
    print(result_dict)


count()
