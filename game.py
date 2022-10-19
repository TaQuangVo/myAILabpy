from game import Tictactoe
import os
os.system('clear')



def getInput(currentPlayer):
    while 1:
        userInput = input(str(currentPlayer) + " turn: ")
        if(type(userInput) != int):
            print("Wrong input format!")
            continue
        if(userInput < 10 or userInput > 33):
            print("Wrong input format")
            continue
        return [userInput/10-1, userInput%10-1]


game = Tictactoe()
while 1:
    os.system('clear')
    game.draw()
    currentPlayer = game.getCurrentPlayer()
    print(game.getLegalMoves())
    userInput = getInput(currentPlayer)
    didMoved = game.makeMove(userInput[0], userInput[1])

    isOver = game.isOver()
    if(isOver != 0):
        os.system('clear')
        game.draw()
        print("Player " + str(isOver) + "win")
        break