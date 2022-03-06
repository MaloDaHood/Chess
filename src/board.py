from piece import *
import pygame
import sys
sys.path.append('../')

class Board:
    
    def __init__(self) -> None:
        pass
    
    def display_board(self, window) -> None:
        background = pygame.image.load("assets/board.png")
        background = pygame.transform.scale(background, (800, 800))
        window.blit(background, (0,0))
        
    def display_piece(self, window, piece :Piece) -> None:
        if piece.isAlive:
            window.blit(piece.get_image(), piece.get_position())
