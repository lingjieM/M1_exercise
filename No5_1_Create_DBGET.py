import os
import re

os.system("module load dbget")
with open("/lustre1/aptmp/lingjie/M1_exercise/No5_database/ribosome_gene_keywords", "r") as infile:
    line = infile.read()
    line = re.split("\n", line)
    length = len(line)
    i = 0
    while i < length:
        linei = re.split(" ", line[i])
        ENTRY = "".join(linei[0])
        os.system("bget genes %s" % ENTRY)
        i = i + 1
