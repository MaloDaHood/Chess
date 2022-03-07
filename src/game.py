import pygame
from piece import *

class Game:
    
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess")
        
    def get_window(self) -> pygame.surface.Surface:
        return self.window
        
    def is_over(self) -> bool:
        #if game is not over
        return False
    
    def update(self) -> None:
        pygame.display.flip()
    
    # Creates a dictionnary containing all the different pieces linked to their id
    def spawn_pieces(self, board :list[list[str]]) -> dict[str, Piece]:
            
        pieces = {}
        
        for i in range(len(board)):

            for j in range(len(board[i])):
                
                coord = ((j * 100), (i * 100))
                id = board[i][j]
                
                if id[0] == " ":
                    pass
                
                elif id[0] == "P":
                    pieces[id] = (Pawn(coord, id))
                    
                elif id[0] == "R":
                    pieces[id] = (Rook(coord, id))
                    
                elif id[0] == "H":
                    pieces[id] = (Knight(coord, id))
                    
                elif id[0] == "B":
                    pieces[id] = (Bishop(coord, id))
                    
                elif id[0] == "Q":
                    pieces[id] = (Queen(coord, id))
                    
                elif id[0] == "K":
                    pieces[id] = (King(coord, id))
                    
        return pieces