import sys
import sqlite3
import pygame
from backend import Field


class Design_Field:
    def __init__(self):
        self.Field1 = Field('Kirill2005', 'Kirill2005')
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
        score = pygame.font.SysFont('', 60)
        txt_score = score.render(f'Score: {self.Field1.score}', True, (255, 165, 0))
        pygame.draw.rect(self.screen, self.WHITE_RESULTS, self.TITLE_RESULTS)
        pygame.draw.rect(self.screen, (0, 0, 255), (400, 20, 150, 40))
        pygame.draw.rect(self.screen, (0, 255, 0), (400, 70, 150, 40))
        exit1 = pygame.font.SysFont('', 30)
        txt_exit1 = exit1.render(f'Назад', True, (0, 0, 0))
        self.screen.blit(txt_exit1, (445, 80))
        new_game = pygame.font.SysFont('', 30)
        txt_new_game = new_game.render(f'Новая игра', True, (0, 0, 0))
        self.screen.blit(txt_new_game, (415, 30))
        font = pygame.font.SysFont('', 70)
        self.screen.blit(txt_score, (40, 40))
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

    def button_new_game(self):
        self.Field1.new_game()
        self.displaying_cells()


class menu:
    def __init__(self):
        self.Field1 = Field('Kirill2005', 'Kirill2005')
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

    def displaying_cells(self):
        fon = pygame.image.load('КЕ.jpg').convert()
        fon = pygame.transform.smoothscale(fon, self.screen.get_size())
        self.screen.blit(fon, (0, 0))
        pygame.draw.rect(self.screen, (255, 140, 0), (150, 350, 300, 50))
        pygame.draw.rect(self.screen, (255, 69, 0), (150, 420, 300, 50))
        button1 = pygame.font.SysFont('', 30)
        txt_button1 = button1.render(f'Играть с подсказками', True, (0, 0, 0))
        self.screen.blit(txt_button1, (190, 365))
        button2 = pygame.font.SysFont('', 30)
        txt_button2 = button2.render(f'Играть без подсказок', True, (0, 0, 0))
        self.screen.blit(txt_button2, (190, 435))
        rules = pygame.font.SysFont('', 30)
        txt_rules = rules.render(f"Правила игры", True, (255, 255, 255))
        self.screen.blit(txt_rules, (180, 480))
        rules = pygame.font.SysFont('', 20)
        txt_rules = rules.render(f"Выбирайте сторону куда хотите ходить:", True, (255, 255, 255))
        self.screen.blit(txt_rules, (60, 520))
        rules = pygame.font.SysFont('', 20)
        txt_rules = rules.render(f"нажимайте стрелочку влево если вы хотите пойти влево", True, (255, 255, 255))
        self.screen.blit(txt_rules, (60, 545))
        rules = pygame.font.SysFont('', 20)
        txt_rules = rules.render(f"нажимайте стрелочку вправо если вы хотите пойти вправо", True, (255, 255, 255))
        self.screen.blit(txt_rules, (60, 570))
        txt_rules = rules.render(f"нажимайте стрелочку вверх если вы хотите пойти вверх", True, (255, 255, 255))
        self.screen.blit(txt_rules, (60, 595))
        rules = pygame.font.SysFont('', 20)
        txt_rules = rules.render(f"нажимайте стрелочку вниз если вы хотите пойти вниз", True, (255, 255, 255))
        self.screen.blit(txt_rules, (60, 620))
        max_score = self.Field1.max_score()


def field_launch(flag=False):
    Design_Field1 = Design_Field()
    Design_Field1.displaying_cells()
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 400 and event.pos[0] <= 550 and event.pos[1] >= 20 and event.pos[1] <= 60:
                    Design_Field1.button_new_game()
                elif event.pos[0] >= 400 and event.pos[0] <= 550 and event.pos[1] >= 70 and event.pos[1] <= 110:
                    flag = False
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
    Design_Field1.button_new_game()
    menu_launch()

def menu_launch():
    Menu = menu()
    Menu.displaying_cells()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 150 and event.pos[0] <= 450 and event.pos[1] >= 350 and event.pos[1] <= 400:
                    field_launch(True)
                elif event.pos[0] >= 150 and event.pos[0] <= 450 and event.pos[1] >= 420 and event.pos[1] <= 470:
                    field_launch()
            pygame.display.update()
print(field_launch())