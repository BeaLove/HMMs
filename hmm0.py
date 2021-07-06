# # HMM0. KTH EECS
# # AI
#
# #
# A= [4 ,4 ,0.2 0.5 0.3 0.0 0.1 0.4 0.4 0.1 0.2 0.0 0.4 0.4 0.2 0.3 0.0 0.5]
# 4 3 1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0 0.2 0.6 0.2
# 1 4 0.0 0.0 0.0 1.0
#
# A = [[0.2, 0.5, 0.3, 0.0],  ]

def matrices(vals):
     # We do this for A, then B then pi
    rows = int(vals[0]) #get row value
    cols = int(vals[1])
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    r = 0
    c = 0
    i = 0
    while r < rows:
        while c < cols:
            matrix[r][c] = float(vals[i+2])
            c = c + 1
            i = i + 1
        c = 0
        r = r + 1
    return matrix, rows, cols


def product_matrices(matrixA, matrixB, rowsA, colsB):
    matrix_prod = [ [ 0 for i in range(colsB) ] for j in range(rowsA) ]
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrix_prod[i][j] += matrixA[i][k] * matrixB[k][j]
    print(matrix_prod)
    return matrix_prod
### new code by Beatrice 9/3/2020:
### cleaned up the matrix multiplication a little :)
def initializeHMM(PI, A):
    PI = PI[0] #make PI a proper vector
    PI1 = [0 for i in range(len(PI)] #create empty
    for i in range(len(PI)): #for each in PI
        for j in range(len(A)): #rows of A
            a0[i] = sum(PI[i]*A[j][k] for k in range(len(A[0]))) #cols of A w list comprehension
    return PI1

PI1 = initializeHMM(PI, A):
a0 = initializeHMM(PI1, B)
def toString(a0): #make a string of the initialized HMM
    str = ""
    for i in a0:
        str += " "+ i
    return str
ans = open("sample_00.ans", "w") #open answer file in write mode
ans.write(str) #write string in file on one line

### end new code

def matrix2str(matrixX):
    stri = ''
    for a in

file = open("sample_00.in", "r") #open file in read mode
values = file.readlines()
avals = values[0].split()
bvals = values[1].split()
pivals = values[2].split()

A, arows, acols = matrices(avals)
B, brows, bcols= matrices(bvals)
PI, pirows, picols = matrices(pivals)

PitimesA = product_matrices(PI,A,pirows,acols)
final_result = product_matrices(PitimesA,B,pirows,bcols)

