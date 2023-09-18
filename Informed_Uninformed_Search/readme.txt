

I have done the assignment 1 in pyton pycharm

1) Imported all required librares,used sys.argv to call the command line arguments. Thus sys.argv[1] is used to call start-file ;sys.argv[2] is used to call goal file. 

2) A class gridstate to used to mention current state, parent,direction,depth ,cost.

3) We can only move number'0' in 4 direction so i defined a search function which returns position of number '0'

4) After the position of '0' is known we need to know in which direction '0' can be moved : up or down or left or right.
   This is been defined in a function named adolescent and this function will return children of current node. 
   In this function we need to make sure every time a correct parent node is passed while generating children; thus a copy function is used.

5) BFS: closeset is initially asigned to set as we need to make sure every node in closeset is unique. Used deque( doubly ended queue) structure to make pop 
	and add children from current frindge . (.pop ) is used to pop the first elemet from the frindge, every time a node is popped iterate the nodes popped.
	Every time a child is generated from parent which is not in a close set we need to iterate the nodes expanded. if length of frindge is more than max frindge size 
	set lengh of frindge as max frindge size. Every time a node is generated iterate the nodes generated. If current node state is equals to goal state return all the
	required set of output variables. If dump condition is true get the written file. 

6) DFS: closeset is initially asigned to set as we need to make sure every node in closeset is unique. Used list data structure here.(.pop ) is used to pop 
	the last elemet from the frindge[LIFO] , every time a node is popped iterate the nodes popped.Every time a child is generated from parent which is 
	not in a close set we need to iterate the nodes expanded. if length of frindge is more than max frindge size 
	set lengh of frindge as max frindge size. Every time a node is generated iterate the nodes generated. If current node state is equals to goal state 
	return all the required set of output variables. If dump condition is true get the written file. 


7) DLS: This is same as DFS but here we need to specify the depth length. We need to only generate child from parent if and only if current depth of node is less than 
	mentioned depth length. 

8) IDS: Here depth length isnt specified but we increment depth length one by one untill infinite. This is been done till goal state is found. 
	if goal state is not found return 0 or return 1

9) UCS: The frindge is in list of tuple. heapq.heappop is used to pop the least cost node. If a child node is not in close set we need to append that node 
	using heapq.heappush. 

  
10) greedy : heuristic value is used to pop the node, the node having least heuristic value is popped. For this cal heuristic function is used. 
	     where we get the location of a number in both input nd output state, after we use manhattan distance formula to get the distance. distance is mutliplied with current number to get the heuristic value. 
	     Similarly for every number we get heuristic value. Every value is added up to get total heuristic number. This value is used for popping the node.

11) a* : here the cost is total heuristic value + cost of the particular node . This value is used for popping the node.

IN COMMAND PROMPT 
My python file is AI.py MY start file is input.txt and my goal file is output.txt 
For calling methods we need to mention one of following : bfs or dfs or dls or ids or ucs or greedy or a*
if no method is called an if condition is used to make a* as default method( we give python AI.py input.txt output.txt) 

If dump condition is not specified i have taken it as false which will only return required output variables.
If dump condition is specified , dump= true it will print required output variables and a trace file in which gives child nodes, cost ,depth , frindge , close set. 



for ex: to get bfs output , in command line we need to give as python AI.py input.txt output.txt bfs or if we need the dump file also we give as python AI.py input.txt output.txt bfs true





  

 
