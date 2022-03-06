import pygame

class Game:
    
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess")
        
    def get_window(self) -> pygame.surface.Surface:
        return self.window
        
    def is_over(self) -> bool:
        #if game is not over
        return False
    
    def update(self) -> None:
        pygame.display.flip()