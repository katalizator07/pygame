import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1200, 800
WH = 340
HH = 300

GREEN = (85, 165, 75)
WHITE_BLUE = (245, 240, 255)
GREY = (140, 140, 140)
BLUE = (90, 160, 200)
SUN = (255, 240, 0)
BRAUN = (105, 95, 45)
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLUE)  # заливка фона
pg.display.set_caption("Игра")
clock = pg.time.Clock()


pg.draw.polygon(screen, GREEN, [[0, HEIGHT/2], [0, HEIGHT], [WIDTH, HEIGHT], [WIDTH, HEIGHT/2]])
pg.draw.circle(screen, SUN, (150,150), 60)
pg.draw.rect(screen, GREY, (WIDTH / 2 + 60, 190, WH, HH))
pg.draw.line(screen, SUN, (150, 140), (300, 125,), 3)
pg.draw.line(screen, SUN, (150, 170), (300, 250), 3)
pg.draw.line(screen, SUN, (150, 150), (150, 280), 3)
pg.draw.polygon(screen, BRAUN, [[WIDTH / 2 + 60, 190], [WIDTH / 2 + 60 + WH/2, 70], [WIDTH / 2 + 60 + WH, 190]])


# отображаем нарисованные объекты
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()
