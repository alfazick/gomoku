

from board import Board
from player import HumanPlayer
from player import RandomPlayer


def main():

    b = Board(10)
    b.show_board()

    p1 = HumanPlayer("Askar","O")

    p1.make_move(b)

    p2 = RandomPlayer("Roblox","X")

    p2.make_move(b)

    





main()


