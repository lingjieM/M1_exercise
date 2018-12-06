import re


with open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/No8_cd-hit/integrate.clstr", "r") as infile:
    context = infile.read()
    context = re.split(">Cluster", context)
    length = len(context)
    d = {}
    i = 0
    while i < length:
        if ">B" in context[i]:
            annotation = "".join(re.compile(r">silva\S*").findall(str(context[i])))
            seq = re.compile(r">B\S*").findall(str(context[i]))
            d[annotation] = seq
        i = i + 1
    print(d)

outfile = open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/No8_cd-hit/annotation_dict", "w")
outfile.write(str(d))
outfile.close()
