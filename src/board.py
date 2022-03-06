class Board:
    
    def __init__(self) -> None:
        self.board = [[" " for j in range(8)] for i in range(8)]
    
    def display(self) -> None:
        fenetre = pygame.display.set_mode((800, 800), RESIZABLE)
        pygame.display.set_caption("Pygame Window")
        
        fond = pygame.image.load("board.png").convert()
        fond = pygame.transform.scale(fond, (800, 800))
        fenetre.blit(fond, (0,0))

        pygame.display.flip()
        
    def draw(self) -> None:
        for line in self.board:
            for case in line:
                print(case + '|', end="")
            print()