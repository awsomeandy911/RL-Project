from game.tic_tac_toe import Board
from game.Player import Player
import numpy as np
from copy import deepcopy


class BenchmarkPlayer(Player):
    def __init__(self):
        # Initialize player's side to None
        self.side = None
        super().__init__()

    def move(self, board: Board):
        # Get all possible moves
        possible_moves = board.possible_actions()

        # Shuffle the list of possible moves
        np.random.shuffle(possible_moves)

       # Check if there is a winning move for the player
        for i in possible_moves:
            # Make a copy of the board to test each move
            temp_board = deepcopy(board)
            move = (i[0], i[1])
            # Check if the move is valid
            if temp_board.is_possible(move):
                # If valid, make the move and check if it results in a win
                temp_board.take_turn(move)
                over, winner = temp_board.is_over()
                if over:
                    # If the move results in a win, make the move on the original board and return
                    board.take_turn(move)
                    over, winner = board.is_over()
                    return winner, board, over

        # Otherwise if there are no winning moves, make a random move and return(first index)
        board.take_turn((possible_moves[0][0], possible_moves[0][1]))
        over, winner = board.is_over()
        return winner, board, over

    def final_result(self, result: int):
        pass

    def new_game(self, side: int):
        self.side = side
