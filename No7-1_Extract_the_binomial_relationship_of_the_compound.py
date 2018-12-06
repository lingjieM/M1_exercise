import glob
import re


outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No7/all_relationship", "w")
allfile = glob.glob("/Users/menglingjie/PycharmProjects/M1_exercise/No7/eco/*.xml")
num_path = len(allfile)
i = 0
while i < num_path:
    with open(allfile[i], "r") as infile:
        line = infile.read()
        if "<reaction" in "".join(line):
            line = re.sub("<entry", "///<entry", line)
            line = re.sub("</entry>", "</entry>///", line)
            line = re.sub("<reaction", "///<reaction", line)
            line = re.sub("</reaction>", "</reaction>///", line)
            reaction = re.split("///", line)
            num_re = len(reaction)
            j = 0
            while j < num_re:
                if "substrate" and "product" in "".join(reaction[j]):
                    print(reaction[j], file=outfile)
                j = j + 1
    i = i + 1
outfile.close()



