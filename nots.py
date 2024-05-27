import pygame
class Note():
    photonots = [[pygame.image.load('short_tile.png'), pygame.image.load('short_tile_pressed.png')],
                 [pygame.image.load('long_tile.png'), pygame.image.load('long_tile_pressed.png')]]
    def __init__(self, coordinat,name,time):
        self.model = Note.photonots[time - 1][0]
        h = self.model.get_height()
        w = self.model.get_width()
        self.square = pygame.rect.Rect(coordinat, [w, h])
        self.speedy = 3
    def draw(self, window):
        window.blit(self.model, self.square)

    def upravlenie(self):
        self.square.y += self.speedy
