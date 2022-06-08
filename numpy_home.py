import numpy as np

#print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

N_min = -(2**16)/2
N_max = (2**16)/2-1

#print(N_min, N_max) 

a = np.int8(-456)
#print(a)
#print(np.iinfo(a)) # min = -128 max = 127

arr = np.array([1,5,2,9,10])
print(arr.dtype) # int32