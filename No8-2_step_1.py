import re


with open("/lustre1/aptmp/lingjie/M1_exercise/No8_cd-hit/SSU_format", "w") as outfile:
    with open("/bio/db/fasta/ribosomaldb/silva_ssu", "r") as infile:
        context = infile.read()
        context = re.sub(" ", "", context)
        outfile.write(context)