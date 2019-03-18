letter = ''

def drawMatrix(matrix):
    print('   |   |')
    print(' ' + matrix[7] + ' | ' + matrix[8] + ' | ' + matrix[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + matrix[4] + ' | ' + matrix[5] + ' | ' + matrix[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + matrix[1] + ' | ' + matrix[2] + ' | ' + matrix[3])
    print('   |   |')

def inputPlayerLetter():
    global letter
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = raw_input().upper()

def otherPlayerLetter(l):
    if l == 'X':
        return 'O'
    else:
        return 'X'

def whoIsFirst(l):
    if l == 'X':
        return 'player1'
    else:
        return 'player2'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

def makeMove(matrix, letter, move):
    matrix[move] = letter

def isWinner(matrix, letter):
    return ((matrix[1] == letter and matrix[2] == letter and matrix[3] == letter) or
            (matrix[4] == letter and matrix[5] == letter and matrix[6] == letter) or
            (matrix[7] == letter and matrix[4] == letter and matrix[1] == letter) or
            (matrix[7] == letter and matrix[5] == letter and matrix[3] == letter) or
            (matrix[7] == letter and matrix[8] == letter and matrix[9] == letter) or
            (matrix[8] == letter and matrix[5] == letter and matrix[2] == letter) or
            (matrix[9] == letter and matrix[5] == letter and matrix[1] == letter) or
            (matrix[9] == letter and matrix[6] == letter and matrix[3] == letter))

def isFree(matrix, move):
    return matrix[move] == ' '

def getPlayerMove(matrix):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isFree(matrix, int(move)):
        print('Enter a number between 1 and 9')
        move = raw_input()
    return int(move)

def isMatrixFull(matrix):
    for i in range(1, 10):
        if isFree(matrix, i):
            return False
    return True

print("This is TicTacToe for two players.")

while True:
    newMatrix = [' '] * 10
    inputPlayerLetter()
    player1Letter = letter
    player2Letter = otherPlayerLetter(letter)
    first = whoIsFirst(letter)
    print('The ' + first + ' is first to play.')
    gameIsPlaying = True

    while gameIsPlaying:
        if first == 'player1':
            print ("It's player1's turn.")
            drawMatrix(newMatrix)
            move = getPlayerMove(newMatrix)
            makeMove(newMatrix, player1Letter, move)

            if isWinner(newMatrix, player1Letter):
                drawMatrix(newMatrix)
                print('Player1 won!')
                gameIsPlaying = False
            else:
                if isMatrixFull(newMatrix):
                    drawMatrix(newMatrix)
                    print('Its a draw!')
                    break
                else:
                    first = 'player2'

        else:
            print ("It's player2s move")
            drawMatrix(newMatrix)
            move = getPlayerMove(newMatrix)
            makeMove(newMatrix, player2Letter, move)

            if isWinner(newMatrix, player2Letter):
                drawMatrix(newMatrix)
                print('Player2 won!')
                gameIsPlaying = False
            else:
                if isMatrixFull(newMatrix):
                    drawMatrix(newMatrix)
                    print('Its a draw!')
                    break
                else:
                    first = 'player1'

    if not playAgain():
        break