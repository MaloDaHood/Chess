from piece import *
import pygame
import sys
sys.path.append('../')

class Board:
    
    def __init__(self) -> None:
        # Basic board with starting positions
        self.board = [
            ["RB1", "HB1", "BB1", "QB1", "KB1", "BB2", "HB2", "RB2"],
            ["PB1", "PB2", "PB3", "PB4", "PB5", "PB6", "PB7", "PB8"],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["PW1", "PW2", "PW3", "PW4", "PW5", "PW6", "PW7", "PW8"],
            ["RW1", "HW1", "BW1", "QW1", "KW1", "BW2", "HW2", "RW2"]
        ]
          
        # Creates the background board
        self.background = pygame.image.load("assets/board.png")
        self.background = pygame.transform.scale(self.background, (800, 800))
    
    def get_board(self) -> list[list[str]]:
        return self.board
    
    # Displays the board on full window
    def display_board(self, window :pygame.surface.Surface) -> None:
        window.blit(self.background, (0,0))
        
    # Displays all pieces at their own positions (in pixels)
    def display_pieces(self, window :pygame.surface.Surface, pieces :dict[str, Piece]) -> None:
        for id in pieces:
            if pieces[id].is_alive():
                window.blit(pieces[id].get_image(), pieces[id].get_position())