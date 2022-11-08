# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:42:02 2019

@author: Jonathan
"""
class Board:
    """ a data type for a connect four board with arbitrary dimensions
    """
    def __init__(self,height,width):
        """ a constructor for Board objects """
        self.height = height
        self.width = width
        self.slots =  [[' ']*self.width for r in range(height)]

    
    def __repr__(self):
        """ return a string representation of a Board """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
            
        s += '-'*self.width*2 + '-' +'\n'
        for n in range(self.width):
            if n > 9 :
                s += ' '+ str(n-10)
            else:
                s += ' ' + str(n)
        return s
     
    def add_checker(self, checker, col):
        """ add checker into the Board """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = 0
        while self.slots[row][col] == ' ': 
            row += 1
            if row == self.height-1:
                break
        if self.slots[row][col] != ' ':
            row += -1
        self.slots[row][col] = checker
    
    def reset(self):
        """reset the Board object on which it is called by setting all slots to contain a space character.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
                
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

        # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    def can_add_to(self,col):
        """ returns True if it is valid to place a checker in the column col on the calling Board object. Otherwise, it should return False."""
        if  0 <= col < self.width:
            for row in range(self.height):
                while self.slots[row][col] == ' ':
                    return True
                return False
        else:
            return False
        
    def is_full(self):
        """returns True if the called Board object is completely full of checkers, and returns False otherwise."""
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
                return True
    
    def remove_checker(self,col):
        """ removes the top checker from column col of the called Board object. If the column is empty, then the method should do nothing."""
        row = 0
        while row < self.height:
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                row += self.height + 1
            else:
                row += 1
    
# is_win_for(self,checker)    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                        return True
        # if we make it here, there were no horizontal wins
        return False
    def is_vertical_win(self,checker):
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                        return True
        # if we make it here, there were no horizontal wins
        return False
    
    def is_down_diagonal_win(self,checker):
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col]== checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3 ][col + 3] == checker:
                        return True
        # if we make it here, there were no horizontal wins
        return False
    
    def is_up_diagnoal_win(self,checker):
        row = self.height -1
        while row > 3:
            for row in range(self.height-3):
                for col in range(self.width-3):
                    if self.slots[row][col]== checker and \
                        self.slots[row - 1][col + 1] == checker and \
                        self.slots[row - 2][col + 2] == checker and \
                        self.slots[row - 3 ][col + 3] == checker:
                            return True
        # if we make it here, there were no horizontal wins
        return False

    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots containing checker on the board. Otherwise, it should return False.
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_down_diagonal_win(checker):
            return True
        if self.is_up_diagnoal_win(checker):
            return True
        if self.is_vertical_win(checker):
            return True
        if self.is_horizontal_win(checker):
            return True
        else:
            return False
        
            