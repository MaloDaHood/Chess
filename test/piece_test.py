import pygame
from board_test import Board
import sys
sys.path.append('../')

class Piece:
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        self.position = position
        self.px_position = (position[1] * 100, position[0] * 100)
        self.id = id # Ex: "RB1" -> Rook Black 1
        self.color = id[1] # Either "B" or "W"
        self.isAlive = True
        self.hasMoved = False
        self.isDragged = False
        # We load the image using the id without the last char 
        self.image = pygame.image.load("assets/" + id[:-1] + ".png")
        
    # Returns the position of the piece relative to the board
    def get_position(self) -> "tuple[int, int]":
        return self.position
    
    # Sets the position of the piece relative to the board
    def set_position(self, position :"tuple[int, int]") -> None:
        self.position = position
        
    # Returns the position of the piece in pixels
    def get_px_position(self) -> "tuple[int, int]":
        return self.px_position
    
    # Centers the piece's image onto the mouse pointer
    def center_on_pointer(self) -> None:
        # We offset by 50 pixels because the image is 100*100 px 
        self.px_position = (pygame.mouse.get_pos()[0] - 50, pygame.mouse.get_pos()[1] - 50)
    
    # Returns the piece's id
    def get_id(self) -> str:
        return self.id
    
    # Returns the piece's image
    def get_image(self) -> pygame.surface.Surface:
        return self.image
    
    # Returns True if the piece is alive
    def is_alive(self) -> bool:
        return self.isAlive
    
    # Kills the piece
    def die(self) -> None:
        self.isAlive = False
        
    # Returns True if the piece is currently being dragged
    def is_dragged(self) -> bool:
        return self.isDragged
    
    # Sets the state of self.isDragged
    def set_drag(self, is_dragged :bool) -> None:
        self.isDragged = is_dragged
    
    # Moves the piece to a different position and returns True if it worked
    def move_to(self, board :Board, destination :"tuple[int, int]") -> bool:
        print("Legal moves : " + str(self.get_legal_moves(board)))
        for move in self.get_legal_moves(board):
            if destination == move:
                self.position = destination
                self.hasMoved = True;
                return True
        return False
    
    # Makes a list of all the legal moves possible
    def get_legal_moves(self, board :Board) -> "list[tuple[int, int]]":
        li = []
        for i in range(8):
            for j in range(8):
                if board.get_board()[i][j] == "   ":
                    li.append((i, j))
        return li
    
class King(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
        
class Queen(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
    
class Bishop(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass        
    
class Knight(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
    
class Rook(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
    
    # Makes a list of all possible legal moves
    def get_legal_moves(self, board: Board) -> "list[tuple[int, int]]":
        
        legal_moves = []
        
        # DOWN
        # We check if we are on the last case
        if self.position[0] != 7:
            
            # How much we increase the x value
            offset = 1
            
            # As long as the neighbouring case is free
            while (self.position[0] + offset) <= 7 and board.get_board()[self.position[0] + offset][self.position[1]] == "   ":
                
                # We add the move to the list of legal moves
                legal_moves.append((self.position[0] + offset, self.position[1]))
                
                # We increase the offset by one
                offset += 1
                                
        # RIGHT
        # We check if we are on the last case
        if self.position[1] != 7:
            
            # How much we increase the y value
            offset = 1
            
            # As long as the neighbouring case is free
            while (self.position[1] + offset) <= 7 and board.get_board()[self.position[0]][self.position[1] + offset] == "   ":
                
                # We add the move to the list of legal moves
                legal_moves.append((self.position[0], self.position[1] + offset))
                
                # We increase the offset by one
                offset += 1
                    
        # UP
        # We check if we are on the last case
        if self.position[0] != 0:
        
            # How much we increase the x value
            offset = -1

            # As long as the neighbouring case is free
            while (self.position[0] + offset) >= 0 and board.get_board()[self.position[0] + offset][self.position[1]] == "   ":
                
                # We add the move to the list of legal moves
                legal_moves.append((self.position[0] + offset, self.position[1]))
                
                # We decrease the offset by one
                offset -= 1
                             
        # LEFT
        # We check if we are on the last case
        if self.position[1] != 0:
            
            # How much we increase the y value
            offset = -1

            # As long as the neighbouring case is free
            while (self.position[1] + offset) >= 0 and board.get_board()[self.position[0]][self.position[1] + offset] == "   ":
                
                # We add the move to the list of legal moves
                legal_moves.append((self.position[0], self.position[1] + offset))
                
                # We decrease the offset by one
                offset -= 1
        
        return legal_moves
        
class Pawn(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass

    # Makes a list of all possible legal moves
    def get_legal_moves(self, board :Board) -> "list[tuple[int, int]]":
        
        legal_moves = []
        
        # Whether the pawn can go up or down
        offset = -1 if self.color == "W" else 1
        
        # We check if we are on the last case
        if (self.position[0] + (1 * offset)) == 0 or (self.position[0] + (1 * offset)) == 8:
            # We don't add any legal move
            pass
        
        else:
            # We check if the first case in front of it is empty
            if board.get_board()[self.position[0] + (1 * offset)][self.position[1]] == "   ":
                
                # We add the move to the list of legal moves
                legal_moves.append((self.position[0] + (1 * offset), self.position[1]))

                # We check if the piece already have moved during the game
                if not self.hasMoved:
                    
                    # We check if the second case in front is empty
                    if board.get_board()[self.position[0] + (2 * offset)][self.position[1]] == "   ":
                        
                        # We add the move to the list of legal moves
                        legal_moves.append((self.position[0] + (2 * offset), self.position[1]))
            
        return legal_moves