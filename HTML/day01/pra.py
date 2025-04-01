from collections import deque


d1 = deque(maxlen=10)

for i in range(10):
    d1.append(i)

print(d1)
d1.append(0)
print(d1)
print("="*10)
d1.append(0)
print(d1)

from itertools import combinations,permutations

l1 = [i for i in range(10)]

l1_c = list(permutations(l1,4))

for i in l1_c:
    print(*i)





    