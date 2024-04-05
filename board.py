


class Board:
    def __init__(self,n:int):
        self.moves = 0

        self.dimension = n
        self.free_cells = set()

        self.matrix = [[" "  for _ in range(n)] for _ in range(n)]

        up = [-1,0]
        down = [1,0]
        left = [0,-1]
        right = [0,1]

        diag_forward = [1,1]
        diag_backward = [-1,-1]

        antidiag_forward = [-1,1]
        antidiag__backward = [1,-1]

        self.neighbors =  {
            "column_check": [up,down],
            "row_check":[left,right],
            "diag_check":[diag_forward,diag_backward],
            "antidiag_check":[antidiag_forward,antidiag__backward],
        }






        for row in range(n):
            for col in range(n):
                self.free_cells.add((row,col))



    def count_visited_bfs(self,cur_row,cur_col,allowed_mark):

        ### find the winner to implement
        pass


    def analyze_board(self):
        self.moves +=1
        return self.moves > 10
    



    def show_board(self):
        for row in self.matrix:
            print(row)

        print("#"*10)

    def place_move(self,row,col,chr):
        self.matrix[row][col] = chr

        self.show_board()



    
        