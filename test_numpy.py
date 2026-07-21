import numpy as np
values = np.array([1,2,3,4,5,6])
values = np.arange(1,6)
print(values)

print(np.ones((1,5)))
print(np.eye(3))
values1 = np.array([1,2,3,4,6,6])
value2 = np.array([7,8,9,10,11,12])
print(values1+value2)
values1 = np.var(values1)
value1 = np.std(values1)
value1 = np.mode(values1)
print(values1)