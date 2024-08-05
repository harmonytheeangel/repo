import pandas as pd
import numpy as np
from numpy import *
arr_one = '1 2 3 4 5'
arr_two = [200 + x for x in range(5)]
#print(arr_two)
data = pd.DataFrame(np.random.randn(5 , 5) ,index=arr_one.split() , columns= 'x y z a b'.split()  )
print(data)

print("hello")

