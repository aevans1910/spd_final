# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

boardRepresentationStrsNum = 10

def drawBoard(board):
    """Prints out the board that function was passed. This board will
    be the board where our tic tac toe game appears."""

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    """Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, 
    and the computer's letter as the second."""
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, 
    # the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def whoGoesFirst():
    """Chooses the player who goes first at random."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def playAgain():
    """Returns True if the player wants to play again, 
    otherwise it returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    """Returns True if that player has won. Is given a board and a player’s letter."""
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    # TODO: Fix the indentation of this lines and the following ones. Fixed indentation?
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle  
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    """Makes a duplicate of the board list and returns it the duplicate."""
    dupeBoard = []

    for char in range(0, len(board)-1): # TODO: Clean this mess! Cleaned mess?
        dupeBoard.append(board[char])

    return dupeBoard

def isSpaceFree(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def getPlayerMove(board):
    """Lets the player type in their move."""
    # TODO: W0621: Redefining name 'move' from outer scope. Hint: 
    # Fix it according to https://stackoverflow.com/a/25000042/81306
    # Fixed it? Changed local variable name
    playerMove = ' ' 
    while playerMove not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(playerMove)):
        print('What is your next move? (1-9)')
        playerMove = input()
    return int(playerMove)

def chooseRandomMoveFromList(board, movesList):
    """Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move."""
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    # TODO: How would you write this pythanically? 
    # Changed to pythonically? "is not"
    if len(possibleMoves) is not 0: 
        return random.choice(possibleMoves)
    # TODO: is this 'else' necessary? 
    # No
    return None

def getComputerMove(board, computerMove): 
    # TODO: W0621: Redefining name 'computerLetter' from outer scope. 
    # Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    # Fixed? Changed local name to computerMove
    """Determines where to move and return that move after being 
    given a board and the computer's letter, """
    if computerMove == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, boardRepresentationStrsNum):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerMove, i)
            if isWinner(copy, computerMove):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, boardRepresentationStrsNum):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None: 
    # TODO: Fix it (Hint: Comparisons to singletons like None 
    # should always be done with is or is not, never the 
    # equality/inequality operators.)
    # Changed to "is not"
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    """Returns True if every space on the board has been 
    taken. Otherwise returns False."""
    for i in range(1, boardRepresentationStrsNum):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

# TODO: The following mega code block is a huge hairy monster. Break it down 
# into smaller methods. Use TODO s and the comment above each section as a guide 
# for refactoring.

# TODO: Work this shit out

def resetBoard():
# while True:
    # Reset the board
    # TODO: Refactor the magic number in this line 
    # (and all of the occurrences of 10 that are conceptually the same.)
    # Refactored the 10? Made a global variable
    theBoard = [' '] * boardRepresentationStrsNum 
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?) 
                        #       See whether you can get rid of this 'flag' variable. If so, remove it.
    return (theBoard, playerLetter, computerLetter, turn, gameIsPlaying)

def playGame(theBoard, playerLetter, computerLetter, turn, gameIsPlaying):
    while gameIsPlaying: # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
                         #       Use a meaningful name for the function you choose.
        if turn == 'player':
            # Player’s turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:  # TODO: is this 'else' necessary?
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:  # TODO: Is this 'else' necessary?
                    turn = 'computer'

        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:     # TODO: is this 'else' necessary?
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else: # TODO: Is this 'else' necessary?
                    turn = 'player'

    if not playAgain():
        break