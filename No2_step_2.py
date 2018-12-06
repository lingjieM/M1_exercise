# input the path of fasta, read and revise the file


import os


def input_fasta():
    fastapath = str(input("Please enter the path of fasta file:", ))
    if os.path.exists(fastapath):
        with open(fastapath, "r") as infile:
            outfile = open("outfile.fasta.txt", "w")
            line = infile.read()
            line = line[line.find("\n") + 1: line.rfind("\n") - 1]
            line = line.replace("\n", "")
            outfile.write(line)
            infile.close()
            outfile.close()

    else:
        print("FASTA file could not be found.")


input_fasta()




