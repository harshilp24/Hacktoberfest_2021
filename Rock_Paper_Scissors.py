import random
print("Welcome to rock paper scissors game .....")
print("You have three chances greater the wins in individual game will increase your chance to win")
print("Press 0-->paper , 1-->rock , 2-->scissors")

comp = 0
player = 0
for i in range(3):
    player_choice = input("Your turn")
    comp_choice=random.randint(0,2)
    print(f"you chose\t{player_choice} and computer chose\t{comp_choice}")
    if int( player_choice) >2:
        print("Enter number between 0,1,2")
        break
    
    if comp_choice == player_choice:
        print("Its a tie.")
        comp  = comp + 1
        player = player+ 1    

    if comp_choice == 0:

        if player_choice == 1:
            print("Computer wins.")
            comp  = comp + 1
        else:
            print("You win.")
            player = player+ 1 
    
    elif comp_choice == 1:

        if player_choice == 2:
            print("Computer wins.")
            comp  = comp + 1
        else:
            print("You win.")
            player = player+ 1 

    elif comp_choice == 2:

        if player_choice == 0:
            print("Computer wins.")
            comp  = comp + 1
        else:
            print("You win.")
            player = player+ 1 

if int(player) > int(comp):
    print("Hurray!!You win!!!")

else:
    print("Computer wins!! Better luck next time !!")                



