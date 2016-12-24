N = int(input()) #Прост чтобы было
t = list(map(int, input().split()))

Ans = [0]
j = 0
for i in t:
    if i>0:
        Ans[j]+=1
    else:
        Ans.append(0)
        j +=1

print(max(Ans))
