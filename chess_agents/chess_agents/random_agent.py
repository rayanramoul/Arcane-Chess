import random
from chess_agents.chess_agents.agent import Agent

class RandomAgent(Agent):
    def __init__(self):
        # set seed random
        # random.seed(0)
        print("\nAGENT CREATED\n")
        
    def initialize(self):
        print("Agent initialized")
    
    def choose_movement(self, state_board, possible_movements):
        # choose random movement
        print("possible movements : ", possible_movements)
        chosen_movement = random.choice(list(possible_movements))
        print("chosen movement : ", chosen_movement)
        return chosen_movement