import os
import glob
import csv
import re


outfile = open("/lustre1/aptmp/lingjie/M1_exercise/No3/DB_info.csv", "w")
csvWrite = csv.writer(outfile)
DB_list = ["refseq", "pdb", "swissprot", "trembl", "pfam", "ncbi-cdd", "pathway", "module", "ko", "compound", "enzyme", "reaction", "drug", "disease"]
length = len(DB_list)
i = 1
while i < length:
    print(DB_list[i])
    os.chdir("/bio/db/ideas/%s" % str(DB_list[i]))
    os.system("pwd")
    all_file = glob.glob("./*.tit")
    length1 = len(all_file)
    j = 0
    while j < length1:
        filename = str(os.path.basename(all_file[j])).split(".")
        print(filename[0])
        number = os.popen("wc -l ./%s" % all_file[j]).readlines()
        number = re.compile(r"\d+").match("".join(number))
        number = number.group()
        print(number)
        csvWrite.writerow([DB_list[i], filename[0], number])
        j = j + 1
    i = i + 1
outfile.close()
