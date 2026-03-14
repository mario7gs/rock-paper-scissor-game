import random
import time
from termcolor import colored

# Initiating global variables for rounds and a list history

rounds = 0
hist = []

# Score: let's use a list contenting [user victory, computer victory, draw], and options list will contain the
# 4 possibilities to choose from

score = [0, 0, 0] 
options = ["ROCK", "PAPER", "SCISSOR", "NEEDLE"]

def print_menu() -> None:
    
    print(colored("+-------------------------------------------------------------------------------------+", 'blue', 'on_grey'))
    print(colored("|                                                                                     |", 'blue', 'on_grey'))
    print(colored("|            ***           ROCK, PAPER, SCISSOR, NEEDLE            ***                |", 'blue', 'on_grey', attrs=["blink", "bold"]))
    print(colored("|                                                                                     |", 'blue', 'on_grey'))
    print(colored(f"|           YOU: {score[0]}               COMPUTER: {score[1]}                TIES: {score[2]}                   |", 'blue', 'on_grey', attrs=["bold"]))
    print(colored("|                                                                                     |", 'blue', 'on_grey'))
    print(colored("+-------------------------------------------------------------------------------------+", 'blue', 'on_grey'))
    time.sleep(0.7)

def get_winner(user, comp):
    '''
    This logic uses the get() method to fetch the win-conditions...
    '''
    if user == comp:
        return "TIE"
    
    # The game logic: the keys wins over the values
    rules = {
        "ROCK": ["SCISSOR", "NEEDLE"],
        "PAPER": ["ROCK"],
        "SCISSOR": ["PAPER"],
        "NEEDLE": ["PAPER"]
    }
    
    # Using a dict for the game logic to turn it easily extensible. If decided add new weapons,
    # it'll be enough update the new weapon at the bottom of the dict without breaking the logic 

    if comp in rules.get(user, []):
        return "WIN"
    return "LOSS"

    '''
    This if controls through the get() method the user choice and the comp weapon random assigned; 
    if user's choice is inside the rules dict, returns from the list that weapon could be beat off: in this
    case will be returned WIN, otherwise, (if not a tie neither a  user's win) it will return LOSS (default case) 
    '''


def ask_game():
    global rounds, hist, score
    
    while True:
        print(colored("+-------------------------------------------------------------------------------------+", 'blue', 'on_grey'))
        print(colored("|                                                                                     |", 'blue', 'on_grey'))
        print(colored("|                   Choose:   ROCK,   PAPER,   SCISSOR,  NEEDLE                       |", 'cyan', 'on_grey'))
        print(colored("|                                                                                     |", 'blue', 'on_grey'))
        print(colored("|                                      ...   Or press 'Q' to exit   ...               |", 'white', 'on_grey'))
        print(colored("+-------------------------------------------------------------------------------------+", 'blue', 'on_grey'))
        time.sleep(0.7)
        user_choice = input(colored("               Make your choice   ...  >>>   ", 'green')).strip().upper()

        if user_choice == "Q":
            print_final_summary()
            break

        if user_choice not in options:
            print(colored("\n" + " " * 15 + "!!! Choice not valid. Try again !!!", 'red', attrs=['bold']))
            continue

        # Round logic: comp_choice is assigned with the result of the execution of random() method imported
        # using as parameter the list inside option variable. The result variable will call the get_winner()
        # function 
        
        comp_choice = random.choice(options)
        result = get_winner(user_choice, comp_choice)

        # ---  Delay effect ---
        print(colored("\n" + " " * 20 + "Rock...", 'red', attrs=['bold']))
        time.sleep(0.4)
        print(colored(" " * 25 + "Paper...", 'yellow', attrs=['bold']))
        time.sleep(0.4)
        print(colored(" " * 30 + "Scissor...", 'green', attrs=['bold']))
        time.sleep(0.4)
        print(colored(" " * 35 + "SHOOT!\n", 'cyan', attrs=['bold', 'blink']))
        time.sleep(0.2)
                # ------------------------

               
        # If statement to decide the result of the round and updating the score and appending it to history list 
        if result == "WIN":
            score[0] += 1
            msg_color = 'green'
        elif result == "LOSS":
            score[1] += 1
            msg_color = 'red'
        else:
            score[2] += 1
            msg_color = 'yellow'

        rounds += 1
        hist.append(f"   Round {rounds} :  {user_choice}   vs   {comp_choice}  ->  ({result}) ")

            # UI for the round
        print(colored("+-------------------------------------------------------------------------------------+", 'blue', 'on_grey'))
        print(colored("|                                                                                     |", 'blue', 'on_grey'))
        print(colored(f"   This round: YOU: {user_choice:^10}  vs   COMP: {comp_choice:^10}         RESULT:  {result:^10}     ", 'white', 'on_blue', attrs=['bold']))
        print(colored("|                                                                                     |", 'blue', 'on_grey'))
        print(colored("+-------------------------------------------------------------------------------------+", 'blue', 'on_grey'))

        # Showing update score after the round
        print(colored(f"\n       STATS:      YOU:   {score[0]}       |       COMPUTER:   {score[1]} \n", msg_color, attrs=['bold']))

def print_final_summary():
    print_menu()             
    print(colored(f"+-------------------------------------------------------------------------------------+", 'green', 'on_grey'))
    print(colored(f"|                                                                                     |", 'green', 'on_grey'))
    print(colored(f"|                               THANKS FOR PLAYING !                                  |", 'green', 'on_grey', attrs=['blink', 'bold']))
    time.sleep(0.4)
    print(colored(f"|                                                                                     |", 'green', 'on_grey'))
    print(colored(" " * 35 + "The results were ...\n", 'blue', attrs=['bold']))
    time.sleep(0.7) 
    print(colored(f"|                                                                                     |", 'green', 'on_grey'))
    print(colored(f"|          Final Score:   {score[0]}   -   {score[1]}                          Total Rounds: {rounds}          |", 'green', 'on_grey', attrs=['bold']))                 
    print(colored(f"|                                                                                     |", 'green', 'on_grey'))
    print(colored(f"+-------------------------------------------------------------------------------------+", 'green', 'on_grey'))
    
    for r in hist:
        # Aligning the list
        print(colored(f"|          {r:<74} |", 'green', 'on_grey'))                 
    print(colored(f"+-------------------------------------------------------------------------------------+", 'green', 'on_grey'))


