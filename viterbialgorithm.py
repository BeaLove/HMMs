def matrices(vals):
    ## produce matrices from our given input values
    rows = int(vals[0])  # get row value
    cols = int(vals[1])
    matrix = [[0.0 for x in range(cols)] for y in range(rows)]
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
    ##takes initial state probabilities (pi), transition probabilities(a) and observation probabilities(b)
    ## and a given observation sequence
    ## returns the most likely state sequence and its probability
    firstobsv = obsv[0] #the first observation
    delta0 = []
    for i in range(len(b)):
        delta0.append(pi[i]*b[i][firstobsv])##initialize probability of first observation given initial probabilities
    #print('delta1', delta0)
    viterbi = [[0 for i in range(len(a))] for j in range(len(obsv))] #empty viterbi matrix
    viterbi[0] = delta0 #add delta0 to viterbi matrix
    backpointers = [[9 for i in range(len(a))] for j in range(len(obsv))] #initialize empty backpointers
    for t in range(1, len(obsv)): ##recursive step
        currentObsv = obsv[t]
        for i in range(len(delta0)):
            #here, instead of summing all probabilities, we create a list for every
            #column of the transition matrix a, and fetch the maximum probability (most likely previous state)
            probabilities = [] #empty probabilities list
            for j in range(len(a[0])):
                probabilities.append(viterbi[t-1][j]*a[j][i]*b[i][currentObsv]) #for every column in a
            viterbi[t][i] = max(probabilities) #most likely transition #keep only the max from the list created, instead of the sum
            backpointers[t][i] = probabilities.index(max(probabilities)) #most likely previous state

    bestpathprob = max(viterbi[-1]) #max probability from the last iteration = total probability of this path
    laststate = viterbi[-1].index(max(viterbi[-1]))
    bestpath = [0 for i in range(len(obsv))]
    bestpath[0] = laststate
    for i in range(1, len(obsv)):
        bestpath[i] = backpointers[-i][laststate]
        laststate = bestpath[i]
    bestpath.reverse()
    return bestpathprob, bestpath

def output(list):
    string = ""
    for i in list:
        string += str(i) + " "
    string = string[:-1]
    return string

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
bestpathprob, bestpath = viterbi(pi, a, b, obsv)
bestpathformat = output(bestpath)
print(bestpathformat)
