import random

letter = ''
difficulty = ''

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

def chooseDifficulty():
    global difficulty
    while not (difficulty == 'E' or difficulty == 'M' or difficulty == 'H'):
        print('What difficulty do you want? (input E, M or H)')
        difficulty = raw_input().upper()

def computerLetter(l):
    if l == 'X':
        return 'O'
    else:
        return 'X'

def whoIsFirst(l):
    if l == 'X':
        return 'player'
    else:
        return 'computer'

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

def getCopy(matrix):
    matrixCopy = []

    for i in matrix:
        matrixCopy.append(i)

    return matrixCopy

def isFree(matrix, move):
    return matrix[move] == ' '

def getPlayerMove(matrix):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isFree(matrix, int(move)):
        print("Enter a number between 1 and 9: ")
        move = raw_input()
    return int(move)

def chooseRandomMove(matrix, movesList):
    possibleMoves = []
    for i in movesList:
        if isFree(matrix, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMoveEasy(matrix, computerLetter):
    for i in range(1, 10):
        if isFree(matrix, i):
            makeMove(matrix, computerLetter, i)
            return i

    move = chooseRandomMove(matrix, [1, 3, 7, 9])
    if move != None:
        return move

    if isFree(matrix, 5):
        return 5

    return chooseRandomMove(matrix, [2, 4, 6, 8])

def getComputerMoveMedium(matrix, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getCopy(matrix)
        if isFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMove(matrix, [1, 3, 7, 9])
    if move != None:
        return move

    if isFree(matrix, 5):
        return 5

    return chooseRandomMove(matrix, [2, 4, 6, 8])

def getComputerMoveHard(matrix, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getCopy(matrix)
        if isFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getCopy(matrix)
        if isFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMove(matrix, [1, 3, 7, 9])
    if move != None:
        return move

    if isFree(matrix, 5):
        return 5

    return chooseRandomMove(matrix, [2, 4, 6, 8])

def isMatrixFull(matrix):
    for i in range(1, 10):
        if isFree(matrix, i):
            return False
    return True


print('This is TicTacToe for single player, you will play with computer.')

while True:
    newMatrix = [' '] * 10
    inputPlayerLetter()
    chooseDifficulty()
    playerLetter = letter
    computerLetter = computerLetter(letter)
    first = whoIsFirst(letter)
    print('The ' + first + ' is first to play.')
    gameIsPlaying = True

    while gameIsPlaying:
        if first == 'player':
            drawMatrix(newMatrix)
            move = getPlayerMove(newMatrix)
            makeMove(newMatrix, playerLetter, move)

            if isWinner(newMatrix, playerLetter):
                drawMatrix(newMatrix)
                print('You won!')
                gameIsPlaying = False
            else:
                if isMatrixFull(newMatrix):
                    drawMatrix(newMatrix)
                    print('Its a draw!')
                    break
                else:
                    first = 'computer'

        else:
            if difficulty == 'E':
                move = getComputerMoveEasy(newMatrix, computerLetter)
                makeMove(newMatrix, computerLetter, move)

                if isWinner(newMatrix, computerLetter):
                    drawMatrix(newMatrix)
                    print('The computer won. You lost.')
                    gameIsPlaying = False
                else:
                    if isMatrixFull(newMatrix):
                        drawMatrix(newMatrix)
                        print('Its a draw!')
                        break
                    else:
                        first = 'player'
            elif difficulty == 'M':
                move = getComputerMoveMedium(newMatrix, computerLetter)
                makeMove(newMatrix, computerLetter, move)

                if isWinner(newMatrix, computerLetter):
                    drawMatrix(newMatrix)
                    print('The computer won. You lost.')
                    gameIsPlaying = False
                else:
                    if isMatrixFull(newMatrix):
                        drawMatrix(newMatrix)
                        print('Its a draw!')
                        break
                    else:
                        first = 'player'
            else:
                move = getComputerMoveHard(newMatrix, computerLetter)
                makeMove(newMatrix, computerLetter, move)

                if isWinner(newMatrix, computerLetter):
                    drawMatrix(newMatrix)
                    print('The computer won. You lost.')
                    gameIsPlaying = False
                else:
                    if isMatrixFull(newMatrix):
                        drawMatrix(newMatrix)
                        print('Its a draw!')
                        break
                    else:
                        first = 'player'

    if not playAgain():
        break