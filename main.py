import time
import settings

import pygame as pg
import random
import songs
pg.init()
pg.mixer.init()

class Game():
    def __init__(self):
        self.window = pg.display.set_mode(settings.SIZE)
        self.x = True
        self.song = songs.Songs(settings.CHRISTMAS_TREE_NOTES,settings.CHRISTMAS_TREE_DURATION)
        self.milisekund = pg.time.get_ticks()
        self.timeprezaryad = -1000
        self.watch = pg.time.Clock()

    def drawall(self):
        self.window.fill([250, 250, 250])
        for i in range(1, settings.STOLBS):
            pg.draw.line(self.window, [0,0,0],[settings.STOLBSW*i,settings.SIZE[1]],[settings.STOLBSW*i,0])
        self.song.draw(self.window)

    def upravlenieall(self):
        self.milisekund = pg.time.get_ticks()
        if self.milisekund - self.timeprezaryad >= 1000:
            self.song.create()
            self.timeprezaryad = self.milisekund

        self.song.upravlenie()


    def pushall(self):
        eventall = pg.event.get()
        for event in eventall:
            if event.type == pg.QUIT:
                self.x = False


    def gameall(self):
        while self.x == True:
            self.drawall()
            self.upravlenieall()
            self.pushall()
            pg.display.update()
            self.watch.tick(60)


game = Game()

game.gameall()


