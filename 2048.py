import numpy as np
import random

val = ['L' , 'U' , 'R' , 'D']

def gen(gameState):
    tmp = []
    for i in range(0,4) : 
        for j in range(0,4):
            if gameState[0][i][j] == 0 :
                tmp.append((i,j))
    ind = random.randint(0,len(tmp) - 1)
    return tmp[ind]

def genN() :
    tmp = random.randint(1,2)
    return tmp * 2

def putR(State) :
    tmp = gen(State)
    tmp1 = genN()
    State[0][tmp[0]][tmp[1]] = tmp1

def createAllStates(state) :
    tmp = []
    for i in range(0,4) : 
        for j in range(0,4):
            if state[0][i][j] == 0 :
                state[0][i][j] = 2
                tmp.append(state)
                state[0][i][j] = 4
                tmp.append(state)
                state[0][i][j] = 0
    return tmp

def shiftL(state) :
    change = 0
    work = [np.zeros((4,4)), 0]
    for i in range(0,4):
        for j in range(0,4):
            work[0][i][j] = state[0][i][j]
    work[1] = state[1]
    for j in range(1, 4) :
        for i in range(0,4) :
            col = j - 1
            while col > -1 :
                if work[0][i][col + 1] == work[0][i][col] :
                    work[0][i][col + 1] = 0
                    work[0][i][col] *= 2
                    work[1] += work[0][i][col]
                    col = -1
                    change = 1
                elif work[0][i][col] == 0 :
                    work[0][i][col] = work[0][i][col + 1]
                    work[0][i][col + 1] = 0
                    col -= 1
                    change = 1
                else :
                    break
    return (work , change)

def shiftR(state) :
    change = 0
    work = [np.zeros((4,4)), 0]
    for i in range(0,4):
        for j in range(0,4):
            work[0][i][j] = state[0][i][j]
    work[1] = state[1]
    for j in reversed(range(3)) :
        for i in range(0,4) :
            col = j + 1
            while col < 4 :
                if work[0][i][col - 1] == work[0][i][col] :
                    work[0][i][col - 1] = 0
                    work[0][i][col] *= 2
                    work[1] += work[0][i][col]
                    col = 4
                    change = 1
                elif work[0][i][col] == 0 :
                    work[0][i][col] = work[0][i][col - 1]
                    work[0][i][col - 1] = 0
                    col += 1
                    change = 1
                else :
                    break
    return (work , change)

def shiftU(state) :
    change = 0
    work = [np.zeros((4,4)), 0]
    for i in range(0,4):
        for j in range(0,4):
            work[0][i][j] = state[0][i][j]
    work[1] = state[1]
    for i in range(1, 4) :
        for j in range(0,4) :
            row = i - 1
            while row > -1 :
                if work[0][row + 1][j] == work[0][row][j] :
                    work[0][row + 1][j] = 0
                    work[0][row][j] *= 2
                    work[1] += work[0][row][j]
                    row = -1
                    change = 1
                elif work[0][row][j] == 0 :
                    work[0][row][j] = work[0][row + 1][j]
                    work[0][row + 1][j] = 0
                    row -= 1
                    change = 1
                else :
                    break
    return (work , change)

def shiftD(state) :
    change = 0
    work = [np.zeros((4,4)), 0]
    for i in range(0,4):
        for j in range(0,4):
            work[0][i][j] = state[0][i][j]
    work[1] = state[1]
    for i in reversed(range(3)) :
        for j in range(0,4) :
            row = i + 1
            while row < 4 :
                if work[0][row - 1][j] == work[0][row][j] :
                    work[0][row - 1][j] = 0
                    work[0][row][j] *= 2
                    work[1] += work[0][row][j]
                    row = 4
                    change = 1
                elif work[0][row][j] == 0 :
                    work[0][row][j] = work[0][row - 1][j]
                    work[0][row - 1][j] = 0
                    row += 1
                    change = 1
                else :
                    break
    return (work , change)

def checkEnd(state) :
    for i in state[0] :
        for j in i :
            if j == 0 :
                return 0
    return 1

def get(state , m) :
    if m == 0 : 
        state , change = shiftL(state)
    elif m == 1 :
        state , change = shiftU(state)
    elif m == 2 : 
        state , change = shiftR(state)
    else :
        state , change = shiftD(state)
    return (state , change)

def move(state , m) :
    work = [np.zeros((4,4)), 0]
    for i in range(0,4):
        for j in range(0,4):
            work[0][i][j] = state[0][i][j]
    work[1] = state[1]
    state , change = get(state , m)
    if(checkEnd(state)) :
        print(work)
        exit()
    else :
        putR(state)
    return state

def score(state) :
    tmp = []
    tmp1 = np.zeros((6,6))
    taken = np.zeros((6,6))
    for i in range(0,4) :
        for j in range(0,4) :
            tmp.append([state[i][j] , i , j])
            tmp1[i + 1][j + 1] = state[i][j]
    tmp.sort(reverse = True)
    sc = 0
    tmp2 = []
    tmp2.append(tmp[0][0])
    pos = 1
    while len(tmp2) < 4 and pos < 16:
        if tmp[pos][0] != tmp[pos - 1][0] :
            tmp2.append(tmp[pos][0])
        pos += 1
    for i in range(0,min(4,len(tmp2))) :
        if state[0][i] == tmp2[i] :
            sc += 4 * tmp2[i]
        else :
            break
    # for i in range (0,8):
    #     sc += tmp[i][0] * 3 / (1 + tmp[i][1] + tmp[i][2])
    sc1 = 0
    for i in range(1,5) :
        for j in range(1,5) :
            if taken[i][j] :
                continue
            if tmp1[i + 1][j] == tmp1[i][j] and not taken[i + 1][j]:
                sc1 += tmp1[i][j]
                taken[i][j] = 1
                taken[i + 1][j] = 1
            elif tmp1[i - 1][j] == tmp1[i][j] and not taken[i - 1][j]:
                sc1 += tmp1[i][j]
                taken[i][j] = 1
                taken[i - 1][j] = 1
            elif tmp1[i][j + 1] == tmp1[i][j] and not taken[i][j + 1]:
                taken[i][j] = 1
                taken[i][j + 1] = 1
                sc1 += tmp1[i][j]
            elif tmp1[i][j - 1] == tmp1[i][j] and not taken[i][j - 1]:
                sc1 += tmp1[i][j]
                taken[i][j] = 1
                taken[i][j - 1] = 1
    return sc1 + sc * 4

def solve(state , dep):
    tmp1 = []
    bestScore = -1
    bestCur = -1
    for i in range(0,2) :
        tmp, change = get(state , i)
        if checkEnd(tmp) or change == 0:
            continue
        tmp1 = createAllStates(tmp)
        # worst = 100000000
        # findMed = []
        # best = 0
        avg = 0
        for curState in tmp1 :
            if dep > 0:
                bestMove = solve(curState , dep - 1)
                # worst = min(worst , bestMove[1])
                # findMed.append(bestMove[1])
                # best = max(best , bestMove[1])
                avg += bestMove[1]
            else :
                # worst = min(worst , tmp[i][1] + score(tmp[i][0]))
                # findMed.append(tmp[1] + score(tmp[0]))
                # best = max(best , tmp[1] + score(tmp[0]))
                avg += tmp[1] + score(tmp[0])
        # findMed.sort()
        # mid = len(findMed)//2
        # worst = (findMed[mid] + findMed[~mid]) / 2
        avg /= len(tmp1)
        if avg > bestScore :
            bestCur = i
            bestScore = avg
    if bestScore == -1 :
        for i in range(2,4) :
            tmp, change = get(state , i)
            if checkEnd(tmp) or change == 0:
                continue
            tmp1 = createAllStates(tmp)
            # worst = 100000000
            # findMed = []
            # best = 0
            avg = 0
            for curState in tmp1 :
                if dep > 0:
                    bestMove = solve(curState , dep - 1)
                    # worst = min(worst , bestMove[1])
                    # findMed.append(bestMove[1])
                    # best = max(best , bestMove[1])
                    avg += bestMove[1]
                else :
                    # worst = min(worst , tmp[i][1] + score(tmp[i][0]))
                    # findMed.append(tmp[1] + score(tmp[0]))
                    # best = max(best , tmp[1] + score(tmp[0]))
                    avg += tmp[1] + score(tmp[0])
            # findMed.sort()
            # mid = len(findMed)//2
            # worst = (findMed[mid] + findMed[~mid]) / 2
            avg /= len(tmp1)
            if avg > bestScore :
                bestCur = i
                bestScore = avg
    return [bestCur , bestScore]

gameState = [np.zeros((4,4) , dtype = int), 0 ]
putR(gameState)
putR(gameState)
tmp1 = 0
while 1:
    tmp = solve(gameState , 1)
    if tmp[0] == -1 :
        print(gameState[0])
        exit()
    print(gameState[0] , '\n' , val[tmp[0]] , '\n')
    gameState = move(gameState , tmp[0])