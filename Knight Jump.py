


class ChessBoard:
    def __init__(self, N=int(input()), board = None):
        self.N = N
        self.board = board


    def create_board(self, board):

        for i in range(self.N):
            self.board.append(input().split())

        return print(self.board)



class Horse:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def newPosistion(self, x, y):
        pass



