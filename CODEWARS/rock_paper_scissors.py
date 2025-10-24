# Description:
# Rules of the "Rock, Paper, Scissors" game are:

# Rock beats Scissors
# Scissors beat Paper,
# Paper beats Rock.
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples:
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

def rps(p1, p2):
    win_ = [('r','s'), ('s','p'), ('p','r')]
    if (p1[0].lower(), p2[0].lower()) in win_:
        return 'Player 1 won!'
    elif p1.lower() == p2.lower():
        return 'Draw!'
    return 'Player 2 won!'

print(rps(input('Enter Player 1: '), input('Enter Player 2: ')))