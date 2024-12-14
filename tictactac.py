import tkinter as tk
import random
import numpy as np

# Constants for the board
PLAYER_X = 1
PLAYER_O = 2
EMPTY = 0

# Create a 3x3 board
def create_board():
    return np.array([[EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY]])

# Check if there is a winner
def check_winner(board):
    for player in [PLAYER_X, PLAYER_O]:
        # Check rows, columns, and diagonals
        if (any(np.all(board[i, :] == player) for i in range(3)) or
            any(np.all(board[:, j] == player) for j in range(3)) or
            np.all(np.diagonal(board) == player) or
            np.all(np.diagonal(np.fliplr(board)) == player)):
            return player
    return None

# Check for tie
def is_full(board):
    return not np.any(board == EMPTY)

# Minimax algorithm to find the best move
def minimax(board, depth, maximizing_player):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1
    if winner == PLAYER_O:
        return -1
    if is_full(board):
        return 0

    if maximizing_player:  # Maximizing for PLAYER_X
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] == EMPTY:
                    board[i, j] = PLAYER_X
                    score = minimax(board, depth + 1, False)
                    board[i, j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:  # Minimizing for PLAYER_O
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i, j] == EMPTY:
                    board[i, j] = PLAYER_O
                    score = minimax(board, depth + 1, True)
                    board[i, j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Find the best move for the current player
def find_best_move(board, maximizing_player):
    best_score = -float('inf') if maximizing_player else float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i, j] == EMPTY:
                board[i, j] = PLAYER_X if maximizing_player else PLAYER_O
                score = minimax(board, 0, not maximizing_player)
                board[i, j] = EMPTY
                if (maximizing_player and score > best_score) or (not maximizing_player and score < best_score):
                    best_score = score
                    best_move = (i, j)
    return best_move

# UI Logic (Tkinter)
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe: Agent vs Agent")
        self.board = create_board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = PLAYER_X  # PLAYER_X starts the game
        self.game_over = False
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", width=10, height=3, font=("Arial", 24),
                                               command=lambda i=i, j=j: self.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row, col] == EMPTY and not self.game_over:
            self.board[row, col] = self.current_playerc:\Users\macha\OneDrive\Desktop\face recognition system.py
            self.buttons[row][col].config(text="X" if self.current_player == PLAYER_X else "O")
            if self.check_game_status():
                return
            self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
            self.ai_move()

    def ai_move(self):
        if self.game_over:
            return
        row, col = find_best_move(self.board, self.current_player == PLAYER_X)
        self.board[row, col] = self.current_player
        self.buttons[row][col].config(text="X" if self.current_player == PLAYER_X else "O")
        if self.check_game_status():
            return
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

    def check_game_status(self):
        winner = check_winner(self.board)
        if winner == PLAYER_X:
            self.game_over = True
            self.show_winner("Player X (AI) wins!")
        elif winner == PLAYER_O:
            self.game_over = True
            self.show_winner("Player O (AI) wins!")
        elif is_full(self.board):
            self.game_over = True
            self.show_winner("It's a tie!")
        return self.game_over

    def show_winner(self, message):
        winner_label = tk.Label(self.root, text=message, font=("Arial", 16))
        winner_label.grid(row=3, column=0, columnspan=3)

# Main Program to Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
