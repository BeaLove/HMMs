def matrices(vals):
    # We do this for A, then B then pi
    rows = int(vals[0])  # get row value
    cols = int(vals[1])
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    r = 0
    c = 0
    i = 0
    while r < rows:
        while c < cols:
            matrix[r][c] = float(vals[i + 2])
            c = c + 1
            i = i + 1
        c = 0
        r = r + 1
    return matrix, rows, cols


def viterbi(pi, a, b, obsv):
    ##initialize
    a0 = []  # empty list
    o0 = obsv[0]  # first observation
    viterbi = [[0 for i in obsv] for j in range(len(a))]  # viterbi matrix rows = states, columns = timesteps
    delta0 = [pi[i] * b[o0][i] for i in obsv]  # initial * column of emision matrix for time T(0).
    viterbi[0] = delta0  # probability of each state giving us the first observation
    backpointers = [[0 for i in obsv] for j in range(len(A))]
    for t in range(1, len(obsv)):  # for each time step multiply last delta with A matrix and current O(t) column of B
        currentObsv = b[t]  # corresponding column of emission matrix
        for i in range(len(delta0)):  # for every value in delta
            for j in range(len(a)):  # rows of A
                viterbi[t][i] = max(viterbi[t - 1][i] * a[j][k] * currentObsv[i] for k in range(
                    len(a[0])))  # for-loop: columns of A, save max computed probability to viterbi matrix
                backpointers[t][i] = viterbi[t].index(max(viterbi[t - 1][i] for i in range(len(viterbi[
                                                                                                   t - 1]))))  # loop through current column of viterbi and get the state that corresponds to computed max prob.


file = open("hmm2_01.in", "r")
avals = file.readline()
A = matrices(avals)
bvals = file.readline()
B = matrices(bvals)
