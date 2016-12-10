Inp = list(map(int, input().split()))
M, N = Inp[0], Inp[1]

Inp = []
[Inp.append( list( map(int, input().split())) ) for i in range(N)]

IN = []
OUT = []
for i in range(N):
    IN.append(Inp[i][0])
    OUT.append(Inp[i][1])

S = []
[S.append([ [0,0,0],[0,0,0] ]) for i in range(20)]

ans = []
def pass_app(m):
    for i in range(20):
        for j in range(2):
            for x in range(3):
                if S[i][j][x] == 0:
                    S[i][j][x] = 1
                    if j == 0:
                        ans.append(i*6 + x + 1)
                    else:
                        ans.append(i*6 + j*6 - x )
                    IN[m] = (i,j,x)
                    return 0

for i in range(1, M+1):
    if i in OUT:
        for x in range(N):
            if i == OUT[x]:
                S [IN[x][0]] [IN[x][1]] [IN[x][2]] = 0
    if i in IN:
        for x in range(N):
            if i == IN[x]:
                pass_app(x)
    
[print(i) for i in ans]
