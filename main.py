# game.py
import os
from graph_ai import GraphAI
from learning_algorithm import LearningAlgorithm

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.graph_ai = GraphAI()
        self.learning_algorithm = LearningAlgorithm()

    def print_board(self):
        os.system('clear')
        print(" " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " ")
        print("-----------")
        print(" " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " ")
        print("-----------")
        print(" " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " ")

    def print_board_nums(self):
        print(" 0 | 1 | 2 ")
        print("-----------")
        print(" 3 | 4 | 5 ")
        print("-----------")
        print(" 6 | 7 | 8 ")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, letter):
        # Check rows, columns, and diagonals
        for start, step in zip([0, 3, 6, 0, 1, 2, 0, 2], [1, 1, 1, 3, 3, 3, 4, 2]):
            if all([self.board[start + i * step] == letter for i in range(3)]):
                return True
        return False
def play(game, x_player, o_player, print_game=True):
  if print_game:
      game.print_board_nums()

  letter = 'X'
  while game.empty_squares():
      if letter == 'O':
          square = o_player.get_move(game)
      else:
          square = x_player.get_move(game)

      if game.make_move(square, letter):
          if print_game:
              print(f'{letter} makes a move to square {square}')
              game.print_board()
              print('')

          if game.current_winner:
              if print_game:
                  print(f'{letter} wins!')
              return letter

          letter = 'O' if letter == 'X' else 'X'

  if print_game:
      print('It\'s a tie!')

if __name__ == '__main__':
  game = TicTacToe()
  x_player = GraphAI()
  o_player = GraphAI()
  play(game, x_player, o_player)

