import pygame
import sys
sys.path.append('../')

class Piece:
    def __init__(self, color :str, position :tuple, id :str) -> None:
        self.color = color # Either "B" or "W"
        self.position = position
        self.id = id # Ex: RB1 -> Rook Black 1
        self.isAlive = True
        self.hasMoved = False
        self.image = pygame.image.load("assets/blank.png")
        
    def get_position(self) -> tuple:
        return self.position
    
    def get_image(self) -> pygame.surface.Surface:
        return self.image
    
    #! NEEDS TO BE A METHOD INSIDE SUB-CLASSES
    # Moves the piece to a different position
    def move_to(self, position :tuple) -> bool:
        # If move is legal
        self.position = position
        self.hasMoved = True;
        return True
    
    def die(self) -> None:
        self.isAlive = False
        
    def is_alive(self) -> bool:
        return self.isAlive
    
    def get_id(self) -> str:
        return self.id
    
class King(Piece):
    def __init__(self, color :str, position :tuple, id :str) -> None:
        super().__init__(color, position, id)
        self.image = pygame.image.load("assets/king" + self.color + ".png")
        
class Queen(Piece):
    def __init__(self, color :str, position :tuple, id :str) -> None:
        super().__init__(color, position, id)
        self.image = pygame.image.load("assets/queen" + self.color + ".png")
    
class Rook(Piece):
    def __init__(self, color :str, position :tuple, id :str) -> None:
        super().__init__(color, position, id)
        self.image = pygame.image.load("assets/rook" + self.color + ".png")
        
class Bishop(Piece):
    def __init__(self, color :str, position :tuple, id :str) -> None:
        super().__init__(color, position, id)
        self.image = pygame.image.load("assets/bishop" + self.color + ".png")
        
class Knight(Piece):
    def __init__(self, color :str, position :tuple, id :str) -> None:
        super().__init__(color, position, id)
        self.image = pygame.image.load("assets/knight" + self.color + ".png")
        
class Pawn(Piece):
    def __init__(self, color :str, position :tuple, id :str) -> None:
        super().__init__(color, position, id)
        self.image = pygame.image.load("assets/pawn" + self.color + ".png")
