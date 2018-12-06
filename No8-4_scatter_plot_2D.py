from matplotlib import pyplot
import csv

x = []
y = []
n = []
with open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/MDS_2D.csv", "r") as infile:
    csv = csv.reader(infile)
    for row in csv:
        x.append(row[1])
        y.append(row[2])
        n.append(row[0])
    del x[0]
    del y[0]
    del n[0]
    z = ["Day1 12:00", "Day1 15:00", "Day1 18:00", "Day1 21:00", "Day2 00:00", "Day2 3:00", "Day2 6:00", "Day2 9:00", "Day2 12:00"]
    x = list(map(float, x))
    y = list(map(float, y))
pyplot.scatter(x, y)
for i, j, m in zip(x, y, z):
    pyplot.text(i, j, m)
pyplot.show()
