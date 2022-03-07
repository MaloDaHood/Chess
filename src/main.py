import pygame
from game import Game
from board import Board
from piece import *

if __name__ == "__main__":
    pygame.init()
    game = Game()
    board = Board()

    pieces = game.spawn_pieces(board.get_board())
    
    # Main game loop
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        board.display_board(game.get_window())
        board.display_pieces(game.get_window(), pieces)

        game.update()
        
        if game.is_over():
            running = False
    
    pygame.quit()