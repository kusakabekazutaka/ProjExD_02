import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 1.0)
    kk_img2=pg.transform.flip(kk_img,False,True)
    kk_spin={
        (0,0):pg.transform.rotozoom(kk_img, 0, 1.0),
        (-5,0):pg.transform.rotozoom(kk_img, 0, 1.0),
        (-5,-5):pg.transform.rotozoom(kk_img, 315,1.0),
        (0,-5):pg.transform.rotozoom(kk_img2, 270, 1.0),
        (5,-5):pg.transform.rotozoom(kk_img2, 225, 1.0),
        (5,0):pg.transform.rotozoom(kk_img2, 180, 1.0),
        (5,5):pg.transform.rotozoom(kk_img2, 135, 1.0),
        (0,5):pg.transform.rotozoom(kk_img2, 90, 1.0),
        (-5,5):pg.transform.rotozoom(kk_img, 45, 1.0),
    }
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bd_img = pg.Surface((20, 20))  
    bd_img.set_colorkey((0, 0, 0))  
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bd_rct = bd_img.get_rect()
    bd_rct.center = x, y 
    vx, vy = +5, +5  

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bd_rct):
            print("game over")
            kk_img = pg.image.load("ex02/fig/8.png")
            kk_img=pg.transform.rotozoom(kk_img, 0, 1.5)
            for i in range(50):
                clock.tick(50)
                screen.blit(kk_img, kk_rct)
                pg.display.update()
            return
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
        if cage(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
        screen.blit(bg_img, [0, 0])
        kk_img=kk_spin[tuple(sum_mv)]
        screen.blit(kk_img, kk_rct)
        bd_rct.move_ip(vx, vy)  
        yoko,tate=cage(bd_rct)
        if not yoko:
            vx*=-1
        if not tate:
            vy*=-1
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)
def cage(rect: pg.Rect):
    yoko, tate=True,True
    if rect.left < 0 or WIDTH < rect.right:#横 
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:#縦
        tate = False
    return yoko,tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()