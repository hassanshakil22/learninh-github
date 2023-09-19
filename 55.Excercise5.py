import random
print ("WELCOME TO ROCK, PAPER, SCISSORS")
def rps():
    while True: 
        choices= ["Rock","Paper","Scissor"]
        user_action = (input("Enter your choice : Rock , Paper, Scissor : "))
        user_action = user_action.title()
        computer_action = random.choice(choices)
        if user_action==computer_action:
            print(f"you chose {user_action} and computer chose {computer_action} \n it's a draw !")
        elif  user_action == "Rock" : # rock
            if computer_action == "Paper" :
                print (f"you chose {user_action } ,computer chose {computer_action} \n Paper wraps rock therefore , You lose! ")
            elif computer_action == "Scissor":
                print (f"you chose {user_action } ,computer chose {computer_action} \n rock breaks scissor therefore , You Win! ")
            
        elif  user_action == "Paper"  : #paper
            if computer_action == "Rock" :
                print (f"you chose {user_action } ,computer chose {computer_action} \n Paper wraps rock therefore , You win! ")
            elif computer_action=="Scissor":
                print (f"you chose {user_action } ,computer chose {computer_action} \n scissor cuts paper therefore , You lose! ")
            
        elif user_action == "Scissor" :
            if computer_action == "Rock" :
                print (f"you chose {user_action } ,computer chose {computer_action} \n rock breaks scissor therefore , You Lose! ")
            elif computer_action=="Paper" : 
                print (f"you chose {user_action } ,computer chose {computer_action} \n scissor cuts paper therefore , You Win! ")
        else:
                raise ValueError ("invalid input")         
        play_again = input("Play Again ? Y / N :")
        if play_again.upper() != "Y" :
             break

rps()            