import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# Lisez les données et effectuez votre traitement
line = lines[0]
length = len(line)

if length == 1:
    print(line)
else:
    winner = line[0]
    for i in range(1, length):
        current = line[i]
        if current == 'C' and winner == 'F':
            winner = current
        elif current == 'F' and winner == 'P':
            winner = current
        elif current == 'P' and winner == 'C':
            winner = current
    print(winner)
