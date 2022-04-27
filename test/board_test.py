from piece_test import *
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
        
        self.tboard = [
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "PW1", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "PB1", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
        ]
          
        # Creates the background board
        self.background = pygame.image.load("assets/board.png")
        self.background = pygame.transform.scale(self.background, (800, 800))
    
    # Displays the board on full window
    def display_board(self, window :pygame.surface.Surface) -> None:
        window.blit(self.background, (0,0))
        
    def set_case(self, position :"tuple[int, int]", new_id :str) -> None:
        self.board[position[0]][position[1]] = new_id
        
    # Displays all pieces at their own positions (in pixels)
    def display_pieces(self, window :pygame.surface.Surface, pieces :"dict[str, Piece]") -> None:
        for id in pieces:
            # We don't display the piece if it's dead
            if pieces[id].is_alive:
                # We check if the pieces has pixels coordinates or not
                if pieces[id].is_dragged:
                    window.blit(pieces[id].image, pieces[id].px_position)
                else:
                    window.blit(pieces[id].image, (pieces[id].position[1] * 100, pieces[id].position[0] * 100))
                
    # Moves a piece from origin to destination in the board
    def move_piece(self, origin :"tuple[int, int]", destination :"tuple[int, int]") -> None:
        # Destination takes the id from origin
        self.board[destination[0]][destination[1]] = self.board[origin[0]][origin[1]]
        # Origin gets a blank id
        self.board[origin[0]][origin[1]] = "   "
        
    # Returns the id at position in the board
    def get_id(self, position :"tuple[int, int]") -> str:
        return self.board[position[0]][position[1]]
    
    # Displays a square on the origin of the player's drag and squares on each legal move
    def display_markers(self, window :pygame.surface.Surface, legal_moves :"list[list]", position :"tuple[int, int]") -> None:
        
        # We display a square on the origin of the drag
        pygame.draw.rect(window, (96,193,216), pygame.Rect((position[1] * 100) + 10, (position[0] * 100) + 10, 80, 80))
        
        # We display a square on each legal move
        for move in legal_moves:
            
            if move[2].isalpha():
            
                pygame.draw.rect(window, (0,193,0), pygame.Rect((move[1] * 100) + 10, (move[0] * 100) + 10, 80, 80))
                
            else:
                
                pygame.draw.rect(window, (193,0,0), pygame.Rect((move[1] * 100) + 10, (move[0] * 100) + 10, 80, 80))
                