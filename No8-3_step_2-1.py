import re
import csv


cluster = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/OTUs.out.clstr", "r")
line = cluster.read()
line = re.split(">Cluster", line)
lenClu = len(line)
infile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/No8_cd-hit/annotation_dict", "r")
d = eval(infile.read())
d1 = {}
key = list(d.keys())
ltmp = []
length = len(key)
i = 0
while i < length:
    length1 = len(d[key[i]])
    j = 0
    while j < length1:
        m = 0
        while m < lenClu:
            if d[key[i]][j] in line[m]:
                seq = re.compile(r">B\S*").findall(str(line[m]))
                for items in seq:
                    print(items)
                    ltmp.append(items)
            m = m + 1
        j = j + 1
    d1[key[i]] = ltmp
    i = i + 1
    ltmp = []
cluster.close()
infile.close()

outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/OTU_seq_dict", "w")
outfile.write(str(d1))
outfile.close()
