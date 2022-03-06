class Piece:
    def __init__(self, color, startingPos, isAlive) -> None:
        self.color = color
        self.startingPos = startingPos
        self.isAlive = isAlive
        self.position = startingPos
        
    # Moves the piece to a different position
    def moveTo(self, position) -> bool:
        # If move is legal
        self.position = position
        self.hasMoved = True;
        return True
    
class King(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        pass
        
class Queen(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        pass
        
class Rook(Piece):
    def __init__(self, color, startingPos, isAlive) -> None:
        super().__init__(color, startingPos, isAlive)
        pass
        
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