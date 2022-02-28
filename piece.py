class Piece:
    def __init__(self, color, startingPos, isAlive) -> None:
        self.color = color
        self.startingPos = startingPos
        self.isAlive = isAlive
        self.position = startingPos
    
class King(Piece):
    def __init__(self, color, startingPos, isAlive, hasMoved) -> None:
        super().__init__(color, startingPos, isAlive)
        self.hasMoved = hasMoved
        
class Queen(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        pass
        
class Rook(Piece):
    def __init__(self, color, startingPos, isAlive, hasMoved) -> None:
        super().__init__(color, startingPos, isAlive)
        self.hasMoved = hasMoved
        
class Bishop(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        pass
        
class Knight(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        pass
        
class Pawn(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        pass