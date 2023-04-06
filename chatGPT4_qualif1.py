import sys
from collections import deque

def find_winner(input_str):
    if input_str is None or len(input_str) == 0:
        return ' '
    
    players = deque(input_str)
    
    while len(players) > 1:
        player1 = players.popleft()
        player2 = players.popleft()
        winner = determine_match_winner(player1, player2)
        players.appendleft(winner)

    return players[0]

def determine_match_winner(player1, player2):
    if player1 == player2:
        return player1
    elif player1 == 'P' and player2 == 'C':
        return player1
    elif player1 == 'C' and player2 == 'F':
        return player1
    elif player1 == 'F' and player2 == 'P':
        return player1
    else:
        return player2

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

for line in lines:
    print(find_winner(line))
