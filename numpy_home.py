import numpy as np

#print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

N_min = -(2**16)/2
N_max = (2**16)/2-1

#print(N_min, N_max)

a = np.uint8(25)
print(a)
print(np.iinfo(a))