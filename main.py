

from board import Board
from player import HumanPlayer
from player import RandomPlayer


def main():

    try:
        # Board prep

        n = int(input("Type dimension of board on which you want to play gomuku: "))
        active_board = Board(n)

        option = int(input("Type number 1: if you want to play with Human\nType number 2: to play against robot => "))

        if option not in [1,2]:
            raise Exception
        

        p1 = None
        p2 = None

        if option == 1:
            p1 = HumanPlayer("Human","O")
            p2 = HumanPlayer("Human","X")
        else:
            p1 = HumanPlayer("Human","O")
            p2 = p2 = RandomPlayer("Roblox","X")


        order = 0

        game_finished = False
        while not game_finished:

            if order % 2 == 0:
                cur_player = p1 
            else:
                cur_player = p2


            active_board.show_board()

            cur_player.make_move(active_board)

            game_finished = active_board.analyze_board()

            order +=1
            order %=2




    except:
        print("Provide correct numeric value next time. Game over.")






main()


