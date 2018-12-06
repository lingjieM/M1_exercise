import csv

outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/calculate_compound.csv", "w")
csvWriter = csv.writer(outfile)
with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/compound_relationship.csv", "r") as relationship_file:
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/compound_list.csv", "r") as list_file:
        reader = csv.reader(list_file)
        CR = csv.reader(relationship_file)
        CR = list(CR)
        CL = []
        for row in reader:
            CL.append(row[0])
        length = len(CL)
        i = 0
        while i < length:
            tmp = []
            length1 = len(CR)
            j = 0
            c = 0
            while j < length1:
                if str(CR[j][0]) == str(CL[i]):
                    tmp.append(str(CR[j][1]))
                elif str(CR[j][1]) == str(CL[i]):
                    tmp.append(str(CR[j][0]))
                j = j + 1
            tmp = list(set(tmp))
            c = len(tmp)
            csvWriter.writerow([CL[i], c])
            i = i + 1
outfile.close()



