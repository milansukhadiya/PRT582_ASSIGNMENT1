# importing module
from random import randint
# taking case insensitive choices as input
choice = ['rock','paper','scissor']
ch = 'y'
rounds = 0

# player choice function
def player_choice():
    plr_ch = input("\nPlease input complete word.\n\nEnter your choice Rock / Paper / Scissor: ")

    # player can input other char so check to ensure that cannot be broken
    if plr_ch.lower() and plr_ch.lower() in ('rock','paper','scissor'):
        return plr_ch.lower()
    else:
        print("\nWrong Input... Please Retry...")
        player_choice()
        
# function with parameter to get result on every choice
def get_result(plr_ch):
    comp_choice = choice[randint(0,2)]
    print("\nComputer chose:",comp_choice,"\n")

     # basic game rules
    if plr_ch == comp_choice:
        result = "tie"
        print('{} is same as {}! No score change!'.format(plr_ch.upper(), comp_choice.upper()))
    elif comp_choice == 'scissor' and plr_ch == 'rock':
        result = 'win'
        print('ROCK Wins! Score +1')
    elif comp_choice == 'paper' and plr_ch == 'scissor':
        result = 'win'
        print('SCISSOR Wins! Score +1')
    elif comp_choice == 'rock' and plr_ch == 'paper': 
        result = 'win'
        print('PAPER Wins! Score +1')
        
    # if it does not match any of the win criteria then add 1 to loss and
    # display loss message
    else: 
        result = 'lose'
        print('You lose! Score -1')
    return result

# function to update the scores
def update_score(result):
    global wins, loss, tie
    if result == 'win':
        wins += 1
    elif result == 'lose':
        loss += 1
    else:
        tie += 1

# function to run the game till user defined rounds
def game(rounds):
    tot_score = 0
    global round_result
    for i in range(0,rounds):
        print("\nReady for Round", i+1)
        pc = player_choice()
        res = get_result(pc)
        round_result.append(res)
        update_score(res)
        tot_score = wins - loss
        print("\nAfter round",(i+1),"your score is: ",tot_score)

    return tot_score

# to take the number of rounds from user as input
def game_rounds(r = 0):
    r = input("\nEnter the number of rounds you want to play: ")

    try:
        global rounds
        rounds = int(r)
    except:
        print("\nWrong Input! Enter a number!")
        game_rounds()
        
# Main program
def main():
    global ch, round_result
    print("\nWelcome to Rock, Paper, Scissor Game.")
    print('''\nRules for Winning:\n
    Rock vs Paper -> Paper wins
    Rock vs Scissor -> Rock wins
    Paper vs Scissor -> Scissor wins\n
    For each win the user gets 1 point
    For each loss the user loses 1 point
    And for tie, the user gets 0 point\n''')


    game_rounds()
    ts = game(rounds)
    
    # displaying results after all  rounds
    print("\nAfter",rounds,"rounds, your final score is: ",ts)
    print("\nYou have {} wins, {} ties and {} losses!".format(wins,tie,loss))
    print("\nRound wise result is",round_result)
    ch = input("\nDo you want to continue? Enter y for yes any other char to exit: ")

while(ch == 'y' or ch == 'Y'):
    wins = 0
    loss = 0
    tie = 0

    round_result = []
    rounds
    main()
print("\nBye Bye!!")
