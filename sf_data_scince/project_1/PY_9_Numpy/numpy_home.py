import numpy as np

arr = np.linspace(1, 2, 6)

nd_array = np.linspace(0, 6, 12, endpoint=False).reshape(3,4)

data = np.array([4, 9, -4, 3])
roots = np.sqrt(data)
print(roots)

simplelist = [19, 242, 14, 152, 142, 1000]
print(np.mean(simplelist))