import random

"""
this is a rock,paper,scissors,lizard and spock game. 
first person to win 3 rounds wins the game. 
Enjoy!
"""


LETTER_CHOICES = ['r', 'p', 'l', 'R', 'P', 'L', 'S', 's']
VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
S_VALIDATION = ['S', 's']

PLAYER_SCORE = 0
COMPUTER_SCORE = 0

def prompt(message):
    print(f'==> {message}')

def letter_to_word(choice):
    match choice:
        case 'r':
            return 'rock'
        case 'p':
            return 'paper'
        case 'l':
            return 'lizard'
        case 'R':
            return 'rock'
        case 'P':
            return 'paper'
        case 'L':
            return 'lizard'
        case 's':
            return 'spock'
        case 'S':
            return 'scissors'

def display_winner(player,computer):
    prompt(f'you chose {player}, computer chose {computer}')
    if((player == "rock" and computer == "scissors") or
        (player == "rock" and computer == "lizard") or
        (player == "paper" and computer == "rock") or
        (player == "paper" and computer == "spock") or
        (player == "scissors" and computer == "paper") or
        (player == "scissors" and computer == "lizard") or
        (player == "lizard" and computer == "paper") or
        (player == "lizard" and computer == "spock") or
        (player == "spock" and computer == "rock") or
        (player == "spock" and computer == "scissors")
        ):
        print("You win!")
        # return player_score += 1

    elif((player == "rock" and computer == "spock") or
        (player == "rock" and computer == "paper") or
        (player == "paper" and computer == "scissors") or
        (player == "paper" and computer == "lizard") or
        (player == "scissors" and computer == "rock") or
        (player == "scissors" and computer == "spock") or
        (player == "lizard" and computer == "rock") or
        (player == "lizard" and computer == "scissors") or
        (player == "spock" and computer == "lizard") or
        (player == "spock" and computer == "paper")
        ):
        print("Computer wins!")
        # return computer_score += 1

    else:
        print("It's a tie!")
# create prompt syntax

def increment_score(player,computer):

    global PLAYER_SCORE
    global COMPUTER_SCORE

    if((player == "rock" and computer == "scissors") or
        (player == "rock" and computer == "lizard") or
        (player == "paper" and computer == "rock") or
        (player == "paper" and computer == "spock") or
        (player == "scissors" and computer == "paper") or
        (player == "scissors" and computer == "lizard") or
        (player == "lizard" and computer == "paper") or
        (player == "lizard" and computer == "spock") or
        (player == "spock" and computer == "rock") or
        (player == "spock" and computer == "scissors")
        ):
        PLAYER_SCORE += 1

    if((player == "rock" and computer == "spock") or
        (player == "rock" and computer == "paper") or
        (player == "paper" and computer == "scissors") or
        (player == "paper" and computer == "lizard") or
        (player == "scissors" and computer == "rock") or
        (player == "scissors" and computer == "spock") or
        (player == "lizard" and computer == "rock") or
        (player == "lizard" and computer == "scissors") or
        (player == "spock" and computer == "lizard") or
        (player == "spock" and computer == "paper")
        ):
        COMPUTER_SCORE += 1

def display_score(PLAYER_SCORE, COMPUTER_SCORE):
    print(f"""
    The computer score is: {COMPUTER_SCORE}
    your score is:         {PLAYER_SCORE}
    """)

def who_wins(PLAYER_SCORE, COMPUTER_SCORE):
    if COMPUTER_SCORE == 3:
        print ('The computer wins the game!')
    if PLAYER_SCORE == 3:
        print ('you won the game!')

while True:

    prompt(f'type the first letter of the option: {', '.join(VALID_CHOICES)}')
        # display prompt syntax
    choice = input()
        # assigns input to choice variable

    while choice in S_VALIDATION:
        prompt('please type capital S for scissors or lowercase s for spock.')
        choice = input()
        if choice == 's' or 'S':
            break

    while choice not in LETTER_CHOICES:
        # if the input in choice is not in the accepted variables
        prompt('not a valid choice.')
        choice = input()
            # redoes an input, allows for it to be reented

    choice = letter_to_word(choice)

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice,computer_choice)

    increment_score(choice,computer_choice)

    display_score(PLAYER_SCORE, COMPUTER_SCORE)

    who_wins(PLAYER_SCORE,COMPUTER_SCORE)

        # end_game(player_score, computer_score)
    if COMPUTER_SCORE == 3 or PLAYER_SCORE == 3:
        break

    while True:

        prompt('do you want to plain again(y/n)')
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break
