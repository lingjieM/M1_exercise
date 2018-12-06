import csv


infile1 = open("/Users/menglingjie/PycharmProjects/M1_exercise/No3/T_fasta_info.txt", "r")
infile2 = open("/Users/menglingjie/PycharmProjects/M1_exercise/No3/T_idea_info.txt", "r")

dict1 = eval(infile1.read())
dict2 = eval(infile2.read())
dict1list = []
dict2list = []

for k in dict1.keys():
    dict1list.append(k)

for k in dict2.keys():
    dict2list.append(k)

dictlist = list(set(dict1list).intersection(set(dict2list)))
length = len(dictlist)
i = 0
with open("/Users/menglingjie/PycharmProjects/M1_exercise/No3/No3-1_with_phylum.csv", "w") as csvfile:
    while i < length:
        print(dictlist[i])
        csvWriter = csv.writer(csvfile)
        if dict2[dictlist[i]][1] != "":
            if dict1[dictlist[i]][0] == dict2[dictlist[i]][1]:
                size = "1"
            else:
                size = "0"
        if dict2[dictlist[i]][2] == "":
            dict2[dictlist[i]][2] = "0"
        if dict2[dictlist[i]][3] == "":
            dict2[dictlist[i]][3] = "0"
        if int(dict1[dictlist[i]][1]) == int(dict2[dictlist[i]][2]):
            genes = "1"
        else:
            genes = "0"
        csvWriter.writerow([dictlist[i], dict1[dictlist[i]][0], dict2[dictlist[i]][1], dict1[dictlist[i]][1], dict2[dictlist[i]][2], size, genes, dict2[dictlist[i]][4]])
        i = i + 1


print(dictlist)
print(len(dictlist))


infile1.close()
infile2.close()

