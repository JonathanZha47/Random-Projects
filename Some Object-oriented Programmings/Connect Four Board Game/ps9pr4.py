#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self,checker,tiebreak,lookahead):
        """constructs a new AIPlayer object. """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        Player.__init__(self,checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        return "Player " + self.checker + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score.
        """
        score = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                score += [i]
        
        if self.tiebreak == "RIGHT":
            return score[-1]
        if self.tiebreak == "LEFT":
            return  score[0]
        if self.tiebreak == "RANDOM":
            return random.choice(score)
    
    def scores_for(self,b):
        """return a list containing one score for each column in order to know the possible next move
        """
        scores = [0] * b.width
        for col in range(b.width):
            if not b.can_add_to(col):
                scores[col] = -1
            elif b.is_win_for(self.checker):
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker,col)
                AI_Player = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead -1)
                opp_scores = AI_Player.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 50:
                    scores[col] = 50
                elif max(opp_scores) == -1:
                    scores[col] = 50
                
                b.remove_checker(col)
        return scores
        
    def  next_move(self,b):
        """return the called AIPlayer‘s judgment of its best possible move. """
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
    
    
            