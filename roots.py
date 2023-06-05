def splitter(the_func):
    expression = []
    i = 0
    for_plus = the_func.split('+')
    for i in range(len(for_plus)):
        expression = expression + for_plus[i].split('-')
    if expression[0] == '':
        expression.pop(0)
    the_func = [*the_func]
    if the_func[0] != '-':
        symbols = ['']
    else:
        symbols =[]
    for _ in the_func:
        if _ == '+' or _ == '-':
            symbols = symbols + [_]
    return expression, symbols


def replacer(the_func, remove_square = False): #Removes Spaces
    the_func = [*the_func]
    clear_func =[]
    if remove_square == False:
        for char in the_func:
            if char != chr(32):
                clear_func = clear_func + [char]
        clear_func = ''.join(clear_func)
    if remove_square == True:
        for i in range(len(the_func)):
            if the_func[i]== '^':
                the_func[i] = '**'
        clear_func = ''.join(the_func)
    return clear_func


def derivative(the_func):
    if_x = the_func
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
                if if_x == 'x':
                    expression = ['1']
                else:
                    expression = [*the_func]
                    expression.remove('x')
                return expression


def final_derivative(the_func):
    the_func = replacer(the_func)
    expression, plusminus = splitter(the_func)
    i = 0
    differentiation = []
    for i in range(len(expression)):
        differentiation = differentiation + [plusminus[i]]+ derivative(expression[i])
    if differentiation[0] == '':
        differentiation.pop(0)
    differentiation = replacer(''.join(differentiation), True)
    return differentiation

def add_multiplier(the_func):
    the_func = [*the_func]
    for i in range(len(the_func)):
        if the_func[i] == 'x':
            if i==0 and the_func[0] == 'x' or (the_func[i-1] =='+' or the_func[i-1] =='-'):
                continue
            else:
                the_func[i] = '*x'
    return ''.join(the_func)



print("Give the EQUATION in the form of ---->   ax^2 + bx + c")
func = input("enter function - ") # ax^2+bx+c
equation = add_multiplier(replacer(replacer(func), True))
derivation = add_multiplier(final_derivative(func))

# print(equation)
# print(derivation)

x=0.01
print ("{} ------ is the initial value of x".format(x))
while True:
    b = x
    try:
        x = x - eval(equation)/eval(derivation)
        print (x)
    except:
        print("Something looks wrong check given equation")

    if str(b)[:7] == str(x)[:7]:
        print ("{:.4f} ------ is the Root of this equation".format(x))
        break