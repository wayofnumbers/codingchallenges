import numpy as np

# get N, M as size of array or something similar
n, m = map(int, input().strip().split())

# read in a array with N rows as int
a = [np.array(input().strip().split(), int) for _ in range(n) ]

# reversed range  -- Designer Doormat
reversed(range(10))

#nested list comprehension
[[i,j,k] for i in range(x) for j in range(y) for k in range(z)]

# set input boilerplate
N_e = int(input())
e = set(map(int, input().split()))
N_f = int(input())
f = set(map(int, input().split()))

### Set Mutations ###
_,A=input(),set(map(int,input().split()))
for i in range(int(input())):
    op,_=input().split()
    B=set(map(int,input().split()))
    eval("A."+op+"(B)")   # use 'eval', less safe, slower than 'getattr'
print(sum(A))    

if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)   # use 'getattr'
print (sum(A))


# use all() and any() to do list condition cases


