from collections import deque
import numpy as np
import sys
import heapq



# read  file as user argument
Input_Data = np.genfromtxt(sys.argv[1], dtype=int, encoding=None, skip_footer=1)
Output_Data = np.genfromtxt(sys.argv[2], dtype=int, encoding=None, skip_footer=1)
# read text file from local
# Input_Data = np.genfromtxt('input.txt', dtype=int, encoding=None, skip_footer=1)
# Output_Data = np.genfromtxt('output.txt', dtype=int, encoding=None, skip_footer=1)

# Required output variables from every algorithm
Nodes_Popped= 0
Nodes_Expanded= 0
Nodes_Generated= 0
Max_Fringe_Size =0

class GridState:
    def __init__(self, state, parent, direction, depth, cost,heuristic=0):
        global Nodes_Generated
        Nodes_Generated=Nodes_Generated+1
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth
        self.cost = cost
        self.heuristic=heuristic
        self.var = ''.join(str(e) for e in self.state)

    def __lt__(a,b):
        return (a.cost) < (b.cost)



#  to get zero number position from input 3*3 grid
def search(Input_Data, number=0):
    for i in range(len(Input_Data)):
        for j in range(len(Input_Data[i])):
            if Input_Data[i][j] == number:
                return [i, j]
    return [-1, -1]

# To find each number position and getting heuristic value using manhattan distance
def cal_heuristic(Input_Data):
    sum=0
    for a in range(0,9):
        [X1,Y1]=search(Input_Data,a)
        [X2,Y2]=search(Output_Data,a)
        man=abs(X1-X2)+abs(Y1-Y2)
        heuristic=man*a
        sum=sum+heuristic
    return sum

# to make copy of a list
def colist(inputlist):
    Output=[]
    for x in range(len(inputlist)):
        temp = []
        for elem in inputlist[x]:
            temp.append(elem)
        Output.append(temp)
    return Output


# Children nodes functions
def adolescent(node):
    l = search(node.state)
    r, c = l[0], l[1]

    Children = []
    # moving left
    if c + 1 < len(Input_Data):
        temp1 = colist(node.state)
        x1 = temp1[r][c]
        temp1[r][c] = temp1[r][c + 1]
        temp1[r][c + 1] = x1
        Children.append(GridState(temp1, node, 'LEFT', node.depth + 1, node.cost + temp1[r][c]))

    # moving right
    if c - 1 >= 0:
        temp2 = colist(node.state)
        x2 = temp2[r][c]
        temp2[r][c] = temp2[r][c - 1]
        temp2[r][c - 1] = x2
        Children.append(GridState(temp2, node, 'RIGHT', node.depth + 1, node.cost + temp2[r][c]))

    # moving up
    if r - 1 >= 0:
        temp3 = colist(node.state)
        x3 = temp3[r][c]
        temp3[r][c] = temp3[r - 1][c]
        temp3[r - 1][c] = x3
        Children.append(GridState(temp3, node, 'UP', node.depth + 1, node.cost + temp3[r][c]))

    # moving down
    if r + 1 < len(Input_Data):
        temp4 = colist(node.state)
        x4 = temp4[r][c]
        temp4[r][c] = temp4[r + 1][c]
        temp4[r + 1][c] = x4
        Children.append(GridState(temp4, node, 'DOWN', node.depth + 1, node.cost + temp4[r][c]))

    return Children


def bfs(Input_Data):

    global Nodes_Popped, Nodes_Expanded, Nodes_Generated, Max_Fringe_Size
    Closeset= set()
    # FIFO
    Queue = deque([GridState(Input_Data, None, None, 0, 0)])
    while Queue:
        if len(Queue) > Max_Fringe_Size:
            Max_Fringe_Size=len(Queue)

        node = Queue.popleft()
        Nodes_Popped=Nodes_Popped+1
        Closeset.add(node.var)

        if (node.state == Output_Data).all():

            print('goal found')
            print('Nodes_Popped:',Nodes_Popped)
            print('Nodes_Expanded:',Nodes_Expanded)
            print('Nodes_Generated:',Nodes_Generated)
            print('Max_Fringe_Size:',Max_Fringe_Size)
            print('solution found at depth ',node.depth, 'with cost of',node.cost)

            steps = []

            while (node.state != Input_Data).any():
                steps.append("move   "+str(node.cost-node.parent.cost)+ "    "+ node.direction)
                node=node.parent
            steps=steps[::-1]
            print(*steps, sep='\n')
            return

        Paths = adolescent(node)
        Nodes_Expanded =Nodes_Expanded+1

        for path in Paths:
            if path.var not in Closeset:
                Queue.append(path)
                Closeset.add(path.var)

        if dump == 'true':
            writedata(node, Queue, Closeset)




def dfs(Input_Data):

    global Nodes_Popped, Nodes_Expanded, Nodes_Generated, Max_Fringe_Size
    Closeset= set()
    # LIFO
    Queue = list([GridState(Input_Data, None, None, 0, 0)])
    while Queue:
        if len(Queue) > Max_Fringe_Size:
            Max_Fringe_Size=len(Queue)

        node = Queue.pop()
        Nodes_Popped=Nodes_Popped+1
        Closeset.add(node.var)

        if (node.state == Output_Data).all():

            print('goal found')
            print('Nodes_Popped:',Nodes_Popped)
            print('Nodes_Expanded:',Nodes_Expanded)
            print('Nodes_Generated:',Nodes_Generated)
            print('Max_Fringe_Size:',Max_Fringe_Size)
            print('solution found at depth ',node.depth, 'with cost of',node.cost)

            steps = []

            while (node.state != Input_Data).any():
                steps.append("move   "+str(node.cost-node.parent.cost)+ "    "+ node.direction)
                node=node.parent
            steps=steps[::-1]
            print(*steps, sep='\n')
            return

        Paths = adolescent(node)
        Nodes_Expanded =Nodes_Expanded+1
        # Generating children from a parent
        for path in Paths:
            if path.var not in Closeset:
                Queue.append(path)
                Closeset.add(path.var)

        if dump == 'true':
            writedata(node, Queue, Closeset)





def dls(Input_Data,a):

    global Nodes_Popped, Nodes_Expanded, Nodes_Generated, Max_Fringe_Size
    # Closeset= set()
    Queue = list([GridState(Input_Data, None, None, 0, 0)])
    while Queue:
        if len(Queue) > Max_Fringe_Size:
            Max_Fringe_Size=len(Queue)

        node = Queue.pop()
        Nodes_Popped=Nodes_Popped+1
        # Closeset.add(node.var)

        if (node.state == Output_Data).all():

            print('goal found')
            print('Nodes_Popped:',Nodes_Popped)
            print('Nodes_Expanded:',Nodes_Expanded)
            print('Nodes_Generated:',Nodes_Generated)
            print('Max_Fringe_Size:',Max_Fringe_Size)
            print('solution found at depth ',node.depth, 'with cost of',node.cost)

            steps = []

            while (node.state != Input_Data).any():

                steps.append("move   "+str(node.cost-node.parent.cost)+ "    "+ node.direction)
                node=node.parent
            steps=steps[::-1]
            print(*steps, sep='\n')
            return 1
        if node.depth < a :

            Paths = adolescent(node)
            Nodes_Expanded =Nodes_Expanded+1

            for path in Paths:
                # if path.var not in Closeset:
                Queue.append(path)
                    # Closeset.add(path.var)
            if dump == 'true':
                writedata(node, Queue,[])
    return 0



def ids(Input_Data):
    depth=0
    solution_found =False
    while solution_found == False:
        result= dls(Input_Data,depth)
        print("depth:",depth,"  ",result)
        if result ==1:
            solution_found = True
        depth=depth+1



def ucs(Input_Data):

    global Nodes_Popped, Nodes_Expanded, Nodes_Generated, Max_Fringe_Size
    Closeset= set()

    Queue = [(0,GridState(Input_Data, None, None, 0, 0))]
    while Queue:
        if len(Queue) > Max_Fringe_Size:
            Max_Fringe_Size=len(Queue)

        cost, node =heapq.heappop(Queue)
        Nodes_Popped=Nodes_Popped+1
        Closeset.add(node.var)

        if (node.state == Output_Data).all():

            print('goal found')
            print('Nodes_Popped:',Nodes_Popped)
            print('Nodes_Expanded:',Nodes_Expanded)
            print('Nodes_Generated:',Nodes_Generated)
            print('Max_Fringe_Size:',Max_Fringe_Size)
            print('solution found at depth ',node.depth, 'with cost of',node.cost)

            steps = []

            while (node.state != Input_Data).any():
                steps.append("move   "+str(node.cost-node.parent.cost)+ "    "+ node.direction)
                node=node.parent
            steps=steps[::-1]
            print(*steps, sep='\n')
            return

        Paths = adolescent(node)
        Nodes_Expanded =Nodes_Expanded+1

        for path in Paths:
            if path.var not in Closeset:
                heapq.heappush(Queue,(path.cost, path))
                Closeset.add(path.var)

        if dump == 'true':
            writedata(node, Queue, Closeset)




def greedy(Input_Data):

    global Nodes_Popped, Nodes_Expanded, Nodes_Generated, Max_Fringe_Size
    Closeset= set()

    Queue = [(0,GridState(Input_Data, None, None, 0, 0))]
    while Queue:
        if len(Queue) > Max_Fringe_Size:
            Max_Fringe_Size=len(Queue)

        cost, node =heapq.heappop(Queue)
        Nodes_Popped=Nodes_Popped+1
        Closeset.add(node.var)

        if (node.state == Output_Data).all():

            print('goal found')
            print('Nodes_Popped:',Nodes_Popped)
            print('Nodes_Expanded:',Nodes_Expanded)
            print('Nodes_Generated:',Nodes_Generated)
            print('Max_Fringe_Size:',Max_Fringe_Size)
            print('solution found at depth ',node.depth, 'with cost of',node.cost)

            steps = []

            while (node.state != Input_Data).any():
                steps.append("move   "+str(node.cost-node.parent.cost)+ "    "+ node.direction)
                node=node.parent
            steps=steps[::-1]
            print(*steps, sep='\n')
            return

        Paths = adolescent(node)
        Nodes_Expanded =Nodes_Expanded+1

        for path in Paths:
            if path.var not in Closeset:
                path.heuristic=cal_heuristic(path.state)
                heapq.heappush(Queue,(path.heuristic, path))
                Closeset.add(path.var)

        if dump == 'true':
            writedata(node, Queue, Closeset)




def astar(Input_Data):

    global Nodes_Popped, Nodes_Expanded, Nodes_Generated, Max_Fringe_Size
    Closeset= set()

    Queue = [(0,GridState(Input_Data, None, None, 0, 0))]
    while Queue:
        if len(Queue) > Max_Fringe_Size:
            Max_Fringe_Size=len(Queue)

        cost, node =heapq.heappop(Queue)
        Nodes_Popped=Nodes_Popped+1
        Closeset.add(node.var)

        if (node.state == Output_Data).all():

            print('goal found')
            print('Nodes_Popped:',Nodes_Popped)
            print('Nodes_Expanded:',Nodes_Expanded)
            print('Nodes_Generated:',Nodes_Generated)
            print('Max_Fringe_Size:',Max_Fringe_Size)
            print('solution found at depth ',node.depth, 'with cost of',node.cost)

            steps = []

            while (node.state != Input_Data).any():
                steps.append("move   "+str(node.cost-node.parent.cost)+ "    "+ node.direction)
                node=node.parent
            steps=steps[::-1]
            print(*steps, sep='\n')
            return

        Paths = adolescent(node)
        Nodes_Expanded =Nodes_Expanded+1

        for path in Paths:
            if path.var not in Closeset:
                path.heuristic=cal_heuristic(path.state)+path.cost
                heapq.heappush(Queue,(path.heuristic, path))
                Closeset.add(path.var)

        if dump =='true':
            writedata(node,Queue,Closeset)

# Generating read.txt file for a given method
def writedata(expanding,fringe, visited):
    file.write("\n generating adolscent Nodes:")
    file.write(str(expanding.state)+" "+"Action="+str(expanding.direction)+" depth:"+str(expanding.depth) +" cost:"+str(expanding.cost)
               +" heuristic cost:"+str(expanding.heuristic))
    file.write("\n]\n")
    file.write("\nClosed: [\n")
    for j in visited:
        file.write(j + " ;")
    file.write("\n]")
    file.write("\nfringe: \n")

    for i in fringe:
        if type(i) is tuple:
            j=i[1]
        else:
            j=i
        file.write("<state:"+str(j.state)+" "+" depth:"+str(j.depth) +" cost:"+str(j.cost)+" heuristic cost:"+str(j.heuristic)+" >")



from datetime import datetime


filename1 = datetime.now().strftime("%Y_%m_%d--%I:%M:%S_%p")
print(filename1)

# setting a* as default method
dump='false'
if len(sys.argv)>=4:
    method = sys.argv[3]
    if method == 'true' or method == 'false':
        dump= method
        method='a*'
else:
    method = 'a*'


# check whether dump variable is present or not
if len(sys.argv)>=5:
    dump = sys.argv[4]

print(method,dump)


# Taking various traversals as user argument
from datetime import datetime
if dump== 'true':
    filename = "trace-" + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + ".txt"
    file =open(filename,'w')

if method == 'bfs':
    bfs(Input_Data)
if method == 'dfs':
    dfs(Input_Data)
if method == 'ucs':
    ucs(Input_Data)
if method=='dls':
    a = int(input('please enter the depth limit of dls '))
    dls(Input_Data,a)
if method=='ids':
    ids(Input_Data)
if method =='a*':
    astar(Input_Data)
if method == 'greedy':
    greedy(Input_Data)
if dump =='true':
   file.write("\nNodes popped:"+str(Nodes_Popped))
   file.write("\nNodes Expanded:"+str(Nodes_Expanded))
   file.write("\nNodes Generated:"+str(Nodes_Generated))
   file.write("\nMax frindge size:"+str(Max_Fringe_Size))
   file.close()



