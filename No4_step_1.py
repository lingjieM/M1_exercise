import re
import csv


infile = open("/bio/db/ideas/ko/ko", "r")
line = infile.read()
line = re.split("///", line)
length = len(line)
i = 0
d = {}
while i < length:
    KO = re.sub(" ", "", "".join(re.compile(r"ENTRY(.*?)\n").findall(line[i])))
    KO = re.compile(r"K\d+").findall(KO)
    KO = "".join(KO)
    DEF = "".join(re.compile(r"DEFINITION(.*?)\n").findall(line[i]))
    if "EC:" in DEF:
        EC = re.compile(r"EC:(.*?)]").findall(DEF)
        EC = "".join(EC)
        EC = re.sub("]", "", EC)
        EC = "".join(EC)
        EC = re.split(" ", EC)
        length1 = len(EC)
        j = 0
        while j < length1:
            if EC[j] not in d.keys():
                d[EC[j]] = [KO]
            else:
                d[EC[j]].append(KO)
            j = j + 1
    else:
        print("NULL")
    i = i + 1

print(d)
with open("/aptmp/lingjie/M1_exercise/No4/EC_dict.txt", "w") as outfile:
    outfile.write(str(d))

with open("/aptmp/lingjie/M1_exercise/No4/EC_dict.csv", "w") as outfile:
    csvWriter = csv.writer(outfile)
    for k, v in d.items():
        tmp = [k]
        length2 = len(v)
        m = 0
        while m < length2:
            tmp.append(v[m])
            m = m + 1
        csvWriter.writerow(tmp)
