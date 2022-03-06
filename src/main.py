import pygame
from game import Game
from board import Board
from piece import *

if __name__ == "__main__":
    pygame.init()
    game = Game()
    board = Board()
    board.display_board(game.get_window())
    
    queenB = Queen("B", (300, 0), True)
    board.display_piece(game.get_window(), queenB)
    
    game.run()