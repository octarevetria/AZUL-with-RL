import numpy as np
from constants import NUM_PLAYERS, PIECES

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

    def is_first_move(self): # Algo similar a is_first_move
        """
        Check if it is the first move for the player.

        Parameters:

        Returns:
        - bool: True if it is the first move, False otherwise.
        """
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

    def is_game_over(self, board, pieces): # Facil pero necesaria implementacion
        """
        Check if no more tiles are remaining on the draft board.

        Parameters:
        - board (np.ndarray): The current board state.
        - pieces (np.ndarray): Array indicating which pieces are available for each player.

        Returns:
        - bool: True if the game is over, False otherwise.
        """
        pass