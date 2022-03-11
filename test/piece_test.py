from os import R_OK
from turtle import position
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
                li.append((i, j))
                # if board.get_board()[i][j] == "   ":
                #     li.append((i, j))
        return li
    
class King(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
        
    def get_legal_moves(self, board: Board) -> "list[tuple[int, int]]":
        
        legal_moves = []
        
        
        
        return legal_moves
        
class Queen(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
    
    def get_legal_moves(self, board: Board) -> "list[tuple[int, int]]":
        
        legal_moves = []
                
        #! Code from Bishop class
        # We check UP/LEFT then DOWN/RIGHT then UP/RIGHT then DOWN/LEFT
        for limit_x, limit_y, x, y in zip([-1, 8, -1, 8], [-1, 8, 8, -1], [-1, 1, -1, 1], [-1, 1, 1, -1]):
            
            offset_x = x
            offset_y = y

            # As long as the neighbouring case is in the board
            while (self.position[0] + offset_x) != limit_x and (self.position[1] + offset_y) != limit_y:
                
                next_case_pos = (self.position[0] + offset_x, self.position[1] + offset_y)
                
                # We check if the color of the id on the case is different from the piece's (can be a " ")
                if board.get_id(next_case_pos)[1] != self.color:
                    
                    # We add the move to the list of legal moves
                    legal_moves.append(next_case_pos)
                    
                    # We check if it was a piece and not a blank
                    if board.get_id(next_case_pos)[0].isalpha():
                        
                        # We break the loop as we can't go further
                        break
                
                # If the piece is the same color
                else:
                    # We break the loop as we can't go further
                    break
                    
                # We increase the offsets by their value (depends on the direction)
                offset_x += x
                offset_y += y
            
        #! Code from Rook class    
        # We check UP then DOWN then RIGHT then LEFT
        for limit, pos, x, y in zip([-1, 8, 8, -1], [0, 0, 1, 1], [-1, 1, 0, 0], [0, 0, 1, -1]):
            
            # How much we increase the x value
            offset_x = x
            offset_y = y

            # As long as the neighbouring case is in the board
            while (self.position[pos] + (offset_x + offset_y)) != limit:
                
                next_case_pos = (self.position[0] + offset_x, self.position[1] + offset_y)
                
                # We check if the color of the id on the case is different from the piece's (can be a " ")
                if board.get_id(next_case_pos)[1] != self.color:
                    
                    # We add the move to the list of legal moves
                    legal_moves.append(next_case_pos)
                    
                    # We check if it was a piece and not a blank
                    if board.get_id(next_case_pos)[0].isalpha():
                        
                        # We break the loop as we can't go further
                        break
                    
                # If the piece is the same color
                else:
                    # We break the loop as we can't go further
                    break
                            
                # We increase the offset by one
                offset_x += x
                offset_y += y
        
        return legal_moves
    
class Bishop(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
    
    def get_legal_moves(self, board: Board) -> "list[tuple[int, int]]":
        
        legal_moves = []
        
        # We check UP/LEFT then DOWN/RIGHT then UP/RIGHT then DOWN/LEFT
        for limit_x, limit_y, x, y in zip([-1, 8, -1, 8], [-1, 8, 8, -1], [-1, 1, -1, 1], [-1, 1, 1, -1]):
            
            offset_x = x
            offset_y = y

            # As long as the neighbouring case is in the board
            while (self.position[0] + offset_x) != limit_x and (self.position[1] + offset_y) != limit_y:
                
                next_case_pos = (self.position[0] + offset_x, self.position[1] + offset_y)
                
                # We check if the color of the id on the case is different from the piece's (can be a " ")
                if board.get_id(next_case_pos)[1] != self.color:
                    
                    # We add the move to the list of legal moves
                    legal_moves.append(next_case_pos)
                    
                    # We check if it was a piece and not a blank
                    if board.get_id(next_case_pos)[0].isalpha():
                        
                        # We break the loop as we can't go further
                        break
                
                # If the piece is the same color
                else:
                    # We break the loop as we can't go further
                    break
                    
                # We increase the offsets by their value (depends on the direction)
                offset_x += x
                offset_y += y
            
        return legal_moves
    
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
        
        # We check UP then DOWN then RIGHT then LEFT
        for limit, pos, x, y in zip([-1, 8, 8, -1], [0, 0, 1, 1], [-1, 1, 0, 0], [0, 0, 1, -1]):
            
            # How much we increase the x value
            offset_x = x
            offset_y = y

            # As long as the neighbouring case is in the board
            while (self.position[pos] + (offset_x + offset_y)) != limit:
                
                next_case_pos = (self.position[0] + offset_x, self.position[1] + offset_y)
                
                # We check if the color of the id on the case is different from the piece's (can be a " ")
                if board.get_id(next_case_pos)[1] != self.color:
                    
                    # We add the move to the list of legal moves
                    legal_moves.append(next_case_pos)
                    
                    # We check if it was a piece and not a blank
                    if board.get_id(next_case_pos)[0].isalpha():
                        
                        # We break the loop as we can't go further
                        break
                    
                # If the piece is the same color
                else:
                    # We break the loop as we can't go further
                    break
                            
                # We increase the offset by one
                offset_x += x
                offset_y += y    
 
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
        if self.position[0] == 0 or self.position[0] == 7:
            # We don't add any legal move
            pass
        
        else:
            # We check if the first case in front is empty
            if board.get_board()[self.position[0] + offset][self.position[1]] == "   ":
                
                # We add the move to the list of legal moves
                legal_moves.append((self.position[0] + offset, self.position[1]))

                # We check if the piece has already moved during the game
                if not self.hasMoved:
                    
                    # We check if the second case in front is empty
                    if board.get_board()[self.position[0] + (2 * offset)][self.position[1]] == "   ":
                        
                        # We add the move to the list of legal moves
                        legal_moves.append((self.position[0] + (2 * offset), self.position[1]))
                        

            for limit, dir in zip([0, 7], [-1, 1]):     
            
                if self.position[1] != limit:
                    
                    if board.get_board()[self.position[0] + offset][self.position[1] + dir][1].isalpha() and board.get_board()[self.position[0] + offset][self.position[1] + dir][1] != self.color:
                        
                        legal_moves.append((self.position[0] + offset, self.position[1] + dir))
            
        return legal_moves