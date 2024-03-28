from math import floor
import pygame as pg
import numpy as np

res = width, height = 800, 600


class Fractal:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full(self.app.res, [0, 0, 0], dtype=np.uint8)
    
    def render(self):
        pass
    
    def update(self):
        self.render()
        
        
    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)
        
    def run(self):
        self.update()
        self.draw()


class App:
    def __init__(self, WIDTH:int, HEIGHT:int):
        pg.init()
        self.res = self.width, self.height = WIDTH, HEIGHT
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        self.clock = pg.time.Clock()
        
        self.fractal = Fractal(self)
    
    def draw(self):
        self.screen.fill('black')
        self.fractal.run()
        pg.display.flip()
    
    def run(self):
        while True:
            self.draw()
            
            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f'FPS: {floor(self.clock.get_fps() * 100) / 100}')
            



def main():
    app = App(*res)
    app.run()

if __name__ == '__main__':
    main()