import csv
import re


csvfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/compound_relationship.csv", "w")
csvWriter = csv.writer(csvfile)
with open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/all_relationship", "r") as R:
    line = R.read()
    line = re.sub(" ", "", line)
    line = re.sub("</reaction>", "</reaction>///", line)
    line = re.split("///", line)
    length1 = len(line)
    i = 0
    while i < length1:
        reaction = line[i]
        reaction = re.split("\n", reaction)
        length2 = len(reaction)
        j = 0
        while j < length2:
            if reaction[j].startswith("<substrate"):
                sub_name = eval("".join(re.compile(r"name=(.*?)/").findall(str(reaction[j]))))
                li = re.compile(r"<product(.*?)/").findall(str(reaction))
                length3 = len(li)
                k = 0
                while k < length3:
                    pro_name = eval("".join(re.compile(r"name=(\S*)").findall(str(li[k]))))
                    csvWriter.writerow([sub_name, pro_name])
                    k = k + 1
            j = j + 1
        i = i + 1
csvfile.close()




