import pygame
import sys
sys.path.append('../')

class Piece:
    def __init__(self, color :str, position :tuple) -> None:
        self.color = color # Either "B" or "W"
        self.position = position
        self.isAlive = True
        self.hasMoved = False
        self.image = pygame.image.load("assets/blank.png")
        self.value = 0
        
    def get_position(self) -> tuple:
        return self.position
    
    def get_image(self) -> pygame.surface.Surface:
        return self.image
    
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
    
    def get_value(self) -> int:
        return self.value
        
    def attack(self) -> None:
        pass
    
class King(Piece):
    def __init__(self, color :str, position :tuple) -> None:
        super().__init__(color, position)
        self.image = pygame.image.load("assets/king" + self.color + ".png")
        self.value = 6
        
class Queen(Piece):
    def __init__(self, color :str, position :tuple) -> None:
        super().__init__(color, position)
        self.image = pygame.image.load("assets/queen" + self.color + ".png")
        self.value = 5
    
class Rook(Piece):
    def __init__(self, color :str, position :tuple) -> None:
        super().__init__(color, position)
        self.image = pygame.image.load("assets/rook" + self.color + ".png")
        self.value = 4
        
class Bishop(Piece):
    def __init__(self, color :str, position :tuple) -> None:
        super().__init__(color, position)
        self.image = pygame.image.load("assets/bishop" + self.color + ".png")
        self.value = 3
        
class Knight(Piece):
    def __init__(self, color :str, position :tuple) -> None:
        super().__init__(color, position)
        self.image = pygame.image.load("assets/knight" + self.color + ".png")
        self.value = 2
        
class Pawn(Piece):
    def __init__(self, color :str, position :tuple) -> None:
        super().__init__(color, position)
        self.image = pygame.image.load("assets/pawn" + self.color + ".png")
        self.value = 1