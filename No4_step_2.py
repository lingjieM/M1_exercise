import csv
import re


with open("/Users/menglingjie/PycharmProjects/M1_exercise/No4/EC_dict.txt", "r") as infile:
    d = eval(infile.read())
    keylist = []
    keylist1 = []
    for k in d.keys():
        keylist.append(k)
    print(keylist)
    length = len(keylist)
    i = 0
    while i < length:
        keylist[i] = str(keylist[i]).replace("-", "-1")
        key = keylist[i].split(".")
        keylist1.append(key)
        i = i + 1
    keylist2 = sorted(keylist1, key=lambda x: (int(x[0]), int(x[1]), int(x[2]), int(x[3])))
    length1 = len(keylist2)
    j = 0
    keylist3 = []
    while j < length1:
        a = keylist2[j][0] + "." + keylist2[j][1] + "." + keylist2[j][2] + "." + keylist2[j][3]
        keylist3.append(a)
        j = j + 1
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No4/EC_dict_sorted.csv", "w") as csvfile:
        csvWriter = csv.writer(csvfile)
        length2 = len(keylist3)
        m = 0
        while m < length2:
            keylist3[m] = str(keylist3[m]).replace("-1", "-")
            length3 = len(d[keylist3[m]])
            n = 0
            tmp = [keylist3[m]]
            while n < length3:
                tmp.append(d[keylist3[m]][n])
                n = n + 1
            csvWriter.writerow(tmp)
            m = m + 1




