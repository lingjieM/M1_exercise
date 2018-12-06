# build the dict of restriction enzyme


import csv
import os


def enzyme_dict():
    enzyme = {}
    if os.path.exists("./List_of_Restriction_Enzymes.csv"):
        with open("./List_of_Restriction_Enzymes.csv", "r") as infile:
            reader = csv.reader(infile)
            for row in reader:
                enzyme[row[0]] = row[1]
        print(enzyme)
        infile.close()
    else:
        print("Enzyme list could not be found.")
    return enzyme


enzyme = enzyme_dict()
