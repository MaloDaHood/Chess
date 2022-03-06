import pygame

class Game:
    
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess")
        
    def get_window(self) -> pygame.surface.Surface:
        return self.window
    
    def run(self) -> None:
        running = True
        while(running) :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    running = False
                pygame.display.flip()
        pygame.quit()