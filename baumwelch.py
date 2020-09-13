#implementation of the baum-welch algorithm to estimate lambda given an observation sequence O
#Beatrice Lovely and Daniel Perez-Felipe, KTH AI course
#following the stamp tutorial

#code skeleton 9/13/2020 by BL

from math import log

def data2matrix(data_string):
    # Given a single data input corresponding to a matrix, a matrix is allocated and created

    rows = int(data_string[0])  # get row value
    cols = int(data_string[1])  # get col value

    matrix = [[0.0 for x in range(cols)] for y in range(rows)]  # Creates empty matrix

    r = c = j = 0  # auxiliary variables

    while r < rows:  # Matrix is filled with the given data
        while c < cols:
            matrix[r][c] = float(data_string[j+2])
            c = c + 1
            j = j + 1
        c = 0
        r = r + 1

    return matrix

def baum_welch(observationSequence, A, B, PI):
    T = len(obsvSequence) #length of the observation sequence
    S = len(A) #number of possible states
    N = len(B[0]) #number of possible observations
    alpha = [[0 for i in range(A)] for j in range(T)] #will contain the probabilities of the given observations and states up to time T, computed forwards
    beta = [[0 for i in range(A)] for j in range(T)] #will contain probabilities of all future observations from time T, and any state
    gamma = [[0 for i in range(A)] for j in range(T)]
    di_gamma = [[0 for i in range(A)] for j in range(T)]
    maxIters = 50
    iters = 0
    oldLogProb = -1000

    #alpha(forward)pass
    #initialize alpha0
    firstObsv = observationSequence[0]
    const0 = 0 #scaling constant to avoid underflow
    alpha0 = []
    for i in range(S):
        alpha0[i] = PI[i]*B[i][firstObsv]
        const0 += alpha0[i]
    #scale alpha0
    const0 = 1/const0
    for i in range(S):
        alpha0[i] = const0*alpha0[i]
    alpha[0] =alpha0
    #compute alpha, probability of observation sequence and state Xi
    constants = []
    constants.append(const0)
    for t in range(1, T):
        const_t = 0
        for i in range(S):
            for j in range(S):
                alpha[t][i] += alpha[t-1][j]*A[j][i]*B[j][observationSequence[t+1]]
            const_t += alpha[t][i]
        #scale alpha:
        const_t = 1/const_t
        for i in range(S):
            alpha[t][i] = const_t*alpha[t][i]
        constants.append(const_t)

    #beta(backward) pass
    for i in range(S): #initialize
        beta[-1][i] = constants[-1]
    for t in range(T, -1, -1):
        for i in range(S):
            for j in range(S):
                beta[t][i] += beta[t+1][j]*A[j][i]*B[j][observationSequence[t+1]]
            beta[t][i] = constants[t]*beta[t][i]

    #compute gamma and di-gamma
    for t in range(1,T):
        for i in range(S):
            for j in range(S):
                di_gamma[i][j] = alpha[t][i]*A[j][i]*B[i][observationSequence[t]] #A[j][i] vs A[i][j]?
                gamma[i] += di_gamma[i][j]

    for i in range(S):
        gamma[S][i] = alpha[T][i]

    #re-estimate A,B,PI
    #PI
    for i in range(S):
        PI[i] = gamma[i][0]
    #A
    for i in range(S):
        denom = 0
        for t in range(T-1):
            denom += gamma[t][i]
        for j in range(S):
            numer = 0
            for t in range(T-1):
                numer += di_gamma[t][j]
        A[j][i] = numer/denom

    #B
    for i in range(N):
        denom = 0
        for t in range(T):
            denom += gamma[t][i]
        for j in range(N):
            numer = 0
            for t in range(T):
                if observationSequence[t] ==  j:
                    numer += gamma[t][i]
            b[j][i] = numer/denom

    #logProb
    logProb = 0
    for t in range(T):
        logProb += logProb + log(constant[t])
    logProb = -logProb

    #iterate again?
    iters += 1
    if iters < maxiters and logProb > oldLogProb:
        oldLogProb = logProb
        baum_welch(observationSequence, A, B, PI)
    else:
        return A, B, PI






if __name__ == "__main__":
    file = open("hmm3_01.in")  # TODO. PYCHARM
    #file = sys.stdin  # TODO: KATTIS

    # Data is obtained from input files and classified
    values = file.readlines()
    avals = values[0].split()
    bvals = values[1].split()
    pivals = values[2].split()
    seqvals = values[3].split()
    for i in range(len(seqvals)):
        seqvals[i] = int(seqvals[i])

    # Input data is transformed into matrix form
    A = data2matrix(avals)
    B = data2matrix(bvals)
    PI = data2matrix(pivals)
    # String Input data is transformed into data values
    sequence, num_of_emissions, different_types = data2emission_sequence(seqvals)


#input = open("sample1_RK.in", "r")
#avals = input.readline().split()
avals = input().split()
a, arows, acols = matrices(avals)
#bvals = input.readline().split()
bvals = input().split()
b, brows, bcols = matrices(bvals)
#pivals = input.readline().split()
pivals = input().split()
pi, pirows, picols = matrices(pivals)
pi = pi[0]
#obsv = input.readline().split()
obsv = input().split()
noObsv = obsv.pop(0)
obsv = [int(i) for i in obsv]
#input.close()

