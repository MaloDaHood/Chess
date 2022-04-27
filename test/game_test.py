import pygame
from piece_test import *
from board_test import Board

class Game:
    
    def __init__(self) -> None:
        # We create the game window
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess")
        
        self.is_running = True
        self.is_dragging = False
        self.drag_origin = (-1, -1)
        self.drag_id = "   "
        self.turn = "W"
        
    # Returns True if the game is over
    def check_if_over(self) -> None:
        # if game is not over
        # self.running = True
        pass
    
    # Updates the game window
    def update(self) -> None:
        pygame.display.flip()
        
    # Changes the state of self.dragging
    def switch_dragging(self) -> None:
        self.is_dragging = not self.is_dragging
        
    # Creates a dictionnary containing all the different pieces linked to their id
    def spawn_pieces(self, board :"list[list[str]]") -> "dict[str, Piece]":
            
        pieces = {}
        
        # For each line
        for i in range(len(board)):

            # For each element
            for j in range(len(board[i])):
                
                # The current id
                id = board[i][j]
                
                # Check if the id is empty
                if id == "   ":
                    continue
                
                # Check for the first letter of each id to know what kind of piece it is
                elif id[0] == "P":
                    pieces[id] = (Pawn((i, j), id))
                    
                elif id[0] == "R":
                    pieces[id] = (Rook((i, j), id))
                    
                elif id[0] == "H":
                    pieces[id] = (Knight((i, j), id))
                    
                elif id[0] == "B":
                    pieces[id] = (Bishop((i, j), id))
                    
                elif id[0] == "Q":
                    pieces[id] = (Queen((i, j), id))
                    
                elif id[0] == "K":
                    pieces[id] = (King((i, j), id))
                    
        return pieces
    
    # Converts the coordinates from pixels to board indexes
    def convert_pos(self, position :"tuple[int, int]") -> "tuple[int, int]":
        
        # Coordinates in pixels
        x, y = position[0], position[1]
        
        i = -1
        new_position = []
            
        # For x then y
        for k in [x, y]:
            
            # Check if the value is 3 digits long 
            if len(str(k)) == 3:
                # We keep the first digit as the new value
                i = int(str(k)[0])
                
            else:
                i = 0
                
            new_position.append(i)
            
        # We switch the position of the coordinates and retun it
        return tuple(new_position)[::-1]
    
    def handle_inputs(self, board :Board, pieces :"dict[str, Piece]") -> None:
        
        # We check each event happening in the window
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.is_running = False
            
            # We check if the mouse button is pushed or released        
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP :
                self.handle_drag(board, pieces, event.type == pygame.MOUSEBUTTONDOWN)
            
    # Drives all the logic behind the dragging mechanic
    def handle_drag(self, board :Board, pieces :"dict[str, Piece]", mouse_down :bool) -> None:
            
        # We check if the mouse button is pushed
        if mouse_down:
            
            # We check if the player is not already dragging
            if not self.is_dragging:
                
                # We get the coodinates of the origin of the drag relative to the board
                self.drag_origin = self.convert_pos(pygame.mouse.get_pos())
                
                self.drag_id = board.get_id(self.drag_origin)
                
                # Debug
                print("Origin on " + str(self.drag_origin[0]) + "/" + str(self.drag_origin[1]) + " -> " + self.drag_id)
                
                # We switch to self.dragging = True if the player moved the right color
                self.is_dragging = self.drag_id[1] == self.turn
                
                # If we are dragging we toggle it on the piece object
                if self.is_dragging:
                    pieces[self.drag_id].is_dragged = True
        
        # Otherwise when the mouse button is released
        else:
        
            # We check if the player is dragging
            if self.is_dragging:
                
                # We get the coodinates of the destination of the drag relative to the board
                destination = self.convert_pos(pygame.mouse.get_pos())
                
                # Object representing the piece that is on the origin coordinates
                origin_piece = pieces[self.drag_id]
                
                # Debug
                print("Destination on " + str(destination[0]) + "/" + str(destination[1]) + " -> " + board.get_id(destination))
                        
                # We check if the origin contains a piece                
                if self.drag_id[0].isalpha():
                    
                    # We stop the piece from being in dragging state
                    origin_piece.is_dragged = False
                    
                    # Sets the position value back to the origin 
                    origin_piece.position = self.drag_origin
                    
                    # Check if we can move the piece to the destination on the window
                    if origin_piece.move_to(board, destination, pieces):
                            
                        # We move the piece to the destination on the board
                        board.move_piece(self.drag_origin, destination)
                        
                        # We switch turns
                        self.turn = "W" if self.turn == "B" else "B"
                    
                else:
                    # We put the piece back on the origin
                    origin_piece.position = self.drag_origin
                    
                    # We stop the piece from being in dragging state
                    origin_piece.is_dragged = False
                    
                self.is_dragging = False