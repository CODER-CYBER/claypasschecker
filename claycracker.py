from random import *
Guess=""
password=input("password? ")
letters = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]
while(Guess !=password):
    Guess=""
    for letter in password:
        Guessletter=letters[randint(0,25)]
        Guess=str(Guessletter) + str(Guess)
        print(Guess)
        print("password cracked |!")
