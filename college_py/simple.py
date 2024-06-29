def solve(arr1, arr2, n1, n2):
    i1, i2 = 0, 0
    ans = []
    while i1 < n1 and i2 < n2:
        if arr1[i1] > arr2[i2]:
            ans.append(arr2[i2])
            i2 += 1
        else:
            ans.append(arr1[i1])
            i1 += 1
    while i1 < n1:
        ans.append(arr1[i1])
        i1 += 1
    while i2 < n2:
        ans.append(arr2[i2])
        i2 += 1
    return ans


n1, n2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(*solve(arr1, arr2, n1, n2))
