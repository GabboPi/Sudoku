import numpy as np
def row_sum(matrix,i):
    return sum(matrix[i,])

def col_sum(matrix,i):
    return sum(matrix[:,1])

def row_cost(matrix):
    s = np.shape(matrix)
    cost = np.zeros(s[0])
    for i in range(0,s[0]):
        cost[i] = s[1] - len(np.unique(matrix[i,:]))
    return cost
def col_cost(matrix):
    s = np.shape(matrix)
    cost = np.zeros(s[1])
    for i in range(0,s[1]):
        cost[i] = s[1] - len(np.unique(matrix[:,i]))
    return cost


def compute_cost(matrix):
    s = np.shape(matrix)
    cost = 0
    for i in range(0,s[0]):
        cost += s[1] - len(np.unique(matrix[i,:]))
    return cost

def PrintSudoku(sudoku):
    print("\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i,j].astype(int))+" "
        print(line)
def toMatrix(sudoku,matrix):
    count = 0
    i = 0
    j = 0
    for k in sudoku:
        k = int(k)
        if (k != 0):
            matrix[i,j] = k
        else:
            matrix[i,j] = 0
        count += 1
        i,j = divmod(count,9)
    return matrix
