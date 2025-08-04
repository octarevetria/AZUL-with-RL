import gymnasium as gym
from constants import NUM_PLAYERS, PIECES
import numpy as np

class AzulEnv(gym.Env):
    def __init__(self):
        super(AzulEnv, self).__init__()

        self.action_space = gym.spaces.Tuple((
            gym.spaces.Discrete(6),  # De que lugar draftea (factories o pozo)
            gym.spaces.Discrete(5),  # Selección de color de piezas
            gym.spaces.Discrete(2),  # Selecciona ficha de ir primero
            gym.spaces.Discrete(6)  # En que nivel las coloca
        ))

        self.observation_space = gym.spaces.Dict({
            'draft_board': gym.spaces.Box(low=0, high=16, shape=(NUM_PLAYERS + 2, len(PIECES)), dtype=np.int8),  # Factories y pozo
            'players_board': gym.spaces.Box(low=0, high=7, shape=(NUM_PLAYERS * 6, len(PIECES)), dtype=np.int8),  # Información del jugador
            'scoring_board': gym.spaces.Box(low=0, high=5, shape=(NUM_PLAYERS * 5, 5), dtype=np.int8),  # Información del puntaje
            'current_player': gym.spaces.Discrete(NUM_PLAYERS),  # Jugador actual
            'turn': gym.spaces.Discrete(10),  # Turno actual
            'game_over': gym.spaces.Discrete(2)  # Estado del juego (en curso o terminado)
        })

        self.reset()
    
    def reset(self, seed=None, options=None):
        """
        Reset the state of the environment and return an initial observation.

        Parameters:
        - seed (int, optional): Seed for random number generator.
        - options (dict, optional): Additional options for reset.

        Returns:
        - observation (dict): Initial observation of the environment.
        - info (dict): Additional info.
        """
        self.draft_board = np.zeros((NUM_PLAYERS + 2, len(PIECES)), dtype=np.int8)
        self.players_board = np.zeros((NUM_PLAYERS * 6, len(PIECES)), dtype=np.int8)
        self.scoring_board = np.zeros((NUM_PLAYERS * 5, 5), dtype=np.int8)
        self.current_player = 0
        self.turn = 1

        return self.get_observation(self), {}
    
    def step(self, action):
        """
        Execute one step in the environment.

        Parameters:
        - action (tuple): Action to be taken in the environment.

        Returns:
        - observation (dict): The observation after taking the action.
        - reward (float): Reward received after taking the action.
        - done (bool): Whether the episode has ended.
        - info (dict): Additional info.
        """
        all_valid_actions = self.game_logic.get_valid_actions(self.draft_board, self.players_board, self.current_player)
        if action not in all_valid_actions:
            raise ValueError("Invalid action")
        else:
            factory, color, go_first, ladder_lvl = action
            count = self.game_logic.draft_piece(self.draft_board, self.players_board, self.current_player, factory, color, go_first, ladder_lvl)
            self.game_logic.place_piece(self.players_board, self.current_player, color, go_first, ladder_lvl, count)
        return self.state, reward, done, {}

    def render(self, mode='human'):
        # Visualizar el entorno (opcional)
        print(f"Estado actual: {self.state}")

    def get_observation(self):
        """
        Get the current observation of the environment.

        Returns:
        - observation (dict): The current observation of the environment.
        """
        return {
            'draft_board': self.draft_board.flatten().astype(np.int8),
            'players_board': self.pieces.flatten().astype(np.int8),
            'scoring_board': self.scoring_board.flatten().astype(np.int8),
            'current_player': np.eye(NUM_PLAYERS)[self.current_player - 1].flatten().astype(np.int8),
            'turn': np.array([self.turn], dtype=np.int8)
        }

