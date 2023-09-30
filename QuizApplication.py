import random
i=0
print("Welcome to Quiz Game!")
Name=str(input("What is your name?"))
print("ok,",Name, "Let's start the game.")

ans=input("Who wrote the play 'Romeo and Juliet'?")
if ans.lower()== "william shakespeare":
    print("correct")
    i=i+1
else:
    print("wrong")
ans= input(" Who painted the Mona Lisa?")
if ans.lower()== "leonardo da vinci":
    print("correct")
    i=i+1
else:
    print("wrong")
ans =input("Which planet is known as the 'Red Planet'?")
if ans.lower()== "mars":
    print("correct")
    i=i+1
else:
    print("wrong")
ans=input("What is the chemical symbol for gold?")
if ans.lower()== "au":
    print("correct")
    i=i+1
else:
    print("wrong")

ans = input("What is the capital of France?")
if ans.lower()== "paris":
    print("correct")
    i=i+1
else:
    print("wrong")
print("Your score is", i)
if i>=3:
    print("You are good at GK!")
else:
    print("Thank you!")
