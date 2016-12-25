def dist(frm, to):
    """Расчитывает расстояние от frm до to"""
    if frm<=0 and to<=0:
        return(abs(frm+to))
    else:
        return(abs(frm-to))

N = int(input())
Inp = list(map(int, input().split()))

Ans = []
for i in Inp:
    Ans.append([])
    for j in Inp[0:i] + Inp[i+1:]:
        Ans[Inp.index(i)].append(dist(i,j))

for i in range(len(Ans)):
    Ans[i] = sum(Ans[i])

print(Ans.index(max(Ans)))
