
For assignment 2 i have used python language

How the code is structed?

1) import required libraries.
2) Set the command line arguments for entering number of red and blue marbles. The player is set to computer by default and set 
   max depth to a set number.
3) On Computer turn, the program should use MinMax with Alpha Beta Pruning to determine the best move to make and perform the move.
   On Human turn, the program should use a prompt to get the move from the human user and perform the move.
   The program should alternate between these turns till the game ends (when the players run out of either red or blue marbles).
   Once the game ends, calculate who won and their final score and display it to the user.
   MinMax_AlphaBeta function is defined in code to use Min max algorithm with alpha beta pruning. 
4) For output: 
   If python red_blue_nim.py 2 3 is entered on terminal of python ; it takes computer turn as default , the no of red marble is 2 ,the blue marble is and based 
   on human turn input it return a score. 
   IF python red_blue_nim.py 2 3 human is entered on terminal of python; it takes human turn as default , the no of red marble is 2 and the blue marble is 3 and based 
   on human turn input it return a score.




If terminal state is reached before the given depth limit, score is computed based on number of red & blue marbles.

If the terminal state is not reached before the given depth limit, score of the current is calculate using below conditions:

Sum of red and blue marbles	Current node is 	Score would be
Even				Max player		-2
Even 				Min player		+2
Odd				Max player		+2
Odd				Min player		-2

For output: 
   IF python red_blue_nim.py 2 3  3 human is entered on terminal of python; it takes human turn as default , the no of red marble is 2 the blue marble is 3, depth limit is 3 and based 
   on human turn input it return a score.




