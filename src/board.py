class Board:
    
    def __init__(self) -> None:
        self.board = [[" " for j in range(8)] for i in range(8)]
    
    def draw(self) -> None:
        for line in self.board:
            for case in line:
                print(case + '|', end="")
            print()