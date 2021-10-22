import numpy as np

# get N, M as size of array or something similar
n, m = map(int, input().strip().split())

# read in a array with N rows as int
a = [np.array(input().strip().split(), int) for _ in range(n) ]

# reversed range  -- Designer Doormat
reversed(range(10))

#nested list comprehension
[[i,j,k] for i in range(x) for j in range(y) for k in range(z)]
