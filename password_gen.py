import random
letter = input ("enter number of letters(abc = 3)")
cap_letter = input ("enter number of cap-letters(ABCD= 4)")
number = input ("enter number of numbers")
symbol = input ("enter number of symbols")
sym1 = sym2 = lett1 = lett2 = num1 = 0
symbol1= []
a = []
letter1=[]
number1=[]
cap_letter1=[]
for sym1 in range(32, 48):
    symbol1.append(chr(sym1))
for sym2 in range(58, 65):
    symbol1.append(chr(sym2))
for lett1 in range(97, 123):
    letter1.append(chr(lett1))
for lett2 in range(65, 91):
    cap_letter1.append(chr(lett2))
for num1 in range(48, 58):
    number1.append(chr(num1))
# print ("here\n {} \n {} \n {} \n {}".format(symbol1, letter1, cap_letter1, number1))

letters = random.choices(letter1, k=int(letter))
symbols = random.choices(symbol1, k = int(symbol))
numbers = random.choices(number1, k = int(number))
cap_letters = random.choices(cap_letter1, k = int(cap_letter))
a = letters + symbols + numbers + cap_letters
random.shuffle(a) 
b = ''.join(a)
print (b)