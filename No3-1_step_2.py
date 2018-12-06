# read genome in ideas, construct the dict and export to a csv file

import re
import csv

infile = open("/bio/db/ideas/genome/genome", "r")
line = infile.read()
line = re.sub(" ", "", line)
line = re.sub("\n", "", line)
line = re.split("///", line)
length = len(line)
i = 0
d = {}
while i < length:
    TN = re.sub("ENTRY", "", str(re.compile(r"ENTRYT\d+").findall(line[i])))
    Name = re.sub("NAME", "", str(re.compile(r"NAME\S*DEFINITION").findall(line[i])))
    Name = re.sub("DEFINITION", "", Name)
    TB = re.sub("Numberofnucleotides:", "", str(re.compile(r"Numberofnucleotides:\d+").findall(line[i])))
    PG = re.sub("Numberofproteingenes:", "", str(re.compile(r"Numberofproteingenes:\d+").findall(line[i])))
    RG = re.sub("NumberofRNAgenes:", "", str(re.compile(r"NumberofRNAgenes:\d+").findall(line[i])))
    Phylum = re.sub("LINEAGE", "", str(re.compile(r"LINEAGE(.*?);").findall(line[i])))
    d[TN[2:-2]] = [Name[2:-2], TB[2:-2], PG[2:-2], RG[2:-2], Phylum[2:-2]]
    i = i + 1

print(d)

with open("/lustre1/aptmp/lingjie/M1_exercise/No3/T_idea_info.txt", "w") as outfile:
    outfile.write(str(d))

with open("/lustre1/aptmp/lingjie/M1_exercise/No3/T_idea_info.csv", "w") as csvfile:
    csvWriter = csv.writer(csvfile)
    for k, v in d.items():
        csvWriter.writerow(["".join(k), "".join(v[0]), "".join(v[1]), "".join(v[2]), "".join(v[3]), "".join(v[4])])


