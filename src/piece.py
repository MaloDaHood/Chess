import pygame
import sys
sys.path.append('../')

class Piece:
    def __init__(self, color, startingPos, isAlive) -> None:
        self.color = color
        self.startingPos = startingPos
        self.isAlive = isAlive
        self.position = startingPos
        self.image = pygame.image.load("assets/pawn" + self.color + ".png")
        
    def get_position(self) -> tuple:
        return self.position
    
    def get_image(self) -> pygame.surface.Surface:
        return self.image
    
    # Moves the piece to a different position
    def move_to(self, position) -> bool:
        # If move is legal
        self.position = position
        self.hasMoved = True;
        return True
    
    def die(self) -> None:
        self.isAlive = False
        
    def attack(self) -> None:
        pass
    
class King(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        self.image = pygame.image.load("assets/king" + self.color + ".png")
        
class Queen(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        self.image = pygame.image.load("assets/queen" + self.color + ".png")
    
class Rook(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        self.image = pygame.image.load("assets/rook" + self.color + ".png")
        
class Bishop(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        self.image = pygame.image.load("assets/bishop" + self.color + ".png")
        
class Knight(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        self.image = pygame.image.load("assets/knight" + self.color + ".png")
        
class Pawn(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        self.image = pygame.image.load("assets/pawn" + self.color + ".png")