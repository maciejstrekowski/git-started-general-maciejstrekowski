import random

print("I see you're bored. Let's play the rock, paper, scissors game?")

def rock_paper_scissors():
  
    choices = ["rock", "paper", "scissors"]
    number_of_tries = 0
    rounds =input("How many round would you like to play?\n")
    win_count = 0
    lose_count = 0
 

    while number_of_tries < int(rounds):
        number_of_tries += 1
        cpu_guess = random.choice(choices)
        player_guess = input("Choose rock, paper or scissors!\n")
        if player_guess == "rock" and cpu_guess == "rock":
           print(cpu_guess)
           print("Tie. You can do better babe!")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        elif player_guess == "paper" and cpu_guess == "paper":
           print(cpu_guess)
           print("Good guess!")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        elif player_guess == "scissors" and cpu_guess == "scissors":
           print(cpu_guess)
           print("Damn.")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        elif player_guess == "paper" and cpu_guess == "scissors":
           lose_count += 1
           print(cpu_guess)
           print("Ha!")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        elif player_guess == "scissors" and cpu_guess == "rock":
           lose_count += 1
           print(cpu_guess)
           print("Poor you. Don't give up honey.")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        elif player_guess == "rock" and cpu_guess == "paper":
           lose_count += 1
           print(cpu_guess)
           print("Deal with that!")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        elif player_guess == "scissors" and cpu_guess == "paper":
           win_count += 1
           print(cpu_guess)
           print("Good for you!")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        elif player_guess == "rock" and cpu_guess == "scissors":
           win_count += 1
           print(cpu_guess)
           print("Damn")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        elif player_guess == "paper" and cpu_guess == "rock":
           win_count += 1
           print(cpu_guess)
           print("I'm sure you cheated...")
           print( str(win_count) + " For you" )
           print( str(lose_count) + " For me" )
        else:  
           print("pap..heey!")
           print("You loose, you f'kn loose 'cause you can't play! Let's try again babe. Try to focus this time. ")
    if win_count > lose_count:
        print("You won, lucky bastard!")
    elif win_count < lose_count:
        print("LOOOOOSER!")
    else:
        print("Tie")
if __name__ == "__main__":
   next_game = True
   while  next_game:
       rock_paper_scissors()
       next_time_input = input("It was fun! Do You want to play again? y/n\n")
       if next_time_input == 'n':
           next_game = False
           print("Ohh, goodbye then. I'll miss u") 
           break