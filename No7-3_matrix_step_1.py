import csv


outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/adjacency_matrix.csv", "w")
csvWrite = csv.writer(outfile)
with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/compound_relationship.csv", "r") as relationship_file:
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/compound_list.csv", "r") as list_file:
        reader = csv.reader(list_file)
        CR = csv.reader(relationship_file)
        CR = list(CR)
        CL = []
        for row in reader:
            CL.append(row[0])
        CL.insert(0, "")
        csvWrite.writerow(CL)
        del CL[0]
        length = len(CL)
        length1 = len(CR)
        n = 0
        d = []
        while n < length:
            d.append(0)
            n = n + 1
        i = 0
        while i < length:
            tmp = list(d)
            tmp.insert(0, CL[i])
            j = 0
            while j < length1:
                if str(CR[j][0]) == CL[i]:
                    m = CL.index(CR[j][1])
                    tmp[m + 1] = 1
                elif str(CR[j][1]) == CL[i]:
                    m = CL.index(CR[j][0])
                    tmp[m + 1] = 1
                j = j + 1
            csvWrite.writerow(tmp)
            del tmp[0]
            i = i + 1
outfile.close()

