"""
this is a rock,paper,scissors,lizard and spock game. 
first person to win 3 rounds wins the game. 
Enjoy!
"""
import random

LETTER_CHOICES = ['r', 'p', 'l', 'R', 'P', 'L', 'S', 's']
VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
S_VALIDATION = ['S', 's']

PLAYER_SCORE = 0
COMPUTER_SCORE = 0

def prompt(message):
    """
    Displays the prompt
    """
    print(f'==> {message}')

def letter_to_word(choice):
    """
    takes the option from VALID_CHOICES 
    allows user to input only a letter
    """
    match choice:
        case 'r' | 'R':
            return 'rock'
        case 'p' | 'P':
            return 'paper'
        case 'l' | 'L':
            return 'lizard'
        case 's':
            return 'spock'
        case 'S':
            return 'scissors'

def display_winner(player,computer):
    """
    display the winner of the round
    """
    match (player,computer):
        case ('rock', 'scissors') | ('rock', 'lizard') | ('paper', 'rock'):
            return 'you win'
        case ('paper', 'spock') | ('scissors', 'paper') | ('scissors', 'lizard'):
            return 'you win'
        case ('lizard', 'paper') | ('lizard', 'spock') | ('spock', 'scissors') | ('spock', 'rock'):
            return 'you win'
        case ('rock', 'spock') | ('rock', 'paper') | ('paper', 'scissors'):
            return 'computer wins'
        case ('paper', 'lizard') | ('scissors', 'spock') | ('scissors', 'rock'):
            return 'computer wins'
        case ('lizard', 'scissors') | ('lizard', 'rock') | ('spock', 'lizard') | ('spock', 'paper'):
            return 'computer wins'

def display_score(player_score, computer_score):
    """
    says the score
    """
    return f"""
        The computer score is: {computer_score}
        your score is:         {player_score}
        """

def increment_score(player, computer):
    """
    adds tally to score
    """
    prompt(f'you chose {player}, computer chose {computer}')

    if display_winner(player,computer) == 'you win':
        global PLAYER_SCORE
        PLAYER_SCORE += 1

    if display_winner(player,computer) == 'computer wins':
        global COMPUTER_SCORE
        COMPUTER_SCORE += 1

    if computer == player:
        prompt("it's a tie!")

def who_wins(player_score, computer_score):

    """
    says who won the game
    """
    if computer_score == 3:
        print ('The computer wins the game!')
    if player_score == 3:
        print ('you won the game!')

while True:

    prompt(f'type the first letter of the option: {', '.join(VALID_CHOICES)}')
        # display prompt syntax
    choice = input()
        # assigns input to choice variable

    while choice in S_VALIDATION:
        prompt('please type capital S for scissors or lowercase s for spock.')
        choice = input()
        if choice == 's'.lower():
            break
        if choice == 'S'.upper():
            break

    while choice not in LETTER_CHOICES:
        prompt('not a valid choice.')
        choice = input()

    CHOICE = letter_to_word(choice)

    computer_choice = random.choice(VALID_CHOICES)

    print(display_winner(CHOICE,computer_choice))

    increment_score(CHOICE,computer_choice)

    print(display_score(PLAYER_SCORE, COMPUTER_SCORE))

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
