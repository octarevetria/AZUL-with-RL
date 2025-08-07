import numpy as np
from constants import NUM_PLAYERS, PIECES, SCOREBOARD_MASK, PLAYERS_BOARD_ROWS, PLAYERS_BOARD_COLS, DRAFT_BOARD_ROWS, DRAFT_BOARD_COLS, INDIVIDUAL_PLAYER_BOARD_HEIGHT

'''
funciones necesarias para el enviroment
self.game_logic.get_valid_actions(self.draft_board, self.players_board, self.current_player, self.scoring_board)
self.game_logic.draft_piece(self.draft_board, self.players_board, self.current_player, draft_pool, color, go_first, ladder_lvl)
self.game_logic.place_piece(self.players_board, self.current_player, color, go_first, ladder_lvl, count)
self.game_logic.score_tiles(self.players_board, self.scoring_board, self.points_total)
self.game_logic.calculate_rewards(self.scoring_board, self.points_total)
self.game_logic.is_game_over(self.scoring_board)
self.game_logic.end_game_scoring(self.scoring_board, self.points_total)
self.game_logic.player_tiles_clear(self.players_board)
self.game_logic.reset_draft_board(self.draft_board)
'''

### Done functions

# self.game_logic.no_tiles_to_draft(self.draft_board)
# self.game_logic.update_first_player(self.players_board, self.current_player)


class GameLogic:
    """
    Class containing the core game logic for the Azul board game environment.
    """
    def __init__(self):
        """
        Initialize the GameLogic class.
        """
        pass

    def place_piece(self): # Necesita ser implementada
        """
        Place a piece on the board if the move is valid.

        Parameters:

        Returns:
        - bool: True if the piece is placed successfully, False otherwise.
        """
        pass

    def no_tiles_to_draft(self, draft_board):
        """
        Check if the theres no tiles remaining on the draft board.

        Parameters:
        draft_board (np.ndarray): The current draft board state.

        Returns:
        bool: True if theres no tiles remaining on the draft board. False otherwise.
        """
        return np.sum(draft_board) == 0

    def update_first_player(self, players_board, current_player):
        """
        Update the first player for the next turn.
        """
        for i in range(PLAYERS_BOARD_ROWS):
            if i % INDIVIDUAL_PLAYER_BOARD_HEIGHT == 5:
                for j in range(PLAYERS_BOARD_COLS):
                    if players_board[i, j] == 1: 
                        current_player = i // INDIVIDUAL_PLAYER_BOARD_HEIGHT
        return current_player

    def is_valid_move(self): #Chequear si esta disponible el color donde se quiere colocar
        """
        Check if the move is valid.

        Parameters:

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        pass

        return True

    def get_valid_actions(self): # Necesita ser implementada
        """
        Get 1 valid action for the current player.

        Parameters:

        Returns:
        - list: List of valid actions.
        """
        pass

    def is_game_over(self, scoring_board): # Facil pero necesaria implementacion
        """
        Check if theres a vertical line completed.

        Parameters:
        scoring_board (np.ndarray): The current socring_board state.

        Returns:
        - bool: True if the game is over, False otherwise.
        """
        pass