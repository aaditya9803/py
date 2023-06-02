func = input("enter function - ") # ax^2+bx+c
func = [*func] + ['']

def splitter(the_func):
    splitted = the_func.split('+')
    return splitter
    
def replacer(the_func): #Removes Spaces
    clear_func =[]
    i = 0
    # if the_func[i] == 'x':
    #     the_func_1 = ['1'] + [the_func]
         
    for i in range(len(the_func)):
        if the_func[i] != chr(32):
            clear_func = clear_func + [the_func[i]]
        
    return clear_func

def derivative(the_func): 
    i = 0
    for i in range(len(the_func)):
        if the_func[i] == "^":
            the_func[i-2] = int(the_func[i-2]) * int(the_func[i+1])
            the_func[i+1] = int(the_func[i+1])-1
    return the_func
        


print(derivative(replacer(func)))

