import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1000, 500


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    bonb=pg.Surface((20,20))
    pg.draw.circle(bonb,(255,0,0),(10,10),10)
    bonb.set_colorkey((0,0,0))
    x=random.randint(0,WIDTH)
    y=random.randint(0,HEIGHT)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bonb_rct=bonb.get_rect()
        bonb_rct.center=x,y
        screen.blit(bonb,bonb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()