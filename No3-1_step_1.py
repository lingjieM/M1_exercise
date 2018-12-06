import glob
import os
import csv
import re


all_file1 = glob.glob("/bio/db/fasta/genome/*.genome")
length1 = len(all_file1)
T_dict = {}
filename = []
i = 0
while i < length1:
    with open(all_file1[i], "r") as infile:
        fasta = []
        for line in infile:
            if not line.startswith(">"):
                fasta.append(line.replace("\n", ""))
        total_bases = len("".join(fasta))
        filename1 = str(os.path.basename(all_file1[i])).split(".")
        T_dict[str(filename1[0])] = [str(total_bases)]
        filename.append(str(filename1[0]))
        print(filename1[0])
    i = i + 1
print(filename)


all_file2 = glob.glob("/bio/db/fasta/genes/*.pep")
length2 = len(all_file2)
j = 0
while j < length2:
    with open(all_file2[j], "r") as infile:
        context = infile.read()
        line = re.split("\n", context)
        length = len(line)
        m = 0
        num_sum = 0
        while m < length:
            if line[m].startswith(">"):
                num_sum = num_sum + 1
            m = m + 1
        filename2 = str(os.path.basename(all_file2[j])).split(".")
        if str(filename2[0]) in filename:
            T_dict[str(filename2[0])].append(str(num_sum))
            print(filename2[0])
        else:
            print("skip")
    j = j + 1


with open("/lustre1/aptmp/lingjie/M1_exercise/No3/T_fasta_info.txt", "w") as outfile:
    outfile.write(str(T_dict))

with open("/lustre1/aptmp/lingjie/M1_exercise/No3/T_fasta_info.csv", "w") as csvfile:
    csvWriter = csv.writer(csvfile)
    for k, v in T_dict.items():
        csvWriter.writerow(["".join(k), "".join(v[0]), "".join(v[1])])





