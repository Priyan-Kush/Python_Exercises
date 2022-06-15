#7
from functools import reduce

def find_mean(list):
    return reduce(lambda x,y:x+y,list)/len(list)

def find_std_dev(list):
    mean=find_mean(list)
    return (reduce(lambda x,y:x+((y-mean)**2),list)/len(list))**0.5


players_1=[22,72,0,21,58]
players_2=[92,89,9,44,16]

x=find_std_dev(players_1)
y=find_std_dev(players_2)

if(x>y):
    print('b')
else:
    print('a')
