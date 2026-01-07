import pandas as pd
import numpy as np
from PIL import Image
path ="/Users/adityanegi/Downloads/PFp.jpeg"
img_array = np.array(Image.open(path))
s = pd.Series([img_array])
print(s)
t = input("Enter the address:")
cont = np.array(Image.open(t))
t = pd.Series([cont])
if s == t :
    print("true")
else :
     print("false")






'''
 X = [1,2,3,4,5]
s1 = pd.Series(X)
print (s1)
array_s1 = image_series.map()'''
