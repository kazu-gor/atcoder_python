import numpy as np

N = int(input())
A = list(map(int, input().split()))
A_arr = np.array(A)

count = 0
while 1:
    if np.sum(A_arr % 2) == 0:
        A_arr = A_arr / 2
        count += 1
    else:
        print(count)
        break
