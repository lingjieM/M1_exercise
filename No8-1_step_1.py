import os
import glob
import re


all_file = glob.glob("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/*.extendedFrags.fa")
length = len(all_file)
i = 0
outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/integrated.fa", "w")
while i < length:
    with open(all_file[i], "r") as infile:
        context = infile.read()
        filename = str(os.path.basename(all_file[i])).split(".")
        context = re.sub(" ", "", context)
        context = re.sub(">", ">%s" % filename[0], context)
        outfile.write(context)
    i = i + 1
outfile.close()