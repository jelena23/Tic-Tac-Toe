choice = ''

print("TicTacToe")

while not (choice == 'S' or choice == 'D'):
    print("Choose a mode you want to play in. For single player enter S, and for two players enter D: ")
    choice = raw_input().upper()

if choice == 'S':
    execfile("tictactoeComputer.py")
else:
    execfile("tictactoePlayers.py")
