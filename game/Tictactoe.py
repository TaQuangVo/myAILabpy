import numpy as np


class Tictactoe:
    def __init__(self):
        self.state = np.zeros(9, dtype=int)
        self.currentPlayer = 1

    def makeMove(self, x, y):
        if(self.state[y*3+x] != 0):
            return False
        self.state[y*3+x] = self.currentPlayer
        self.currentPlayer = 4 if self.currentPlayer == 1 else 1
        return True

    def getCurrentPlayer(self):
        return self.currentPlayer

    def isOver(self):
        for i in range(3):
            cols = self.state[0+i] + self.state[3+i] + self.state[6+i]
            if cols == 3 or cols == 12:
                return cols / 3

            row = self.state[0+3*i] + self.state[1+3*i] + self.state[2+3*i]
            if row == 3 or row == 12:
                return row / 3

            dia1 = self.state[0] + self.state[4] + self.state[8]
            if dia1 == 3 or dia1 == 12:
                return dia1 / 3

            dia2 = self.state[2] + self.state[4] + self.state[6]
            if dia2 == 3 or dia2 == 12:
                return dia2 / 3

        return 0
    
    def draw(self):
        print("   1 2 3\n")
        for y in range(3):
            row = str(y+1) + "  "
            for x in range(3):
                row += str(self.state[y*3+x]) + " "
            print(row)
        print("\n")

    def getLegalMoves(self):
        legalMoves = []
        for y in range(3):
            for x in range(3):
                if(self.state[y*3+x] == 0):
                    legalMove = [y, x]
                    legalMoves.append(legalMove)
        return legalMoves


    def getState(self):
        return self.state.copy()