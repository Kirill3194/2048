import sys

import pygame
from backend import Field


class Design_Field:
    def __init__(self):
        self.Field1 = Field('aaa', 'aaa')
        self.WHITE_RESULTS = (255, 255, 255)
        self.blocks = 4
        self.size_block = 130
        self.indent = 10
        self.WIDTH = self.blocks * self.size_block + (self.blocks + 1) * self.indent
        self.HEIGTH = self.WIDTH + 130
        self.TITLE_RESULTS = pygame.Rect(0, 0, self.WIDTH, 130)
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGTH))
        pygame.display.set_caption('2048')
        self.colors = {'0':(110, 110, 110), '2':(255, 255, 255),
                  '4':(255, 250, 205), '8':(255, 161, 97), '16':(255, 104, 0),
                  '32':(255, 79, 0), '64':(247, 94, 37), '128':(255, 0, 0),
                  '256':(166, 202, 240), '512':(102, 102, 255), '1024':(37, 40, 80),
                  '2048':(108, 70, 117)}

    def displaying_cells(self):
        print(self.Field1.field)
        pygame.draw.rect(self.screen, self.WHITE_RESULTS, self.TITLE_RESULTS)
        font = pygame.font.SysFont('', 70)
        for y in range(self.blocks):
            for x in range(self.blocks):
                number = self.Field1.field[y][x]
                text = font.render(f'{number}', True, (0, 0, 0))
                self.WIDTH = self.indent * (x + 1) + x * self.size_block
                self.HEIGTH = self.indent * (y + 1) + y * self.size_block + self.size_block
                pygame.draw.rect(self.screen, self.colors[str(number)], (self.WIDTH, self.HEIGTH, self.size_block, self.size_block))
                if number != 0:
                    f_w, f_h = text.get_size()
                    self.screen.blit(text, (self.WIDTH + (((self.size_block - f_w) // 2)), self.HEIGTH + ((self.size_block - f_h) // 2)))
Design_Field1 = Design_Field()
Design_Field1.displaying_cells()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Design_Field1.Field1.right_move()
                Design_Field1.displaying_cells()
            elif event.key == pygame.K_LEFT:
                Design_Field1.Field1.left_move()
                Design_Field1.displaying_cells()
            elif event.key == pygame.K_UP:
                Design_Field1.Field1.top_move()
                Design_Field1.displaying_cells()
            elif event.key == pygame.K_DOWN:
                Design_Field1.Field1.down_move()
                Design_Field1.displaying_cells()
        pygame.display.update()