#Claudia Walvoord
#January 8, 2025
#Multiplication Quiz

#import
import random
score = 0
import time

#function
def quiz():
    global score #importanttttttttttttt
    print("Hello! Welcome to the multiplication quiz!")
    start_time=time.time() #starts timer
    while True: #makes it infinity (untill break)
        questions = int(input("How many questions would you like to have?"))
        diff = input("Would you like your difficulity to be Easy, Medium, or Hard?") #extra credit yay!!
        for i in range (questions):
            num1 = random.randint(0,10) #picks 2 numbers, depending on difficulity of questions
            num2 = random.randint(0,10)
            num3= random.randint(0,100)
            num4= random.randint(0,100)
            num5= random.randint(-100,100)
            num6= random.randint(-100,100)
            if diff == "Easy": #code if you pick easy
                answer = int(input("What is " + str(num1) + "x" + str(num2) +"?"))
                poop = num1 * num2
                if answer == num1*num2:
                    print("That is correct! The answer is " + str(answer) + "!")
                    score = score + 1
                    print("Your score is " + str(score))
                else:
                    print("That is incorrect. The correct answer is " + str(poop))
                    print("Your score is " + str(score))
            if diff == "Medium": #medium questions code
                answerr = int(input("What is " + str(num3) + "x" + str(num4) +"?"))
                poopp = num3 * num4
                if answerr == num3*num4:
                    print("That is correct! The answer is " + str(answerr) + "!")
                    score = score + 1
                    print("Your score is " + str(score))
                else:
                    print("That is incorrect. The correct answer is " + str(poopp))
                    print("Your score is " + str(score))
            if diff == "Hard": #hard questions
                aanswer = int(input("What is " + str(num5) + "x" + str(num6) +"?"))
                ppoop = num5 * num6
                if aanswer == num5*num6:
                    print("That is correct! The answer is " + str(aanswer) + "!")
                    score = score + 1
                    print("Your score is " + str(score))
                else:
                    print("That is incorrect. The correct answer is " + str(ppoop))
                    print("Your score is " + str(score))

        quit = input("Would you like to quit?")
        if quit == "Yes":
            end_time=time.time() #ends the timer
            elapsed_time = end_time - start_time
            print("Thank you for playing! Your score was " + str(score) +" and your time was " +str(elapsed_time) +" seconds!")
            break #breaks the code


#main
quiz()
