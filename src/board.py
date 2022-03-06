from piece import *
import pygame
import sys
sys.path.append('../')

class Board:
    
    def __init__(self) -> None:
        # Basic board with starting positions
        self.board = [
            [4, 2, 3, 5, 6, 3, 2, 4],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 2, 3, 5, 6, 3, 2, 4]
        ]
        
    # Displays the board on full window
    def display_board(self, window :pygame.surface.Surface) -> None:
        background = pygame.image.load("assets/board.png")
        background = pygame.transform.scale(background, (800, 800))
        window.blit(background, (0,0))
        
    # Displays a list of piece at their own positions (in pixels)
    def display_pieces(self, window :pygame.surface.Surface, pieces :list[Piece]) -> None:
        for piece in pieces:
            if piece.isAlive:
                window.blit(piece.get_image(), piece.get_position())
