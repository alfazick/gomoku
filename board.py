


class Board:
    def __init__(self,n:int):
        self.dimension = n
        self.free_cells = set()

        self.matrix = [[" "  for _ in range(n)] for _ in range(n)]


        for row in range(n):
            for col in range(n):
                self.free_cells.add((row,col))

    def show_board(self):
        for row in self.matrix:
            print(row)

        print("#"*10)

    def place_move(self,row,col,chr):
        self.matrix[row][col] = chr

        self.show_board()



    
        