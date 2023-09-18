import sys


class State:
    def __init__(self, parent, num_red, num_blue):
        self.parent = parent
        self.num_red = num_red
        self.num_blue = num_blue
        self.amount = None


def MinMax_AlphaBeta(maxPlayer, depth, state, ap, bt, maxdepth):

    if state.num_red == 0:
        state.amount = state.num_blue*3
        if maxPlayer != True:
            state.amount = state.amount*-1
        return state
    if state.num_blue == 0:
        state.amount = state.num_red*2
        if maxPlayer != True:
            state.amount = state.amount*-1
        return state

    if int(depth) == int(maxdepth):
        if maxPlayer != True:
            if (state.num_red+state.num_blue) % 2 == 0:
                state.amount = 2
            else:
                state.amount = -2
        else:
            if (state.num_red+state.num_blue) % 2 == 0:
                state.amount = -2
            else:
                state.amount = 2
        return state

    if maxPlayer:
        best = -1000
        leftNode = State(state, state.num_red-1, state.num_blue)
        optimalNode = leftNode
        left = MinMax_AlphaBeta(False, depth+1, leftNode, ap, bt, maxdepth)
        best = max(best, left.amount)
        if left.amount == best:
            optimalNode = left
        if bt <= best:
            return optimalNode
        ap = max(ap, best)
        rightNode = State(state, state.num_red, state.num_blue-1)
        right = MinMax_AlphaBeta(False, depth+1, rightNode, ap, bt, maxdepth)
        best = max(best, right.amount)
        if right.amount == best and right.amount != left.amount:
            optimalNode = right
        if bt <= best:
            return optimalNode
        ap = max(ap, best)
        return optimalNode
    else:
        best = 1000
        leftNode = State(state, state.num_red-1, state.num_blue)
        optimalNode = leftNode
        left = MinMax_AlphaBeta(True, depth+1, leftNode, ap, bt, maxdepth)
        best = min(best, left.amount)
        if left.amount == best:
            optimalNode = left
        if best <= ap:
            return optimalNode
        bt = min(bt, best)
        rightNode = State(state, state.num_red, state.num_blue-1)
        right = MinMax_AlphaBeta(False, depth+1, rightNode, ap, bt, maxdepth)
        best = min(best, right.amount)
        if right.amount == best and right.amount != left.amount:
            optimalNode = right
        if best <= ap:
            return optimalNode
        bt = min(bt, best)
        return optimalNode


current_player = 'computer'
maxdepth = 1000000
num_red = sys.argv[1]
num_red = int(num_red)
num_blue = sys.argv[2]
num_blue = int(num_blue)

if len(sys.argv) > 3:
    current_player = sys.argv[3]
if len(sys.argv) > 4:
    maxdepth = sys.argv[4]

while (not (num_red == 0 or num_blue == 0)):
    print(num_red, num_blue)
    if current_player == 'human':
        ball = input("Enter red or blue:")
        if ball == 'blue':
            num_blue = num_blue-1
        else:
            num_red = num_red-1
        current_player = 'computer'
    else:
        startNode = State(None, num_red, num_blue)
        terminalnode = MinMax_AlphaBeta(
            True, 0, startNode, -1000, 1000, maxdepth)
        while terminalnode.parent != startNode:
            terminalnode = terminalnode.parent
        if terminalnode.num_blue != num_blue:
            num_blue = num_blue-1
            print("Computer removed blue")
        else:
            num_red = num_red-1
            print("Computer removed red")
        current_player = 'human'
    if num_red == 0 or num_blue == 0:
        if current_player == 'human':
            if num_red == 0:
                amount = num_blue*3
            else:
                amount = num_red*2
            print("Human won with an amount of ", amount)
        else:
            if num_red == 0:
                amount = num_blue*3
            else:
                amount = num_red*2
            print("Computer won with an amount of ", amount)
