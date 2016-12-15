Input = open("Input.txt", "r")

Ans = []

for i in (Input.read()).split("\n"):
    if (eval(i.replace("(", "").replace(")", "")) == eval(i)) == True:
        Ans.append(1)
    else:
        Ans.append(0)
    print(1)
Input.close()
    
print (Ans)

Output = open("Output.txt", "w")

for i in Ans:
    Output.write(str(i)+"\n")
Output.close()
