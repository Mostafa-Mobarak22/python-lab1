# _______________ (1)____________

bill = 47.28
service = 0.15
print(f"Each person needs to pay: {(bill+bill*service)/2}")

# ____________________________________________________________

# _______________________(2)________

num1=input("Enter first number ")
num2=input("Enter second number ")
if(num1.isdecimal() and num2.isdecimal() and int(num2)!=0):
    print(int(num1)/int(num2))
else:
    print('not valid numbers')

# ______________________________________________________________

# _____________________ (3)_____________

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "{}"
word6 = "so"
word7 = "far?"
sentence=f"{word1} {word2} {word3} {word4} {word5} {word6} {word7}"
print(sentence)

# ___________________________________________________________________

# ___________(4)____________________

newword=word7.replace('?','!')
print(newword)
print(sentence.format('python'))

# ______________________________________________________________________

# ________________(5)_________________

statment=input("Enter stetmant ")
print(len(statment))

# _____________________________________

# __________________(6)_____________________

num1=input("Enter first number ")
num2=input("Enter second number ")
operator=input('Enter operator + , - , * , / ')

if(num1.isdecimal() and num2.isdecimal()):
    if(operator=='+'):
        print(int(num1)+int(num2))
    elif(operator=='-'):
        print(int(num1)-int(num2))
    elif(operator=='*'):
        print(int(num1)*int(num2))
    elif(operator=='/' and int(num2)!=0):
        print(int(num1)/int(num2))
    else:
        print('not divide on zero')
else:
    print('not valid numbers')

