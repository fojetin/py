Input = input()
N = int(Input.split()[0])
M = int(Input.split()[1])

bils = []
for i in range(M):
    bils.append(input())

conds = [0]*N
for i in bils:
    if i.count('+') is 1:
        conds[i.index('+')] += 1

Ans = []
for i in range(N):
    if 100/sum(conds)*conds[i] >= sum(conds)/100*7:
        Ans.append(i+1)

print(' '.join(list(map(str, Ans))))
