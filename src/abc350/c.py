"""

"""
import numpy as np

N = int(input())
A = list(map(int, input().split()))

result = ''
for n in range(1, int(N/2 + 0.5)):
    a = A[n-1]
    if n != a:
        obj_idx = A.index(n)
        A[n-1] = A[obj_idx]
        A[obj_idx] = a
        result += f'{n} {obj_idx + 1}\n'
print(result)
