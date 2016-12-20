""" Пишу ебучими функциями, прям как ООП, только это блеать олимпиада...
ну ахуеть теперь """

    
def addNewDate(m,d):
    """ Ну если не судьба с уже существующей датой - добавим новый эллемент. Вход - месяц и день """
    if not (m in dates):
        dates.update({m:{}})
    dates[m].update({d:[0,0]})


def addWeather(m,d,w):
    if not (m in dates and d in dates[m]):
       addNewDate(m,d)
    if w is "S":
        W = 0
    elif w is "N":
        W = 1
    dates[m][d][W] += 1


def scanDate(s):
    if '.' in s:
        S = s[:-2].split('.')
        w = s[-1]
        d = int(S[0])
        m = int(S[1])
        
    elif '-' in s:
        S = s[:-2].split('-')
        w = s[-1]
        d = int(S[2])
        m = int(S[1])
        
    elif '/' in s:
        S = s[:-2].split('/')
        w = s[-1]
        d = int(S[1])
        m = int(S[0])
        
    return(m,d,w)


def main(s):
    Arr = scanDate(s)
    m, d, w = Arr[0], Arr[1], Arr[2]
    addWeather(m,d,w)


dates = {}
"""
Формат данных:
    {Месяц: {День:[S,N],...}, ... }
"""



Input = open("Input.txt")
data = (Input.read()).split("\n")
Input.close()

for i in data:
    main(i)




Output = open("Output.txt", "w")
l = list(dates.keys())
l.sort()

for m in l:
    L = list(dates[m].keys())
    L.sort()
    for d in L:
        S = str(m) + ' ' + str(d) + ' ' + str(dates[m][d][0]) + ' ' + str(dates[m][d][1]) + '\n'
        Output.write(S)
        print(S[:-2])
Output.close()

#print(dates)
