import csv
import re


infile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/Frequency.csv", "r")
reader = csv.reader(infile)
d1 = {}
d2 = {}
for line in reader:
    taxa = re.split(";", line[1])
    phylum = taxa[1]
    class_ = taxa[2]
    freq = [float(_s) for _s in line[2:11]]
    if phylum in d1.keys():
        old1 = d1[phylum]
        new1 = [old1[i] + freq[i] for i in range(0, len(old1))]
        d1[phylum] = new1
    else:
        d1[phylum] = freq
    if class_ in d2.keys():
        old2 = d2[class_]
        new2 = [old2[i] + freq[i] for i in range(0, len(old2))]
        d2[class_] = new2
    else:
        d2[class_] = freq
infile.close()

outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/phylum_frequency.csv", "w")
csvWriter = csv.writer(outfile)
key1 = list(d1.keys())
length = len(key1)
i = 0
while i < length:
    ltmp = [str(key1[i])]
    length1 = len(d1[key1[i]])
    j = 0
    while j < length1:
        ltmp.append(d1[key1[i]][j])
        j = j + 1
    csvWriter.writerow(ltmp)
    i = i + 1
outfile.close()

outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/class_frequency.csv", "w")
csvWriter = csv.writer(outfile)
key2 = list(d2.keys())
length3 = len(key2)
i = 0
while i < length3:
    ltmp = [str(key2[i])]
    length2 = len(d2[key2[i]])
    j = 0
    while j < length2:
        ltmp.append(d2[key2[i]][j])
        j = j + 1
    csvWriter.writerow(ltmp)
    i = i + 1
outfile.close()