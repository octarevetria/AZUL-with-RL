import gym
import numpy as np

class CustomBoardGameEnv(gym.Env):
    def __init__(self):
        super(CustomBoardGameEnv, self).__init__()
        # Definir la acción y el espacio de observación
        self.action_space = gym.spaces.MultiDiscrete([21,6])  # Ejemplo: 4 acciones posibles
        self.observation_space = gym.spaces.MultiDiscrete([6]*20 + #Las 5 fabricas
                                                          [2]*1 + #La ficha de ir primero
                                                          [7]*7 + #Negativas
                                                          [2]*5 + [2]*5 + [2]*5 + [2]*5 + [2]*5 + #Puntos
                                                          [6]*5 + #Primer lugar de niveles piramide
                                                          [2]*1 + #Segundo lugar de nivel 2
                                                          [2]*2 + #2do y 3er lugar de nivel 3
                                                          [2]*3 + #2do, 3er y 4to lugar de nivel 4
                                                          [2]*4) #2do, 3er, 4to y 5to lugar de nivel 5
    
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
