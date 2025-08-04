import gymnasium as gym
from constants import NUM_PLAYERS, PIECES
import numpy as np

class AzulEnv(gym.Env):
    def __init__(self):
        super(AzulEnv, self).__init__()

        # Definir la acción y el espacio de observación
        self.action_space = gym.spaces.Tuple((
            gym.spaces.Discrete(6),  # De que lugar draftea (factories o pozo)
            gym.spaces.Discrete(5),  # Selección de color de piezas
            gym.spaces.Discrete(2),  # Selecciona ficha de ir primero
            gym.spaces.Discrete(6)  # En que nivel las coloca
        ))

        self.observation_space = gym.spaces.Dict({
            'draft_board': gym.spaces.Box(low=0, high=16, shape=(NUM_PLAYERS + 2, len(PIECES)), dtype=np.float32),  # Ejemplo: tablero de 10 elementos
            'players_board': gym.spaces.Box(low=0, high=7, shape=(NUM_PLAYERS * 6, len(PIECES)), dtype=np.int8),  # Información del jugador
            'scoring_board': gym.spaces.Box(low=0, high=5, shape=(NUM_PLAYERS * 5, 5), dtype=np.int8),  # Información del puntaje
            'current_player': gym.spaces.Discrete(NUM_PLAYERS),  # Jugador actual
            'turn': gym.spaces.Discrete(10),  # Turno actual
            'game_over': gym.spaces.Discrete(2)  # Estado del juego (en curso o terminado)
        })
    
    def reset(self):
        # Reiniciar el entorno al estado inicial
        self.state = np.random.rand(10)  # Ejemplo: un estado inicial aleatorio
        return self.state
    
    def step(self, action):
        # Ejecutar la acción en el entorno y devolver la nueva observación, recompensa, etc.
        reward = np.random.rand()  # Ejemplo: recompensa aleatoria
        done = np.random.rand() > 0.95  # Ejemplo: termina el episodio con probabilidad
        self.state = np.random.rand(10)  # Ejemplo: nuevo estado aleatorio
        return self.state, reward, done, {}

    def render(self, mode='human'):
        # Visualizar el entorno (opcional)
        print(f"Estado actual: {self.state}")

