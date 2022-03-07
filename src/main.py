import pygame
from game import Game
from board import Board
from piece import *

if __name__ == "__main__":
    pygame.init()
    game = Game()
    board = Board()

    window = game.get_window()
    
    pieces = game.spawn_pieces(board.get_board())
    
    # Main game loop
    while(game.is_running()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.stop()
                
        board.display_board(window)
        board.display_pieces(window, pieces)

        game.update()
        
        game.check_if_over()
    
    pygame.quit()