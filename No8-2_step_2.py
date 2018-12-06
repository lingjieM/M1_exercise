import re
import csv


outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/No8_cd-hit/annotation.csv", "w")
with open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/No8_cd-hit/integrate.clstr", "r") as infile:
    csvWriter = csv.writer(outfile)
    context = infile.read()
    context = re.split(">Cluster", context)
    length = len(context)
    i = 0
    while i < length:
        if ">B" in context[i]:
            annotation = "".join(re.compile(r">silva\S*").findall(str(context[i])))
            print(annotation)
            seq = re.compile(r">B\S*").findall(str(context[i]))
            length1 = len(seq)
            j = 0
            while j < length1:
                csvWriter.writerow([seq[j], annotation])
                j = j + 1
        i = i + 1
outfile.close()