import matplotlib.animation
import numpy as np
import matplotlib.pyplot as plt
import numpy.random
import utils

N = 9
matrix = np.zeros((N,N))

'''
for i in range(0,N):
    for j in range(0,N):
        matrix[i,j] = np.random.randint(1,10)

print(matrix)
print(utils.compute_cost(matrix))

utils.PrintSudoku(matrix)
print(utils.row_cost(matrix))
'''
sudoku = '907080520' \
         '380000900' \
         '500000381' \
         '009000000' \
         '013065000' \
         '000470010' \
         '090100050' \
         '030002094' \
         '602090100'

matrix = utils.toMatrix(sudoku,matrix)
check = matrix
utils.PrintSudoku(matrix)

stop = 0
while stop == 0:
    





#Check for duplicates in rows
j_d = utils.row_cost(matrix)
#Check for duplicates in columns
i_d = utils.col_cost(matrix)

print(i_d)

