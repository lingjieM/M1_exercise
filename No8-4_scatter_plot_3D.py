from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import csv

fig = pyplot.figure()
ax = Axes3D(fig)
x = []
y = []
z = []
n = []
with open("/Users/menglingjie/PycharmProjects/M1_exercise/No8/16Sread_merged/MDS_3D.csv","r") as infile:
    csv = csv.reader(infile)
    for row in csv:
        x.append(row[1])
        y.append(row[2])
        z.append(row[3])
        n.append(row[0])
    del x[0]
    del y[0]
    del z[0]
    del n[0]
    x = list(map(float, x))
    y = list(map(float, y))
    z = list(map(float, z))
ax.scatter(x, y, z)
m = ["Day1 12:00", "Day1 15:00", "Day1 18:00", "Day1 21:00", "Day2 00:00", "Day2 3:00", "Day2 6:00", "Day2 9:00", "Day2 12:00"]
for i, j, m, l in zip(x, y, z, m):
    ax.text(i, j, m, l)
pyplot.show()
