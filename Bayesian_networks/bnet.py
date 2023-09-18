import pandas as pd
import numpy as np
import sys
pd.set_option('display.max_columns', None)
Input_Data = np.genfromtxt(sys.argv[1], dtype=int, encoding=None, skip_footer=0)
# print(Input_Data)
# print(len(Input_Data))
panda_df = pd.DataFrame(data = Input_Data,columns = ["B","G", "C","F"])
# print(type(panda_df['B'][0]))

###### TASK 1#######################################################################################################################
count_zero = (panda_df['B'] == 0).sum()
count_one=(panda_df['B'] == 1).sum()
Basketball_game_on_TV= count_one/(count_one+count_zero)
Not_Basketball_game_on_TV= 1-Basketball_game_on_TV
data = {'Basketball_game_on_TV': [Basketball_game_on_TV],
        'Not_Basketball_game_on_TV': [Not_Basketball_game_on_TV]}
  
df = pd.DataFrame(data, index=['P(Basketball_game_on_TV)'])
print(df)
print('\n')


count_zero = (panda_df['C'] == 0).sum()
count_one=(panda_df['C'] == 1).sum()
out_of_cat_food= count_one/(count_one+count_zero)
not_out_of_cat_food= 1-out_of_cat_food
# print(out_of_cat_food,not_out_of_cat_food)
data = {'out_of_cat_food': [out_of_cat_food],
        'not_out_of_cat_food': [not_out_of_cat_food]}
  
df = pd.DataFrame(data, index=['P(out_of_cat_food)'])
print(df)
print('\n')

# count=(panda_df['B','C']==1).sum()
c=0
for i in Input_Data:
    if i[0]==1 and i[1]==1:
        c=c+1
P_B_G= c/len(Input_Data)
prob_Basketball_game_on_TV_george_watches_tv=P_B_G/Basketball_game_on_TV
prob_Basketball_game_on_TV_not_george_watches_tv=1-prob_Basketball_game_on_TV_george_watches_tv
# print(prob_Basketball_game_on_TV_george_watches_tv,prob_Basketball_game_on_TV_not_george_watches_tv)

c1=0
for i in Input_Data:
    if i[0]==0 and i[1]==0:
        c1=c1+1
P_BF_GF=c1/len(Input_Data)
prob_not_Basketball_game_on_TV_not_george_watches_tv=P_BF_GF/Not_Basketball_game_on_TV
prob_not_Basketball_game_on_TV_george_watches_tv=1-prob_not_Basketball_game_on_TV_not_george_watches_tv
# print(prob_not_Basketball_game_on_TV_george_watches_tv,prob_not_Basketball_game_on_TV_not_george_watches_tv)

data = {'P(baseball_game_on_TV)':['T','F'],'P(george_watches_tv|baseball_game_on_TV)': [prob_Basketball_game_on_TV_george_watches_tv,prob_not_Basketball_game_on_TV_george_watches_tv],'P(not george_watches_tv|baseball_game_on_TV)': [prob_Basketball_game_on_TV_not_george_watches_tv,prob_not_Basketball_game_on_TV_not_george_watches_tv]
        }  
df = pd.DataFrame(data)
print(df)
print('\n')

c2=0
for i in Input_Data:
    if i[1]==1 and i[2]==1 and i[3]==1:
        c2=c2+1
GT_CT_FT= c2/len(Input_Data)
c3=0
for i in Input_Data:
    if i[1]==1 and i[2]==1 :
        c3=c3+1
GT_CT=c3/len(Input_Data)

GT_CT_FT=GT_CT_FT/GT_CT
GT_CT_FF=1-GT_CT_FT
# print(GT_CT_FT,GT_CT_FF)


c4=0
for i in Input_Data:
    if i[1]==1 and i[2]==0 and i[3]==1:
        c4=c4+1
GT_CF_FT= c4/len(Input_Data)
c5=0
for i in Input_Data:
    if i[1]==1 and i[2]==0 :
        c5=c5+1
GT_CF=c5/len(Input_Data)

GT_CF_FT=GT_CF_FT/GT_CF
GT_CF_FF=1-GT_CF_FT
# print(GT_CF_FT,GT_CF_FF)

c6=0
for i in Input_Data:
    if i[1]==0 and i[2]==1 and i[3]==1:
        c6=c6+1
GF_CT_FT= c6/len(Input_Data)
c7=0
for i in Input_Data:
    if i[1]==0 and i[2]==1 :
        c7=c7+1
GF_CT=c7/len(Input_Data)
GF_CT_FT=GF_CT_FT/GF_CT
GF_CT_FF=1-GF_CT_FT
# print(GF_CT_FT,GF_CT_FF)

c8=0
for i in Input_Data:
    if i[1]==0 and i[2]==0 and i[3]==1:
        c8=c8+1
GF_CF_FT= c8/len(Input_Data)
c9=0
for i in Input_Data:
    if i[1]==0 and i[2]==0 :
        c9=c9+1
GF_CF=c9/len(Input_Data)
GF_CF_FT=GF_CF_FT/GF_CF
GF_CF_FF=1-GF_CF_FT
# print(GF_CF_FT,GF_CT_FF)

data = {'P(george_watches_tv)':['T','T','F','F'],
        'P(out_of_cat_food)':['T','F','T','F'],
        'P(george_feeds_cat|george_watches_tv,out_of_cat_food)': [GT_CT_FT,GT_CF_FT,GF_CT_FT,GF_CF_FT],
        'P(not george_feeds_cat|george_watches_tv,out_of_cat_food)': [GT_CT_FF,GT_CF_FF,GF_CT_FF,GF_CF_FF]
        }

df = pd.DataFrame(data)

print(df)
print('\n')


############################## TASK2 ##############################################################################################




def P(B,G,C,F):
    multiplication_factor=1
    if B=='t':
        multiplication_factor=multiplication_factor* Basketball_game_on_TV
    else:
        multiplication_factor=multiplication_factor* Not_Basketball_game_on_TV
    if C=='t':
        multiplication_factor=multiplication_factor* out_of_cat_food
    else:
        multiplication_factor=multiplication_factor*not_out_of_cat_food
    if B=='t':
        if G=='t':
            multiplication_factor=multiplication_factor*prob_Basketball_game_on_TV_george_watches_tv
        else:
            multiplication_factor=multiplication_factor*prob_Basketball_game_on_TV_not_george_watches_tv
    else:
        if G=='t':
            multiplication_factor=multiplication_factor*prob_not_Basketball_game_on_TV_george_watches_tv
        else:
            multiplication_factor=multiplication_factor*prob_not_Basketball_game_on_TV_not_george_watches_tv
    if G=='t':
        if C=='t':
            if F=='t':
                multiplication_factor=multiplication_factor*GT_CT_FT
            else:
                multiplication_factor=multiplication_factor*GT_CT_FF
        else:
            if F=='t':
                multiplication_factor=multiplication_factor*GT_CF_FT
            else:
                multiplication_factor=multiplication_factor*GT_CF_FF
    else:
        if C=='t':
            if F=='t':
                multiplication_factor=multiplication_factor*GF_CT_FT
            else:
                multiplication_factor=multiplication_factor*GF_CT_FF
        else:
            if F=='t':
                multiplication_factor=multiplication_factor*GF_CF_FT
            else:
                multiplication_factor=multiplication_factor*GF_CF_FF
    return multiplication_factor


# print(P('t','f','t','f') )   
################################## TASK3########################################################################################### 

def inference_by_enumaration(B, G, C, F):
    sum = 0
    for i in ['t', 'f']:
        for j in ['t', 'f']:
            for k in ['t', 'f']:
                for l in ['t', 'f']:
                    if (i==B or B==None) and (j==G or G==None) and (k==C or C==None) and (l==F or F==None):
                        sum = sum+P(i, j, k, l)
                        # print(i, j, k, l)
                        # get diff combination
                    
    return sum
# print(inference_by_enumaration(None,None,None,'f'))


from textwrap import wrap
s = 'Bf'
s1=wrap(s,1)
query_B,query_G,query_C,query_F,evidence_B,evidence_G,evidence_C,evidence_F=None,None,None,None,None,None,None,None
evidence= False
for i in range(2,len(sys.argv)):
    s1=wrap(sys.argv[i],1)
    if sys.argv[i]=='given':
        evidence=True
    elif s1[0]=='B':
        if evidence==True:
            evidence_B=s1[1]
            query_B=s1[1]
        else: 
            query_B=s1[1]
    elif s1[0]=='G':
        if evidence==True:
            evidence_G=s1[1]
            query_G=s1[1]
        else: 
            query_G=s1[1]
    elif s1[0]=='C':
        if evidence==True:
            evidence_C=s1[1]
            query_C=s1[1]
        else: 
            query_C=s1[1]
    elif s1[0]=='F':
        if evidence==True:
            evidence_F=s1[1]
            query_F=s1[1]
        else: 
            query_F=s1[1]

# print(query_B,query_G,query_C,query_F,evidence_B,evidence_G,evidence_C,evidence_F)   

if evidence == True:
    num=inference_by_enumaration(query_B,query_G,query_C,query_F)
    den=inference_by_enumaration(evidence_B,evidence_G,evidence_C,evidence_F)
    print('when evidence variables are present the probability is:',num/den)
else:
    print('when no evidence variables are present the probility is:',inference_by_enumaration(query_B,query_G,query_C,query_F))
