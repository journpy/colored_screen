import pygame as pg

pg.init()

screen = pg.display.set_mode((1280, 720))
running = True

#colors
BLACK =	(0,0,0)
WHITE =	(255,255,255)
RED = (255,0,0)
LIME = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
FUCHSIA	= (255,0,255)
SILVER = (192,192,192)
GRAY = (128,128,128)
MAROON	= (128,0,0)
OLIVE = (128,128,0)
GREEN =	(0,128,0)
PURPLE = (128,0,128)
TEAL =	(0,128,128)
NAVY =	(0,0,128)

background = WHITE

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                background = BLACK
            if event.key == pg.K_w:
                background = WHITE
            if event.key == pg.K_r:
                background = RED
            if event.key == pg.K_l:
                background = LIME
            if event.key == pg.K_b:
                background = BLUE
            if event.key == pg.K_y:
                background = YELLOW
            if event.key == pg.K_c:
                background = CYAN
            if event.key == pg.K_f:
                background = FUCHSIA
            if event.key == pg.K_s:
                background = SILVER
            if event.key == pg.K_a:
                background = GRAY
            if event.key == pg.K_m:
                background = MAROON
            if event.key == pg.K_o:
                background = OLIVE
            if event.key == pg.K_g:
                background = GREEN
            if event.key == pg.K_p:
                background = PURPLE
            if event.key == pg.K_t:
                background = TEAL
            if event.key == pg.K_n:
                background = NAVY
                
    screen.fill(background)
    pg.display.update()

pg.quit()
