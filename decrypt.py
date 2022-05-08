alphabets = []
# 97 to 122
for i in range (97,123):
    alphabets.append(chr(i))
    en_word=""
word = str(input ("enter word to enc/dec  "))
num = int(input("enter the number u want to shift "))
def encrypt(word,num):
    en_word=""
    endc = str(input ("encrpyt or decrypt ? (e/d)"))
    for i in range (0, len(word)):
        letter = word[i:i+1]
        if endc == "e":
            position = int(alphabets.index(letter) + num)
        elif endc == "d":
            position = int(alphabets.index(letter) - num)
        else:
            print ("enter e/d")
        en_word = en_word + alphabets[position]
            
    print (en_word)
    
encrypt(word,num)
input()