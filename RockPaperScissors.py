#Claudia Walvoord
#1-6-25
#Rock Paper Scissors
#input
import random

#function
humanscore = 0
compscore = 0 #these are the score variables

def game():
    global humanscore #globalize
    global compscore
    print("Welcome to Rock Paper Scissors!!")
    print("Select either Rock, Paper, or Scissors!")
    while True: #makes it loop
        print("Your current score is " + str(humanscore) + " and the computers score is " + str(compscore))
        answer = input("Rock, Paper, or Scissors? or would you like to quit") #opening menu
        if answer == "Quit":
            print("Thank you for playing!")
            break #ends the loop
        comp = random.randint(1,3)
        if comp == 1 and answer == "Rock": #all of these if statements run all the possible combos
            print("It was a tie!")
            print("Computer chose Rock")
        if comp == 1 and answer == "Paper":
            print("Computer wins!")
            print("Computer chose Rock")
            compscore = compscore + 1
        if comp == 1 and answer == "Scissors":
            print("You win!")
            print("Computer chose Rock")
            humanscore = humanscore + 1
        if comp == 2 and answer == "Rock":
            print("Computer wins!")
            print("Computer chose Paper")
            compscore = compscore + 1
        if comp == 2 and answer == "Paper":
            print("It was a tie!")
            print("Computer chose Paper")
        if comp == 2 and answer == "Scissors":
            print("You win!")
            print("Computer chose Paper")
            humanscore = humanscore + 1
        if comp == 3 and answer == "Rock":
            print("You win!")
            print("Computer chose Scissors")
            humanscore = humanscore + 1
        if comp == 3 and answer == "Paper":
            print ("Computer wins!")
            print("Computer chose Scissors")
            compscore = compscore + 1
        if comp == 3 and answer == "Scissors":
            print ("It was a tie!")
            print("Computer chose Scissors")
#main
game()

