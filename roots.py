func = input("enter function - ")
# ax^2+bx+c
# a = func.split('+')
forsquare = []
print (func)
for _ in func:
    forsquare = forsquare + [*_]
forsquare = forsquare + [""]
print (forsquare)
for i in range(len(forsquare)):
    if (forsquare[i].isalpha() == True) and (forsquare[i] == "^"):
        
    if forsquare[i] == "^":
        forsquare[i-2] = int(forsquare[i-2]) * int(forsquare[i+1])
        forsquare[i+1] = int(forsquare[i+1])-1        
        forsquare[i] = "**"
    # if (forsquare[i].isalpha()) and (forsquare[i+1].isalpha()) == True:
    #     print("hello")
            
print (forsquare)