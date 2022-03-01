import pygame

class Game:
    
    def __init__(self) -> None:
        pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess")
        
    def run(self) -> None:
        running = True
        while(running) :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    running = False
        pygame.quit()