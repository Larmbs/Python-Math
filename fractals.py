import pygame as pg

rules = [
    ('A', 'AB'),
    ('B', 'A')
]

behaviors = [
    ()
]


def createFractal(depth, seed):
    val = seed
    for _ in range(depth):
        val = applyRules(val)
    return val
    
def applyRules(string):
    res = ''
    for chr in string:
        for rule in rules:
            res += rule[1] if rule[0] == chr else ""
    return res
    
class Fractal:
    def __init__(self, data:str, lineColor, lineWidth, pos):
        self.data = data
        self.lineColor = lineColor
        self.lineWidth = lineWidth
        self.x, self.y = pos
    
    def draw():
        
    
    
    
class App:
    def __init__(self, WIDTH=800, HEIGHT=600):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        
        self.fractal = Fractal()

    def run():
        while True:
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip() 
            

class App:
    def __init__(self, WIDTH=800, HEIGHT=800, CELL_SIZE=8):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()
        
        self.CELL_SIZE = CELL_SIZE
        self.ROWS, self.COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
        
        self.grid = [[0 for col in range(self.COLS)] for row in range(self.ROWS)]
        
        self.ant = Ant(self, (self.COLS // 2, self.ROWS // 2), color=pg.Color('orange'))
        
    def run(self):
        while True:
            self.ant.run()
            
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            
            pg.display.flip() 
            self.clock.tick()