import random
comp=random.randint(1,100)
num=-1
guess=0
while(num!=comp):
    guess=guess+1
    num=int(input("Guess the number\n"))
    if(num>comp):
        print("Try a lower number")
    elif(num<comp):
        print("Try a bigger number")

print("You guessed it right, the number is:",num)
print("Number of guesses: ",guess)
