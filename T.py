import pandas as pd
import numpy as np
from PIL import Image
path ="/Users/adityanegi/Downloads/PFp.jpeg"
img_array = np.array(Image.open(path))
s = pd.Series([img_array])
print(s)
'''
 X = [1,2,3,4,5]
s1 = pd.Series(X)
print (s1)
array_s1 = image_series.map()'''
