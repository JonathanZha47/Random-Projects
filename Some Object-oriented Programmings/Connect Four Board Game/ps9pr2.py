#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
      """ a data type for a player of the Connect Four game"""
      
      def __init__(self,checker):
          """constructs a new Player object by initializing the two attributes
          """
          assert(checker == 'X' or checker == 'O')
          self.checker = checker
          num_moves = 0
          self.num_moves = num_moves
          
      def __repr__(self):
          """returns a string representing a Player object"""
          s = self.checker
          return 'Player ' + s
      
      def opponent_checker(self):
          """returns a one-character string representing the checker of the Player object’s opponent. """
          if self.checker == 'X':
              return 'O'
          else:
              return 'X'
      def next_move(self,b):
          """ accepts a Board object b as a parameter and returns the column where the player wants to make the next move."""
          self.num_moves += 1
          while True: 
              col = int(input('Enter a column: ')) 
              if 0 <= col <= b.width -1:
                  return col
                  break
              print('Try again!')
          b.add_checker(self.checker,col)

          