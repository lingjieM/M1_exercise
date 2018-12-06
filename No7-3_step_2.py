import csv

outcsv = open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/test.csv", "w")
outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/test", "w")
csvWriter = csv.writer(outcsv)
with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/compound_relationship.csv", "r") as relationship_file:
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/compound_list.csv", "r") as list_file:
        reader = csv.reader(list_file)
        CR = csv.reader(relationship_file)
        CR = list(CR)
        CL = []
        tmp = []
        CC = []
        CLU = []
        for row in reader:
            CL.append(row[0])
        length = len(CL)
        i = 0
        m = 0
        while i < length:
            if str(CL[i]) not in CLU:
                tmp.append(str(CL[i]))
                CC.append(str(CL[i]))
                CLU.append(str(CL[i]))
                while len(tmp) != 0:
                    print("tmp", tmp)
                    length1 = len(CR)
                    j = 0
                    while j < length1:
                        if str(CR[j][0]) == str(tmp[0]):
                            if str(CR[j][1]) not in CLU:
                                tmp.append(str(CR[j][1]))
                                CC.append(str(CR[j][1]))
                                CC = list(set(CC))
                                CLU.append(str(CR[j][1]))
                        elif str(CR[j][1]) == str(tmp[0]):
                            if str(CR[j][0]) not in CLU:
                                tmp.append(str(CR[j][0]))
                                CC.append(str(CR[j][0]))
                                CC = list(set(CC))
                                CLU.append(str(CR[j][0]))
                                CLU = list(set(CLU))
                        j = j + 1
                    del tmp[0]
                else:
                    m = m + 1
                    print("connected component%s" % m, CC, file=outfile)
                    csvWriter.writerow(["connected component%s" % m, len(CC)])
                    print("CLU", CLU)
                    CC = []
                i = i + 1
            else:
                print("used", CL[i])
                i = i + 1
outfile.close()
outcsv.close()




