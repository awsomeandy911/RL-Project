from game.tic_tac_toe import Board
from game.Player import Player
import numpy as np

class HumanPlayer(Player):
    def __init__(self):
        # Initialize player's side to None
        self.side = None
        super().__init__()

    def move(self, board: Board):
        # Display current board
        print(board.cells)
        move = int(input("Please enter a move:\n"))
        # Convert move to action tuple after user input
        action = (move // 3, move % 3)
        # Keep prompting for valid input until a valid action is entered
        while (not board.is_possible(action)):
            move = int(input("input again:\n"))
            action = (move // 3, move % 3)
        # Take the chosen action on the board
        board.take_turn(action)
        # Check if game is over and return winner, board, and over status
        (over, winner) = board.is_over()
        return winner, board, over

    def final_result(self, result: int):
        pass

    def new_game(self, side: int):
        self.side = side