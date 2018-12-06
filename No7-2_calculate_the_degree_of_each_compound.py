import re
import csv


with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/all_relationship", "r") as infile:
    line = infile.read()
    line = re.sub(" ", "", line)
    line = re.split("\n", line)
    length = len(line)
    name = str()
    compound = []
    i = 0
    while i < length:
        if line[i].startswith("<substrate"):
            name = eval("".join(re.compile(r"name=(.*?)/").findall(line[i])))
            print(name)
            compound.append(name)
            i = i + 1
        elif line[i].startswith("<product"):
            name = eval("".join(re.compile(r"name=(.*?)/").findall(line[i])))
            print(name)
            compound.append(name)
            i = i + 1
        else:
            print("no")
            i = i + 1

with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/compound_list.csv", "w") as csvfile:
    csvWriter = csv.writer(csvfile)
    compound = list(set(compound))
    for n in compound:
            csvWriter.writerow([n])




