import numpy as np
from constants import NUM_PLAYERS, PIECES, SCOREBOARD_MASK, INDIVIDUAL_PLAYER_BOARD_HEIGHT, COLOR_TO_COLUMN

'''
funciones necesarias para el enviroment
self.game_logic.get_valid_actions(self.draft_board, self.players_board, self.current_player, self.scoring_board)
self.game_logic.place_piece(self.players_board, self.current_player, color, go_first, ladder_lvl, count)
self.game_logic.score_tiles(self.players_board, self.scoring_board, self.points_total)
self.game_logic.calculate_rewards(self.scoring_board, self.points_total)
self.game_logic.reset_draft_board(self.draft_board)
self.end_game_scoring(self.scoring_board, self.points_total)
'''

### Done functions

# self.game_logic.no_tiles_to_draft(self.draft_board)
# self.game_logic.update_first_player(self.players_board, self.current_player)
# self.game_logic.draft_piece(self, draft_board, draft_pool, color, count, go_first_available)
# self.game_logic.is_game_over(self, scoring_board)
# self.game_logic.player_tiles_clear(self, players_board)

class GameLogic:
    """
    Class containing the core game logic for the Azul board game environment.
    """
    def __init__(self):
        """
        Initialize the GameLogic class.
        """
        pass
    
    def draft_piece(self, draft_board, draft_pool, color, count, go_first_available):
        """
        Draw tiles from the draft board and the update it.

        Parameters:
        draft_board (np.ndarray): The current draft board state.
        draft_pool (int): The pool from which the piece is drafted.
        color (int): The color of the tiles to be drafted.
        count (int): The number of tiles to be drafted.
        go_first_available (bool): Whether the go first tile is still available.
        """
        center_draft_pool = draft_board.shape[0] - 1
        draft_board[draft_pool, color] = 0
        if draft_pool == center_draft_pool:
            if go_first_available: 
                draft_board[draft_pool, COLOR_TO_COLUMN["first_player"]] = 0
        else:
            draft_board[center_draft_pool] = draft_board[center_draft_pool] + draft_board[draft_pool]
            draft_board[draft_pool, : ] = 0

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
        for i in range(players_board.shape[0]):
            if i % INDIVIDUAL_PLAYER_BOARD_HEIGHT == 5:
                if  players_board[i, COLOR_TO_COLUMN["first_player"]] == 1: 
                    current_player = i // INDIVIDUAL_PLAYER_BOARD_HEIGHT
        return current_player # Podria no ser necesario devolverlo

    def is_game_over(self, scoring_board):
        """
        Check if theres a vertical line completed.

        Parameters:
        scoring_board (np.ndarray): The current socring_board state.

        Returns:
        - bool: True if the game is over, False otherwise.
        """
        for i in range(scoring_board.shape[0]):
            if scoring_board[i].sum() == 15:
                return True
        return False

    def player_tiles_clear(self, players_board):
        """ 
        Clear the tiles of the completed floors of all player's board.

        Parameters:
        players_board (np.ndarray): The current players board state.
        """
        for i in range(players_board.shape[0]):
            if i % INDIVIDUAL_PLAYER_BOARD_HEIGHT == 5 or players_board[i].sum() == (i % INDIVIDUAL_PLAYER_BOARD_HEIGHT) + 1:
                players_board[i, :] = 0

    def calculate_rewards(self, players_board, scoring_board, current_player, points_total, color, go_first_available, ladder_lvl, spill_tiles_count):
        """
        Calculate the rewards based on the current scoring board and players total points, rehacer.
        """
        reward = 0
        last_row_edited = current_player * INDIVIDUAL_PLAYER_BOARD_HEIGHT + ladder_lvl
        if players_board[last_row_edited, COLOR_TO_COLUMN[color]] == ladder_lvl + 1:
            reward += 1 # Seguir desde aca
        pass

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