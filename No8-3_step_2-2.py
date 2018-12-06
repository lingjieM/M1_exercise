import csv


infile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/OTU_seq_dict", "r")
outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/Frequency.csv", "w")

d = eval(infile.read())
key = list(d.keys())
length = len(key)
i = 0
while i < length:
    print(key[i])
    ltmp = ["OTU%s" % i, key[i], 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j = 1
    while j < 10:
        sub = ">B%s" % j
        count = "".join(d[key[i]]).count(sub)
        ltmp[j + 1] = count
        j = j + 1
    csvWriter.writerow(ltmp)
    i = i + 1
infile.close()
outfile.close()

