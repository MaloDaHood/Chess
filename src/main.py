import pygame
from game import Game
from board import Board
from piece import *

if __name__ == "__main__":
    pygame.init()
    game = Game()
    board = Board()
    
    pawns = rooks = []
    x = 0
    for i in range(2):
        color = "B" if i == 0 else "W"
        
        # Creation of all the pawns
        for j in range(8):
            y = 100 if i == 0 else 600
            pawns.append(Pawn(color, (x + (j * 100), y)))
            
        # Creation of all the rooks
        for j in range(2):
            y = 0 if i == 0 else 700
            rooks.append(Rook(color, (x + (j * 700), y)))
            
        x = 0
    
    # Main game loop
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        board.display_board(game.get_window())
        board.display_pieces(game.get_window(), pawns)
        board.display_pieces(game.get_window(), rooks)
        
        game.update()
        
        if game.is_over():
            running = False
    
    pygame.quit()