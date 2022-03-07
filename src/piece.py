import pygame
import sys
sys.path.append('../')

class Piece:
    def __init__(self, position :tuple[int , int], id :str) -> None:
        self.position = position
        self.id = id # Ex: "RB1" -> Rook Black 1
        self.color = id[1] # Either "B" or "W"
        self.isAlive = True
        self.hasMoved = False
        self.image = pygame.image.load("assets/" + id[:-1] + ".png")
        
    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def get_id(self) -> str:
        return self.id
    
    def get_image(self) -> pygame.surface.Surface:
        return self.image
    
    def is_alive(self) -> bool:
        return self.isAlive
    
    def die(self) -> None:
        self.isAlive = False
    
    
    
    #! NEEDS TO BE A METHOD INSIDE SUB-CLASSES
    # Moves the piece to a different position
    def move_to(self, position :tuple[int, int]) -> bool:
        # If move is legal
        self.position = position
        self.hasMoved = True;
        return True
    
class King(Piece):
    def __init__(self, position :tuple[int , int], id :str) -> None:
        super().__init__(position, id)
        pass
        
class Queen(Piece):
    def __init__(self, position :tuple[int , int], id :str) -> None:
        super().__init__(position, id)
        pass
    
class Rook(Piece):
    def __init__(self, position :tuple[int , int], id :str) -> None:
        super().__init__(position, id)
        pass
        
class Bishop(Piece):
    def __init__(self, position :tuple[int , int], id :str) -> None:
        super().__init__(position, id)
        pass        
    
class Knight(Piece):
    def __init__(self, position :tuple[int , int], id :str) -> None:
        super().__init__(position, id)
        pass
            
class Pawn(Piece):
    def __init__(self, position :tuple[int , int], id :str) -> None:
        super().__init__(position, id)
        pass