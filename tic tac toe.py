from graphics import *


class TicTacToe:
    def __init__(self):
        self.BOARD_SIZE = 3
        # we initialize
        self.CELL_SIZE = 100
        self.WINDOW_SIZE = self.BOARD_SIZE * self.CELL_SIZE
        self.board = [[' ' for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.win = GraphWin("Tic Tac Toe", self.WINDOW_SIZE, self.WINDOW_SIZE)
        self.current_player = 'X'

    def draw_board(self):
        #draws the board
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                x1 = col * self.CELL_SIZE
                y1 = row * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE
                rect = Rectangle(Point(x1, y1), Point(x2, y2))
                rect.setFill("white")
                rect.draw(self.win)

    def update_board(self, row, col):
        self.board[row][col] = self.current_player
        #we put the values of x and 0 in ' ' matrix

    def check_win(self):
        for row in range(self.BOARD_SIZE):
            #checks if all the columns of a rows are same
            if all(self.board[row][col] == self.current_player for col in range(self.BOARD_SIZE)):
                return True

        for col in range(self.BOARD_SIZE):
            #checks if all the rows of a column are same
            if all(self.board[row][col] == self.current_player for row in range(self.BOARD_SIZE)):
                return True

            #checks if 1,1 , 2,2, 3,3 are same from top left
        if all(self.board[i][i] == self.current_player for i in range(self.BOARD_SIZE)):
            return True
            #checks if 1,1 , 2,2, 3,3 are same from the top right
        if all(self.board[i][self.BOARD_SIZE - 1 - i] == self.current_player for i in range(self.BOARD_SIZE)):
            return True

        return False

    def check_full(self):
        for row in range(self.BOARD_SIZE):
            if ' ' in self.board[row]:
                return False
        return True
    #returns true if the boxes are full and it's not ' '

    def get_cell_from_click(self, x, y):
        row = int(y // self.CELL_SIZE)
        col = int(x // self.CELL_SIZE)
        return row, col #returns which row/column where it was clicked

    def draw_move(self, row, col):
        # draws the current move of player
        # takes row,column / calculates the coordinate / draws in the coordinate
        x = col * self.CELL_SIZE + self.CELL_SIZE // 2
        y = row * self.CELL_SIZE + self.CELL_SIZE // 2
        
        marker = Text(Point(x, y), self.current_player)
        marker.setSize(36)
        marker.draw(self.win)

    def display_result(self, message):
        #displays the given message
        result_text = Text(Point(self.WINDOW_SIZE // 2, self.WINDOW_SIZE // 2), message)
        result_text.setSize(24)
        result_text.setStyle("bold")
        result_text.draw(self.win)

    def play_game(self):
        self.draw_board()
        #calls the draw_board() function to draw the board

        while True:
            click_point = self.win.getMouse()
            click_x = click_point.getX()
            click_y = click_point.getY()

            #sends click coordinate to find which row & column
            row, col = self.get_cell_from_click(click_x, click_y) 

            if self.board[row][col] == ' ': #loop if vacant
                self.draw_move(row, col)
                self.update_board(row, col)
                
                #checks win
                if self.check_win():
                    self.display_result("Player {} wins!".format(self.current_player))
                    break
                
                #checks draw
                if self.check_full():
                    self.display_result("It's a tie!")
                    break
                
                #changes x & O in every click
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                

    def start(self):
        self.play_game()
        self.win.getMouse()
        self.win.close()


# Starts the game
game = TicTacToe()
game.start()
