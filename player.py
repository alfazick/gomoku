

import random

from board import Board


class Player:
    def __init__(self,name,symbol):
        self.name = name 
        self.symbol = symbol

    
    def make_move(self):
        pass 



class HumanPlayer(Player):
    def make_move(self,board:Board):
        
        row = -1
        col = -1

        while row < 0 or col < 0:

            try:
                new_row = int(input("Type row on which you want a place your move"))
                new_col = int(input("Type col on which you want a place your move"))

                if (new_row,new_col) in board.free_cells:
                    board.place_move(new_row,new_col,self.symbol)
                    row = new_row
                    col = new_col
                else:
                    print("Dimension is board is {}, indexing starts with 0".format(board.dimension))
                    print("Check if cell is already occupied")



            except:
                print("Please provide valid coordinates")


class RandomPlayer(Player):
    def make_move(self,board:Board):
        
        cur_moves = list(board.free_cells)
        random_idx = random.randint(0,len(cur_moves))

        next_row,next_col = cur_moves[random_idx]

        board.place_move(next_row,next_col,self.symbol)




        
                