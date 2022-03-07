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
        
    # def spawn_pieces_loop(self) -> list[list[Piece]]:
        
    #     pawns = rooks = knights = bishops = queens = kings = []
                
    #     for i in range(2):
    #         color = "B" if i == 0 else "W"
            
    #         # Creation of all the pawns
    #         for j in range(8):
    #             y = 100 if i == 0 else 600
    #             pawns.append(Pawn(color, (j * 100, y)))
                
    #         y = 0 if i == 0 else 700
    #         # Creation of all the rooks, knights and bishops
    #         for j in range(2):
    #             rooks.append(Rook(color, (j * 700, y)))
    #             knights.append(Knight(color, (100 + (j * 500), y)))
    #             bishops.append(Bishop(color, (200 + (j * 300), y)))
            
    #         # Creation of the queens and kings
    #         queens.append(Queen(color, (300, y)))
    #         kings.append(King(color, (400, y)))
            
    #     return [pawns, rooks, knights, bishops, queens, kings]
    
    def spawn_pieces(self, board :list[list[str]]) -> list[Piece]:
            
        pieces = []
        
        for i in range(8):

            for j in range(8):
                
                color = board[i][j][1]
                coord = ((j * 100), (i *100))
                id = board[i][j]
                
                if board[i][j][0] == "":
                    pass
                
                elif board[i][j][0] == "P":
                    pieces.append(Pawn(color, coord, id))
                    
                elif board[i][j][0] == "R":
                    pieces.append(Rook(color, coord, id))
                    
                elif board[i][j][0] == "H":
                    pieces.append(Knight(color, coord, id))
                    
                elif board[i][j][0] == "B":
                    pieces.append(Bishop(color, coord, id))
                    
                elif board[i][j][0] == "Q":
                    pieces.append(Queen(color, coord, id))
                    
                elif board[i][j][0] == "K":
                    pieces.append(King(color, coord, id))
                    
        return pieces