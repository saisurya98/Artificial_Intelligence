SAI SURYA GORREPATI 
UTA ID -1002028664
email - sxg8664@mavs.uta.edu

python programming language is used for assignment 3.

Task1:
import the required libraries.
I have read the given text data as a numpy array and as a pandas data frame.

For variable B: True if there is a Baseball Game on TV, False if not
count the numbers of zero's and one's for B.
Probability for B is number of one's/(number of zero's + number of one's) because it is independent variable

The same is done for variable C for getting probability 

As variable G is a dependent variable on variable B , the probability of G dependents on value of B variable takes
P(G|B) =P(G,B)/ P(B) 
when B is false the probabilities of G | B is calculated and  notG|B.  
similarly probabilities are evaluated when B is true. 

The variable F is a dependent variable on what value variables G and C takes. Hence probability of F is dependent on G and C
P(F|G,C) =P(F,G,C)|P(G,C)
For different combinations of G,C what value probability of variable F is calculated. 

 On command prompt type python bnet.py input.txt, to see all probabilities values of different variables.

Task2 :
on command prompt type python bnet.py input.txt  Bt Gf Ct Ff to get the value of probability when variable B is true, G is false, C is true, F is false. 
Similarly we can get the value for any given innput of variables. A function P(B,G,C,F) is used to get probability value.
 

Task3:

On command prompt you can type python bnet.py input.txt Bt Gf Ct given Ff to get the probability of P(B=T, G=F, C=T, F=f)/P(F=f) 
A function inference_by_enumaration(B,G,C,F) is used to evaluate probability values here. Initially all query and evidence variables are set to none and depending on what value variable's
B,G, C, F takes the probabilities are calculated. 
Similarly we can get the value for any given input of variables whether or not evidence variables are present. 
