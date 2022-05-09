#// File Name: Not-Enough-Lifeboats.py
#// Mission Name: Not Enough Lifeboats!
#// Description: N/A
#// Credits: Alex

ExplorationPyFile = 1.1
Name = "Not Enough Lifeboats!"
AuthorS = "Alex"
Description = """
Survive the Titanic's maiden voyage as a theif, try to act normal to avoid suspicion.
Every time you disobey an order, or act weirdly your suspicion rate raises. If this gets
too high you will risk being exposed.
14/02/2022
"""
import webbrowser
def unalive():
    print("you a dead boy")
    webbrowser.open("https://upload.wikimedia.org/wikipedia/en/8/8a/Dancing_Pallbearers.jpg")
    exit()


global time, random
try:
    import time, random
except Exception as Exc:
    print("ERROR 006 ('README.txt')")
    input()
    exit()

def Game(API):
    # > Game Globals <
    SCORE = 0
    SUS = 0
    Inventory = []
    
    # > Intro < #
    API.write("* It's the 13th of April, the sea is clear and you are on the deck of the Titanic. *",0.02)
    time.sleep(1)
    API.write("* The ship is divided from upper class to lower class, your purpose here is to steal the jewel from an upper class passenger", 0.01)
    time.sleep(1)
    API.say("Go to your quarters.")
    time.sleep(1)
    print("Welcome to your quarters!")
    Choice = API.menu([
        "I'm tired, go to sleep.",
        "Look out of the window, I wonder what the sea's like?"
    ])
    if Choice == "Look out of the window, I wonder what the sea's like?":
        API.write("The sea's starting to pick up, the waves are almost up to my window.",0.03)
        time.sleep(1)
        API.say("I should sleep now.")
    time.sleep(0.25)
    API.write("* As the sun sets, you drift to sleep *",0.03)
    
    # > Day 1 < #
    print("-----------------------")
    time.sleep(1.5)
    print("""
TIME: Morning
DAY: Unknown, Hungover
LOCATION: Titanic
    """)
    API.say("Great, another morning on this floating mission camp.")
    API.say("I should go have breakfast while you still can.")
    
    
    API.write("What should I take with me?",0.03)
    Choices = [
    "Steyr M1912 pistol",
    "Mirror",
    "Watch",
    "Nothing- It's just breakfast"
    ]
    ## Run through the options till non left.
    while True:
        X = API.menu(Choices)
        if Choices.index(X) == len(Choices)-1:
            break
        Inventory.append(X)
        Choices[len(Choices)-1] = "Done, let's go."
        Choices.remove(X)
    API.write("* You head to get breakfast. *",0.02)
    print("- Your Coat Pockets")
    for i in Inventory:
        print(i)
        time.sleep(0.5)
    time.sleep(1)
    
    # > 
    API.write("!! On the way to breakfast, you see a target. !!",0.02)
    API.write("( He's wearing a gold ring. )",0.01)
    X = API.menu([
        "I should take the chance, there's no one here. I could steal it, risky though.",
        "No, to soon."
    ])
    if X == "No, to soon.":
        SCORE = SCORE - 1
    else:
        SCORE = SCORE + 1
        # 7 IN 10 CHANCE OF BEING SUCCESSFUL
        API.say("Hey! You.")
        API.say("Give me that.")
        Upper = 4
        if "Steyr M1912 pistol" in Inventory:
            Upper = Upper+3
        Successful = (random.randint(1,10) <= Upper)
        if Successful:
            SCORE = SCORE+3
            SUS = SUS+1
            API.write("+ Success. +",0.05)
            Inventory.append("Gold Ring")
            if "Steyr M1912 pistol" in Inventory:
                API.write("# Your M1912 gave you an extra 30% chance.",0.03)
        else:
            SCORE = SCORE-2
            SUS = SUS+2
            API.write("- Failure. +",0.05)
            if not ("Steyr M1912 pistol" in Inventory):
                API.write("# You didn't bring your M1912, this made it 30% less likely to succeed.",0.05)
            else:
                API.write("# It was hard, your M1912 gave you an extra 30% chance but you still failed.",0.05)
    # > Summary < #
    print("- Current Score\n"+str(SCORE)+"\n- Current Suspicion\n"+str(SUS)+"\n- Your Coat Pockets")
    for i in Inventory:
        print(i)
        time.sleep(0.5)
        
    # > Go To Breakfast < #
    time.sleep(2)
    API.write("* You go to breakfast *",0.03)
    time.sleep(0.5)
    print("-- SIDE NOTE\nYou must try to act as normal as possible, guards will arrest you if you are too suspicious.\nRemember this throughout the game.")
    API.say("Continue")
    API.write("Your at breakfast, what should you eat/drink?",0.03)
    Choices = {
        "Cream of Wheat": 2,
        "Hash": 1,
        "Milk": 1,
        "Wine": 3,
        "Gin": 4,
        "Pancakes": -1,
        "Crepes": -1,
        "Toast": 1,
        "Brandy": 5,
        "Beer": 5,
        "Bacon": 1,
        "One-Eyed Jack": 2,
        "Coffee": -1,
        "Tea": -2,
        "Orange Juice": 0,
        "Croissants": -2,
        "Weetabix": 1,
        "Spam N Egg": -1,
        "Crumpets": 1,
        "Sausages": 0,
        "Whisky": 5,
        "Vodka": 6
    }
    CA = Choices.keys()
    CA = list(CA)
    CA.append("Nothing, I'll just sit.")
    ## Run through the options till non left.
    while True:
        X = API.menu(CA)
        if CA.index(X) == len(CA)-1:
            break
        CA[len(CA)-1] = "Okay, I'm ready to leave now."
        CA.remove(X)
        SUS = SUS+Choices[X]
        print(f'You had your {X}.')