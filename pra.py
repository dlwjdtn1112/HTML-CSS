

# arr = [list(map(int,input().split())) for _ in range(5)]

# for i in arr:
#     print(*i)
# arr1 = list(zip(*arr))
# for i in arr1:
#     print(*i)


l1 = [i for i in range(10)]

l1_sT = sorted(l1,reverse=True)
l1_sF = sorted(l1,reverse=False)
print(l1_sT)
print(l1_sF)

result = []

for i in range(3):
    l2 = list(map(int,input().split()))
    result.append(l2)

result1 = sorted(result,key=lambda x : x[0])
result2 = sorted(result,key=lambda x : x[1])

print(result1)
print(result2)

arr3 = [i for i in range(10)]
arr4 = [i for i in range(0,21,2)]
for i,j in zip(arr3,arr4):
    print(i,j)




    