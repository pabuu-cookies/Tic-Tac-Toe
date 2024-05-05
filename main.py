import random as rd
import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x500")
        self.root.configure(background="black")
        self.n=3
        self.currentPlayer = "X"
        self.gameStatus = True
        self.board=None
        self.buttons=None
        self.winner=None
        self.message_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.message_label.pack(padx=10, pady=10)

    def submit(self):
        print(self.n-1)
        self.n=int(self.entry.get())
        self.print_message("Yay! Let's start")
        self.label.pack_forget()
        self.entry.pack_forget()
        self.submit_button.pack_forget()
        self.initialize_game()

    def initialize_game(self):
        self.print_message("Welcome to Tic Tac Toe Game")
        self.board = [['  ']*self.n for _ in range(self.n)]
        self.display_board()

    def print_message(self, message):
        self.message_label.config(text=message)

    def display_board(self):
        print("board display garney")
        self.buttons = [[None]*self.n for _ in range (self.n)]
        for i in range(self.n):
            frame=tk.Frame(self.root)
            frame.pack(side=tk.TOP)
            for j in range(self.n):
                self.buttons[i][j]=tk.Button(frame, text="", width=10, height=3, bg='lightgrey', command=lambda row=i, col=j:self.get_the_move(row,col))
                self.buttons[i][j].pack(side=tk.LEFT)
                self.buttons[i][j]["text"]=self.board[i][j]
        self.root.update()
        if self.currentPlayer == "O":
            self.computer_move()
        elif self.currentPlayer == "X":
            self.player_move()

    def player_move(self):
        self.print_message("Player's Turn")

    def computer_move(self):
        self.print_message("computer's Turn")
        Moverow = None
        Movecolumn = None
        if Moverow is None and Movecolumn is None:
            #check the winning move
            for i in range (self.n):
                for j in range(self.n):
                    if self.board[i][j] =="  ":
                        self.board[i][j] = "O"
                        if self.check_rows_cols() or self.check_diagonal():
                            Moverow = i
                            Movecolumn = j
                            break
                        else:
                            self.board[i][j] == "  "
        if Moverow is None and Movecolumn is None:
            #blocking the winning move
            for i in range (self.n):
                for j in range(self.n):
                    if self.board[i][j] =="  ":
                        self.board[i][j] = "X"
                        if self.check_rows_cols() or self.check_diagonal():
                            Moverow = i
                            Movecolumn = j
                            break
                        else:
                            self.board[i][j] == "  "
        if Moverow is None and Movecolumn is None:
            #strategy
            strategy = [(self.n//2,self.n//2), (0,0), (0,self.n-1), (self.n-1,0),(self.n-1, self.n-1)]
            for move in strategy:
                if self.board[move[0]][move[1]] == "  ":
                    Moverow = move[0]
                    Movecolumn = move[1]
                    break
        if Moverow is None and Movecolumn is None:
            #random
            while Moverow is None and Movecolumn is None:
                Mrow = rd.randint(0,self.n-1)
                Mcolumn =rd.randint(0,self.n-1)
                if self.board[Mrow][Mcolumn] == "  ":
                    Moverow = Mrow
                    Movecolumn = Mcolumn
        self.get_the_move(Moverow, Movecolumn)
                

    def get_the_move(self, row, col):
        print("we got the move")
        Moverow = row
        Movecolumn = col
        if (Moverow<=self.n-1 and Moverow>=0) and (Movecolumn <= self.n-1 and Movecolumn >=0):
            if self.board[Moverow][Movecolumn] =="  ":
                self.board[Moverow][Movecolumn]= self.currentPlayer
            else:
                self.print_message("Please select the empty spot to place your move")
                if self.currentPlayer == "X":
                    self.player_move()
                elif self.currentPlayer == "O":
                    self.computer_move()
        self.check_winner()

    def check_rows_cols(self): 
        for row in range(self.n):
            if all(self.board[row][col]== "X" for col in range(self.n)) or all(self.board[row][col]== "O" for col in range(self.n)):
                return True 
        for col in range(self.n):
            if all(self.board[row][col]== "X" for row in range(self.n)) or all(self.board[row][col]== "O" for row in range(self.n)):
                return True
        return False

    def check_diagonal(self):
        if self.board[0][0] !='  ':
            #check for forward diagonal
            for i in range(self.n):
                for j in range(self.n):
                    if i==j and self.board[i][j] != self.board[0][0]:
                        return False
        elif self.board[0][self.n-1] != '  ':
            #check for backward diagonal
            j=self.n-1
            for i in range(self.n):
                if self.board[i][j]!= self.board[0][self.n-1]:
                    return False
                j=j-1
        else:
            return False 
        return True 

    def check_winner(self):
        print("routine checkuppp")
        self.WinningStatus = (self.check_rows_cols() or self.check_diagonal())
        if self.WinningStatus:
            winner = self.currentPlayer
            self.print_message(f"congrats! {winner} wins the game")
            self.gameStatus = False
        else:
            if all('  ' not in row for row in self.board):
                self.print_message("Its a Tie!!")
                self.gameStatus = False
        if self.gameStatus:
            self.switch_player()
        else:
            for i in range(self.n):
                for j in range(self.n):
                    self.buttons[i][j].config(state=tk.DISABLED)
            self.remove_buttons()
            for i in range(self.n):
                frame = tk.Frame(self.root)
                frame.pack(side=tk.TOP)
                for j in range(self.n):
                    label = tk.Label(frame, text=self.board[i][j], width=6, height=3, borderwidth=2,bg='lightgrey', relief="solid")
                    label.pack(side=tk.LEFT)

            # Update the GUI
            self.root.update_idletasks()

    def remove_buttons(self):
        print("remove them now")
        for frame in self.root.winfo_children():
            if isinstance(frame, tk.Frame):
                frame.destroy()                

    def switch_player(self):
        print("adla badli")
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'
        self.remove_buttons()
        self.display_board()

game=TicTacToe()

game.message_label.config(text="")

game.label = tk.Label(game.root, text="Enter the size of grid(n) odd number only: ")
game.label.pack(pady=50)

game.entry = tk.Entry(game.root)
game.entry.pack()

game.submit_button = tk.Button(game.root, text="Submit", command=game.submit)
game.submit_button.pack()

game.root.mainloop()


