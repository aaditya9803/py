func ="-3x^2"
def differentation(the_func):
    i =0
    if the_func.isdigit() == True:
        return [i]
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
                               
print (differentation(func))




# for ii in range(len(the_func)):
#                     if the_func[ii] == 'x':
#                         a = the_func[ii+1:]
#                         return a
#                     # return "hello"
                    