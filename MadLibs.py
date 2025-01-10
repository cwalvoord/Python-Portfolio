#Claudia Walvoord
#December 10, 2024
#Mad Libs

#Function
def bold_text(text):
    bold_start= '\033[1m'
    bold_end= '\033[0m'
    return bold_start + text + bold_end
def inputs():
    Animal = input("Please enter an animal: ")
    Animal.upper()
    Name = input("Please enter a name: ")
    Name.upper()
    Ing = input("Please enter an ing verb: ")
    Ing.upper()
    pronoun = input("Please enter a pronoun: ")
    pronoun.upper()
    Weird = input("Please enter a weird item: ")
    Weird.upper()
    Adj = input("Please enter an adjective: ")
    Adj.upper()
    print ("""There once was a little """ + bold_text(Animal) + """ named """ + bold_text(Name) + """ . """ + bold_text(Name) + """ was once """ + bold_text(Ing) + """ through a forest when """ + bold_text(pronoun) + """ discovered a """ + bold_text(Weird) + """! It turns out the """ + bold_text(Weird) + """ belonged to a """ + bold_text(Adj) + """ Troll! The Troll killed """ + bold_text(Name) + """. The End!
""")

#Main
inputs()
