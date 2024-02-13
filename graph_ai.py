# graph_ai.py
import random

class GraphAI:
    def __init__(self):
        self.graph = {}
        self.learning_rate = 0.1

    def get_move(self, game):
        available_moves = game.available_moves()
        if random.random() > self.learning_rate:
            return random.choice(available_moves)
        else:
            best_move = None
            max_value = -float('inf')
            for move in available_moves:
                if move not in self.graph:
                    self.graph[move] = random.random()  # Initialize with random values if move is new
                if self.graph[move] > max_value:
                    max_value = self.graph[move]
                    best_move = move
            return best_move

    def update_graph(self, move, reward):
        if move in self.graph:
            self.graph[move] += self.learning_rate * (reward - self.graph[move])
        else:
            self.graph[move] = reward
