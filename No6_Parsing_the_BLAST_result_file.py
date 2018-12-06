
def gene1():
    html = open("/Users/menglingjie/PycharmProjects/M1_exercise/No6/TsxC.html", "w")
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No6/YsxC.tsv") as tsv:
        print("<table>", file=html)
        for line in tsv:
            row = line.split("\t")
            if eval(row[10]) < 1e-10:
                print("<tr>", file=html)
                print("<td>%s</td>" % row[0], file=html)
                print("<td>%s</td>" % row[1], file=html)
                print("<td>%s</td>" % row[2], file=html)
                print("<td>%s</td>" % row[3], file=html)
                print("<td>%s</td>" % row[4], file=html)
                print("<td>%s</td>" % row[5], file=html)
                print("<td>%s</td>" % row[6], file=html)
                print("<td>%s</td>" % row[7], file=html)
                print("<td>%s</td>" % row[8], file=html)
                print("<td>%s</td>" % row[9], file=html)
                print("<td>%s</td>" % row[10], file=html)
                print("<td>%s</td>" % row[11], file=html)
                print("<tr>", file=html)
            else:
                continue
        print("<table>", file=html)
    html.close()


def gene2():
    html = open("/Users/menglingjie/PycharmProjects/M1_exercise/No6/tRNA-lysidine_synthetase.html", "w")
    with open("/Users/menglingjie/PycharmProjects/M1_exercise/No6/tRNA-lysidine_synthetase.tsv") as tsv:
        print("<table>", file=html)
        for line in tsv:
            row = line.split("\t")
            if eval(row[10]) < 1e-10:
                print("<tr>", file=html)
                print("<td>%s</td>" % row[0], file=html)
                print("<td>%s</td>" % row[1], file=html)
                print("<td>%s</td>" % row[2], file=html)
                print("<td>%s</td>" % row[3], file=html)
                print("<td>%s</td>" % row[4], file=html)
                print("<td>%s</td>" % row[5], file=html)
                print("<td>%s</td>" % row[6], file=html)
                print("<td>%s</td>" % row[7], file=html)
                print("<td>%s</td>" % row[8], file=html)
                print("<td>%s</td>" % row[9], file=html)
                print("<td>%s</td>" % row[10], file=html)
                print("<td>%s</td>" % row[11], file=html)
                print("<tr>", file=html)
            else:
                continue
        print("<table>", file=html)
    html.close()


def main():
    gene1()
    gene2()


main()








