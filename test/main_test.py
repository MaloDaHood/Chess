import pygame
from game_test import Game
from board_test import Board
from piece_test import *

if __name__ == "__main__":
    pygame.init()
    game = Game()
    board = Board()

    window = game.get_window()
    
    # We create a dict containing every piece linked to its id
    pieces = game.spawn_pieces(board.get_board())
    
    # Main game loop
    while(game.is_running()):
        
        game.handle_inputs(board, pieces)
        
        # We display the board in the background           
        board.display_board(window)
        
        # We Check if the player is currently dragging a piece
        if game.is_dragging():
            
            pygame.mouse.set_visible(False)
            
            # We check if the player has selected an empty spot as the origin
            if board.get_id(game.get_drag_origin()) == "   ":
                # Stop the drag
                game.switch_dragging()
            # We place the piece's image at the middle of the pointer
            else:
                pieces[board.get_id(game.get_drag_origin())].center_on_pointer()

            # We display the blue and green squares
            board.display_markers(window, pieces[game.get_drag_id()].get_legal_moves(board), game.get_drag_origin())
            
        else:
            pygame.mouse.set_visible(True)
            
        # We display all the pieces on top of the board
        board.display_pieces(window, pieces)

        # We update the window each frame
        game.update()
        
        game.check_if_over()
    
    pygame.quit()