#Claudia Walvoord, pd 4
#October 17th
#Spirit Animal Generator

print("Welcome to the Spirit Animal Generator!!")
print("Answer the questions to discover your Spirit Animal!")
ans = input ("Stay in or Go out?")
if ans == "Stay in":
    ans = input ("Burgers or Pizza?")
    if ans== "Burgers":
        ans = input("Beach or Moutian?")
        if ans=="Beach":
            print("Your Spirit Animal is a Frog!")
        else:
            print("Your Spirit Animal is a Turtle!")
    elif ans== "Pizza":
        ans = input ("Skydiving or Scubadiving?")
        if ans == "Skydiving":
            print("Your Spirit Animal is a Giraffe!")
        else:
            print("Your Spirit Animal is a Octpus!")
elif ans == "Go out":
    ans = input ("Savory or Sweet?")
    if ans == "Savory":
        ans = input ("Low energy or High energy?")
        if ans == "Low energy":
            print("Your Spirit Animal is a Tiger!")
        else:
            print("Your Spirit Animal is a Bunny!")
    elif ans == "Sweet":
        ans = input("Rain Forest or Big City?")
        if ans == "Rain Forest":
            print("Your Spirit Animal is a Parrot!")
        else:
            print("Your Spirit Animal is a Snail!")
