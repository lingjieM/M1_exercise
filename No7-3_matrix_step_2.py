import numpy as np



adj_matrix = np.genfromtxt("/Users/menglingjie/PycharmProjects/M1_exercise/No7/adjacency_matrix_pure.csv", delimiter=",")
adj_matrix_blc = np.block(adj_matrix)
print(adj_matrix_blc)
