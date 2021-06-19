def bestsum(K, a):
    ans = [0]*10**5
    ans[0] = []

    for i in range(K):
        if ans[i] != 0:
            for j in a:
                combination = ans[i].copy()
                combination.append(j)
                if ans[i+j] == 0:
                    ans[i+j] = combination.copy()
                elif len(combination) < len(ans[i+j]):
                    ans[i+j] = combination.copy()
    
    return ans[K]

a = [5, 3, 4, 7]
print(bestsum(11,a))