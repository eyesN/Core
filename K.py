import pandas as pd 
s1 = pd.Series('1,2,3,4,5')
print(s1) 
s2 = pd.Series('1,2,3,4,5')
if s1.equals(s2) :
    print("true set")
   
elif not s1.equals(s2) :
    print("improper set")
else :
    print("no set ")
