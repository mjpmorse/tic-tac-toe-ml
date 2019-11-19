### From Chapter 1 of Mitchell.
### First
##### Task T:        Learn Tic-Tac-Toe
##### Performance P: Percent of games won against a human player
##### Training E:    Games played against self

###############################################
### Target function: V: Boards -> R         ###
### Assigns higher scores to winning boards ###
### Function approx: h: wT*x                ###
### x are board featuresm w is weights      ###
###############################################

############# Need ###########
###  Experiment Generator  ###
###  Performance System    ###
###  Critic                ###
###  Generalizer           ###
##############################


## Imports
import numpy as np


### Experiment Generator
class Experiment_Generator():
    ### In Tic Tac Toe the generator will always return a new game ##
    ### In general the generator will take the current hypothesis and
    ### generate a new game based on unexplored parameter space ####

    def __int__(self):
        self.initial_board_state = [['','',''],['','',''],['','','']]

    def generate_game(self):
        return(self.initial_board_state)

class Player:

    ## Methods needed
    ### int, is_game_over, find_moves

    def __int__(self,player_symbol,weights):

        self.player_symbol = player_symbol
        self.weights = weights

    def is_game_over(self,board,player_symbol):

        game_over = False
        ## We need to check win senarios

        ## Loop over rows and check for 3 in a row
        for row in range(0,3):
            ## Check the rows for a victory
            game_over = all(symbol == player_symbol for symbol in board[:][row])
            ## return that the game is over if victory is found
            if(game_over):
                return(game_over)


        for column in range(0,3):
            ## Check the columns for a victory
            game_over = all(symbol == player_symbol for symbol in board[column][:])
            if(game_over):
                return(game_over)


        ### need to check the two diagionals as well

        if(board[0][0]==board[1][1]==board[2][2]==player_symbol):
            game_over = True
            return(game_over)
        if(board[0][2]==board[1][1]==board[2][0]==player_symbol):
            game_over = True
            return(game_over)
