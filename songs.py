import random

import nots
import settings
class Songs():
    def __init__(self,name,time):
        self.name = name
        self.time = time
        self.nots = []
        self.chit = 0

    def create(self):
        x = settings.STOLBSW*random.randint(0,settings.STOLBS)
        i = nots.Note([x, 0],self.name[self.chit],self.time[self.chit])
        self.nots.append(i)
        self.chit += 1

    def draw(self,window):
        for i in self.nots:
            i.draw(window)

    def upravlenie(self):
        for i in self.nots:
            i.upravlenie()
