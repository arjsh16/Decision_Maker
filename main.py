
from random import *
n=int(input("what is the number of choices available: \n"))

opt_list=[]

i=0
while i<n:
    a=input()
    opt_list.append(a)

options_range=len(opt_list)
ind=randint(0,options_range)
print(f"Alright then this code chooses: {opt_list[ind]}")
