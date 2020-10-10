import random#Rock paper scissor
def gameWin(comp, you):
    # declare a tie!
    if comp == you:
        return None    # when computer chose rock
    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    
    # when computer chose paper
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
    
    # when computer chose scissor
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return Trueprint("Comp Turn: Rock(r) Paper(p) or scissor(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'you = input("Your Turn: Rock(r) Paper(p) or scissor(s)?")
a = gameWin(comp, you)
print ("\n")
print(f"1] Computer chose:- {comp}")
print(f"2] You chose:- {you} ")if a == None:
    print("==> The game is a tie! ")
elif a:
    print("==> You Win! 🤩")
else:
    print("==> You Lose! ☹️")
