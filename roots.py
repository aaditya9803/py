def splitter(the_func):
    expression = []
    i = 0
    symbols = ['']
    for_plus = the_func.split('+')
    # for for_minus in for_plus:
    #     if for_plus[i] != '-':
    #         expression = expression + for_minus.split('-')
    #     elif for_plus[i] == '-':
    #         for_plus[i+1] = '-' + for_plus[i+1]
    #     i += 1
    the_func = [*the_func]
    for _ in the_func:
        if _ == '+' or _ == '-':
            symbols = symbols + [_]            
    return expression, symbols
    
def replacer(the_func): #Removes Spaces
    clear_func =[]
    i = 0
    for i in range(len(the_func)):
        if the_func[i] != chr(32):
            clear_func = clear_func + [the_func[i]] 
    return clear_func



def derivative(the_func):
    i =0
    if the_func.isdigit() == True:
        return [str(i)]
    else:
        the_func = [*the_func]
        for i in range(len(the_func)):
            if '^' in the_func:
                if i==0 and the_func[i] == 'x':
                    square = ''.join(the_func[i+2:])
                    square = int(square) - 1
                    square = str(square)
                    a = the_func[i+2:]
                    expression = a + ['x'] + ['^'] + [*square]
                    return expression
                else:
                    if the_func[i] == '^':
                        square = ''.join(the_func[i+1:])
                        square = int(square)
                        a = ''.join(the_func[:i-1])
                        a = int(a) * square
                        square = square - 1
                        expression = [*str(a)] + ['x'] + ['^'] + [*str(square)]
                        return expression
                        
            elif '^' not in the_func:
                expression = [*the_func]
                expression.remove('x')
                return expression
        



func = input("enter function - ") # ax^2+bx+c

expression, plusminus = splitter(func)
# i = 0
# differentiation = []
# for i in range(len(expression)):
#     differentiation = differentiation + [plusminus[i]] + derivative(expression[i])
#     print (''.join(differentiation))

print(expression)