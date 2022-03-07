from asyncio.windows_events import NULL
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
    
    def spawn_pieces(self, board :list[list[str]]) -> list[Piece]:
            
        pieces = []
        
        for i in range(len(board)):

            for j in range(len(board[i])):
                
                coord = ((j * 100), (i * 100))
                id = board[i][j]
                
                if id[0] == " ":
                    pass
                
                elif id[0] == "P":
                    pieces.append(Pawn(coord, id))
                    
                elif id[0] == "R":
                    pieces.append(Rook(coord, id))
                    
                elif id[0] == "H":
                    pieces.append(Knight(coord, id))
                    
                elif id[0] == "B":
                    pieces.append(Bishop(coord, id))
                    
                elif id[0] == "Q":
                    pieces.append(Queen(coord, id))
                    
                elif id[0] == "K":
                    pieces.append(King(coord, id))
                    
        return pieces