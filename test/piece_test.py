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
        self.is_alive = True
        self.has_moved = False
        self.is_dragged = False
        
        # We load the image using the id without the last char 
        self.image = pygame.image.load("assets/" + id[:-1] + ".png")
    
    # Centers the piece's image onto the mouse pointer
    def center_on_pointer(self) -> None:
        # We offset by 50 pixels because the image is 100*100 px 
        self.px_position = (pygame.mouse.get_pos()[0] - 50, pygame.mouse.get_pos()[1] - 50)
    
    # Kills the piece
    def die(self, board :Board) -> None:
        self.is_alive = False
        board.set_case(self.position, "   ")
    
    # Moves the piece to a different position and returns True if it worked
    def move_to(self, board :Board, destination :"tuple[int, int]", pieces :"dict[str, Piece]") -> bool:
        
        print("Legal moves : " + str(self.get_legal_moves(board)))
        
        for move in self.get_legal_moves(board):
            
            if destination == (move[0], move[1]):
                
                self.position = destination
                self.has_moved = True;
                
                if move[2] != "NONE":
                    
                    pieces[move[2]].die(board)
                
                return True
            
        return False
    
    # Makes a list of all the legal moves possible
    def get_legal_moves(self, board :Board) -> "list[list]":
        # We return an empty list as the method is used by the sub-classes
        return []
    
class King(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
        
    def get_legal_moves(self, board: Board) -> "list[list]":
        
        legal_moves = []
        
        # We check UP then DOWN then RIGHT then LEFT
        for limit, pos, offset_x, offset_y in zip([-1, 8, 8, -1], [0, 0, 1, 1], [-1, 1, 0, 0], [0, 0, 1, -1]):
            
            # We check if the neighbouring case is in the board
            if self.position[pos] + (offset_x + offset_y) != limit:
                
                next_case_pos = (self.position[0] + offset_x, self.position[1] + offset_y)
                
                # We check if the color of the id on the case is different from the piece's (can be a " ")
                if board.get_id(next_case_pos)[1] != self.color:
                    
                    # We add the move to the list of legal moves
                    legal_moves.append([next_case_pos[0], next_case_pos[1], "NONE"])
                    
                    if board.get_id(next_case_pos)[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id(next_case_pos)
        
        # We check UP/LEFT then DOWN/RIGHT then UP/RIGHT then DOWN/LEFT
        for limit_x, limit_y, offset_x, offset_y in zip([-1, 8, -1, 8], [-1, 8, 8, -1], [-1, 1, -1, 1], [-1, 1, 1, -1]):
            
            # We check if the neighbouring case is in the board
            if self.position[0] + offset_x != limit_x and self.position[1] + offset_y != limit_y:
                
                next_case_pos = (self.position[0] + offset_x, self.position[1] + offset_y)
                
                # We check if the color of the id on the case is different from the piece's (can be a " ")
                if board.get_id(next_case_pos)[1] != self.color:
                    
                    # We add the move to the list of legal moves
                    legal_moves.append([next_case_pos[0], next_case_pos[1], "NONE"])
                    
                    if board.get_id(next_case_pos)[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id(next_case_pos)
                    
        #! Castling
        
        
        return legal_moves
        
class Queen(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
    
    def get_legal_moves(self, board: Board) -> "list[list]":
        
        legal_moves = []
        
        # We create a fake Rook and a fake Bishop objects
        fake_rook = Rook(self.position, "R" + self.color + "0")
        fake_bishop = Bishop(self.position, "B" + self.color + "0")
        
        # We use their legal moves depending on the queen's position and color
        legal_moves += fake_rook.get_legal_moves(board)
        legal_moves += fake_bishop.get_legal_moves(board)
        
        return legal_moves
    
class Bishop(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
    
    def get_legal_moves(self, board: Board) -> "list[list]":
        
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
                    legal_moves.append([next_case_pos[0], next_case_pos[1], "NONE"])
                    
                    # We check if it was a piece and not a blank
                    if board.get_id(next_case_pos)[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id(next_case_pos)
                        
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
    
    def get_legal_moves(self, board: Board) -> "list[list]":
        
        legal_moves = []
        
        if self.position[0] + 2 <= 7:
            
            if self.position[1] + 1 <= 7:
                
                if board.get_id((self.position[0] + 2, self.position[1] + 1))[1] != self.color:
                    
                    legal_moves.append([self.position[0] + 2, self.position[1] + 1, "NONE"])
                    
                    if board.get_id((self.position[0] + 2, self.position[1] + 1))[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id((self.position[0] + 2, self.position[1] + 1))
                    
            if self.position[1] - 1 >= 0:
                
                if board.get_id((self.position[0] + 2, self.position[1] - 1))[1] != self.color:
                    
                    legal_moves.append([self.position[0] + 2, self.position[1] - 1, "NONE"])
                    
                    if board.get_id((self.position[0] + 2, self.position[1] - 1))[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id((self.position[0] + 2, self.position[1] - 1))
        
        if self.position[0] - 2 >= 0:
            
            if self.position[1] + 1 <= 7:
                
                if board.get_id((self.position[0] - 2, self.position[1] + 1))[1] != self.color:
                    
                    legal_moves.append([self.position[0] - 2, self.position[1] + 1, "NONE"])
                    
                    if board.get_id((self.position[0] - 2, self.position[1] + 1))[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id((self.position[0] - 2, self.position[1] + 1))
                    
            if self.position[1] - 1 >= 0:
                
                if board.get_id((self.position[0] - 2, self.position[1] - 1))[1] != self.color:
                    
                    legal_moves.append([self.position[0] - 2, self.position[1] - 1, "NONE"])
                    
                    if board.get_id((self.position[0] - 2, self.position[1] - 1))[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id((self.position[0] - 2, self.position[1] - 1))
                    
        if self.position[1] + 2 <= 7:
            
            if self.position[0] + 1 <= 7:
                
                if board.get_id((self.position[0] + 1, self.position[1] + 2))[1] != self.color:
                    
                    legal_moves.append([self.position[0] + 1, self.position[1] + 2, "NONE"])
                    
                    if board.get_id((self.position[0] + 1, self.position[1] + 2))[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id((self.position[0] + 1, self.position[1] + 2))
                    
            if self.position[0] - 1 >= 0:
                
                if board.get_id((self.position[0] - 1, self.position[1] + 2))[1] != self.color:
                    
                    legal_moves.append([self.position[0] - 1, self.position[1] + 2, "NONE"])
                    
                    if board.get_id((self.position[0] - 1, self.position[1] + 2))[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id((self.position[0] - 1, self.position[1] + 2))
                    
        if self.position[1] - 2 >= 0:
            
            if self.position[0] + 1 <= 7:
                
                if board.get_id((self.position[0] + 1, self.position[1] - 2))[1] != self.color:
                    
                    legal_moves.append([self.position[0] + 1, self.position[1] - 2, "NONE"])
                    
                    if board.get_id((self.position[0] + 1, self.position[1] - 2))[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id((self.position[0] + 1, self.position[1] - 2))
                    
            if self.position[0] - 1 >= 0:
                
                if board.get_id((self.position[0] - 1, self.position[1] - 2))[1] != self.color:
                    
                    legal_moves.append([self.position[0] - 1, self.position[1] - 2, "NONE"])
                    
                    if board.get_id((self.position[0] - 1, self.position[1] - 2))[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id((self.position[0] - 1, self.position[1] - 2))
        
        return legal_moves
    
class Rook(Piece):
    def __init__(self, position :"tuple[int , int]", id :str) -> None:
        super().__init__(position, id)
        pass
    
    # Makes a list of all possible legal moves
    def get_legal_moves(self, board: Board) -> "list[list]":
        
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
                    legal_moves.append([next_case_pos[0], next_case_pos[1], "NONE"])
                    
                    # We check if it was a piece and not a blank
                    if board.get_id(next_case_pos)[0].isalpha():
                        
                        legal_moves[-1][2] = board.get_id(next_case_pos)
                        
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
    def get_legal_moves(self, board :Board) -> "list[tuple[int, int, str]]":
        
        legal_moves = []
        
        # Whether the pawn can go up or down
        offset = -1 if self.color == "W" else 1
        
        # We check if we are on the last case
        if self.position[0] == 0 or self.position[0] == 7:
            
            print("new piece")
            
            # We don't add any legal move
            pass
        
        else:
            # We check if the first case in front is empty
            if board.board[self.position[0] + offset][self.position[1]] == "   ":
                
                # We add the move to the list of legal moves
                legal_moves.append([self.position[0] + offset, self.position[1], "NONE"])

                # We check if the piece has already moved during the game
                if not self.has_moved:
                    
                    # We check if the second case in front is empty
                    if board.board[self.position[0] + (2 * offset)][self.position[1]] == "   ":
                        
                        # We add the move to the list of legal moves
                        legal_moves.append([self.position[0] + (2 * offset), self.position[1], "NONE"])
                        
            # We check if we can attack on the LEFT then the RIGHt
            for limit, dir in zip([0, 7], [-1, 1]):     
            
                next_case_pos = (self.position[0] + offset, self.position[1] + dir)
            
                # We check that we are not on the edge of the board
                if self.position[1] != limit:
                    
                    # We check if the case has an ennemy piece on it
                    if board.get_id(next_case_pos)[0].isalpha() and board.get_id(next_case_pos)[1] != self.color:
                        
                        # We add the move to the list of legal moves
                        legal_moves.append([next_case_pos[0], next_case_pos[1], board.get_id(next_case_pos)])
                    
                    if board.get_id(next_case_pos) == "   " and board.get_id((self.position[0], self.position[1] + dir))[0].isalpha() and board.get_id((self.position[0], self.position[1] + dir))[1] != self.color:
                        
                        legal_moves.append([next_case_pos[0], next_case_pos[1], board.get_id((self.position[0], self.position[1] + dir))])
            
        return legal_moves