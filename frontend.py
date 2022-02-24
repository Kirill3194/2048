import sys
import sqlite3
import pygame
from backend import Field
from backend import photoss
flaggg = True


class Design_Field:
    def __init__(self):
        self.Field1 = Field()
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
        self.colors = {'0': (110, 110, 110), '2': (255, 255, 255),
                       '4': (255, 250, 205), '8': (255, 161, 97), '16': (255, 104, 0),
                       '32': (255, 79, 0), '64': (247, 94, 37), '128': (255, 0, 0),
                       '256': (166, 202, 240), '512': (102, 102, 255), '1024': (37, 40, 80),
                       '2048': (108, 70, 117)}

    def displaying_cells(self, flag=False):
        global flaggg
        self.flag = flag
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
                if flaggg and number != 0:
                    text = font.render(f'{number}', True, (255, 255, 255))
                else:
                    text = font.render(f'{number}', True, (0, 0, 0))
                self.WIDTH = self.indent * (x + 1) + x * self.size_block
                self.HEIGTH = self.indent * (y + 1) + y * self.size_block + self.size_block
                if flaggg and number != 0:
                    fon = pygame.image.load(f'photos/{str(number)}.jpg').convert()
                    fon = pygame.transform.smoothscale(fon, (self.size_block, self.size_block))
                    self.screen.blit(fon, (self.WIDTH, self.HEIGTH))
                else:
                    pygame.draw.rect(self.screen, self.colors[str(number)],
                                     (self.WIDTH, self.HEIGTH, self.size_block, self.size_block))
                if number != 0:
                    f_w, f_h = text.get_size()
                    if flaggg and number != 0:
                        self.screen.blit(text, (
                        self.WIDTH + (((self.size_block - f_w) // 2)), self.HEIGTH + ((self.size_block - f_h + 5))))
                    else:
                        self.screen.blit(text, (
                            self.WIDTH + (((self.size_block - f_w) // 2)), self.HEIGTH + ((self.size_block - f_h) // 2)))
        if flag:
            hint = pygame.font.SysFont('', 20)
            recomend = self.Field1.recommended_move()
            if recomend == 'Невозможно никуда походить':
                txt_hint = hint.render(f'{recomend}', True, (0, 0, 0))
            else:
                txt_hint = hint.render(f'Исскуственный интеллект советует ходить {recomend}', True, (0, 0, 0))
            self.screen.blit(txt_hint, (10, 100))

    def button_new_game(self):
        self.Field1.new_game()
        self.displaying_cells(self.flag)


class menu:
    def __init__(self):
        self.Field1 = Field()
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
        pygame.draw.rect(self.screen, (102, 0, 255), (45, 30, 230, 50))
        button1 = pygame.font.SysFont('', 30)
        txt_button1 = button1.render(f'Рейтинговая таблица', True, (0, 0, 0))
        self.screen.blit(txt_button1, (55, 45))
        pygame.draw.rect(self.screen, (102, 0, 255), (305, 30, 230, 50))
        button1 = pygame.font.SysFont('', 30)
        txt_button1 = button1.render(f'Выбор кубиков', True, (0, 0, 0))
        self.screen.blit(txt_button1, (340, 45))
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


def field_launch(flag1=False):
    Design_Field1 = Design_Field()
    Design_Field1.displaying_cells(flag1)
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
                    Design_Field1.displaying_cells(flag1)
                elif event.key == pygame.K_LEFT:
                    Design_Field1.Field1.left_move()
                    Design_Field1.displaying_cells(flag1)
                elif event.key == pygame.K_UP:
                    Design_Field1.Field1.top_move()
                    Design_Field1.displaying_cells(flag1)
                elif event.key == pygame.K_DOWN:
                    Design_Field1.Field1.down_move()
                    Design_Field1.displaying_cells(flag1)
            pygame.display.update()
    Design_Field1.button_new_game()
    menu_launch()


def menu_launch():
    Menu = menu()
    Menu.displaying_cells()
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 150 and event.pos[0] <= 450 and event.pos[1] >= 350 and event.pos[1] <= 400:
                    flag1 = 1
                    flag = False
                elif event.pos[0] >= 150 and event.pos[0] <= 450 and event.pos[1] >= 420 and event.pos[1] <= 470:
                    flag1 = 2
                    flag = False
                elif event.pos[0] >= 45 and event.pos[0] <= 275 and event.pos[1] >= 30 and event.pos[1] <= 80:
                    flag = False
                    flag1 = 3
                elif event.pos[0] >= 305 and event.pos[0] <= 535 and event.pos[1] >= 30 and event.pos[1] <= 80:
                    flag = False
                    flag1 = 4
            pygame.display.update()
    if flag1 == 1:
        field_launch(True)
    elif flag1 == 2:
        field_launch()
    elif flag1 == 4:
        photos()
    else:
        rating()


def rating():
    WIDTH = 570
    HEIGTH = WIDTH + 130
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGTH))
    pygame.display.set_caption('2048')
    fon = pygame.image.load('КЕ.jpg').convert()
    fon = pygame.transform.smoothscale(fon, screen.get_size())
    screen.blit(fon, (0, 0))
    pygame.draw.rect(screen, (255, 140, 0), (400, 20, 150, 50))
    exit1 = pygame.font.SysFont('', 30)
    txt_exit1 = exit1.render(f"Выход", True, (0, 0, 0))
    screen.blit(txt_exit1, (440, 35))
    rating = open('rating.txt', 'r', encoding='utf=8')
    ratings = rating.readlines()
    rat = pygame.font.SysFont('', 40)
    txt_rat = rat.render(f"Рейтинг", True, (255, 255, 255))
    screen.blit(txt_rat, (170, 490))
    for i in range(len(ratings)):
        if '\n' in ratings[i]:
            ratings[i] = ratings[i][:-1]
    ratings.sort(key=lambda x: -int(x))
    for i in range(min(len(ratings), 6)):
        player = pygame.font.SysFont('', 40)
        txt_player = player.render(f"{i + 1}: {ratings[i]}", True, (255, 255, 255))
        screen.blit(txt_player, (180, 520 + i * 30))

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 400 and event.pos[0] <= 550 and event.pos[1] >= 20 and event.pos[1] <= 170:
                    flag = False
            pygame.display.update()
    menu_launch()


def displaying_cells_photos(a, b, c=False):
        WIDTH = 570
        HEIGTH = WIDTH + 130
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('2048')
        fon = pygame.image.load('КЕ.jpg').convert()
        fon = pygame.transform.smoothscale(fon, screen.get_size())
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (50, 620, 470, 50))
        pygame.draw.rect(screen, (255, 140, 0), (400, 20, 150, 50))
        txt = pygame.font.SysFont('', 20)
        txt_txt = txt.render(f"Выведите путь к картинке для кубика под номером {a} в формате jpg", True, (255, 255, 255))
        screen.blit(txt_txt, (45, 600))
        if c:
            txt1 = pygame.font.SysFont('', 25)
            txt1_txt = txt1.render(f"Неправильный путь к картинке!!!", True, (255, 255, 255))
            screen.blit(txt1_txt, (130, 550))
        txt = pygame.font.SysFont('', 25)
        if len(b) > 30:
            b1 = len(b)
            txt_txt = txt.render(f"{b[b1 - 30:]}", True, (0, 0, 0))
        else:
            txt_txt = txt.render(f"{b}", True, (0, 0, 0))
        screen.blit(txt_txt, (50, 640))
        exit1 = pygame.font.SysFont('', 30)
        txt_exit1 = exit1.render(f"Выход", True, (0, 0, 0))
        screen.blit(txt_exit1, (440, 35))


def photos():
    global flaggg
    need_inpit = False
    text_input = ''
    displaying_cells_photos(2, text_input)
    num = 2
    flag = True
    ceill = False
    flagg = False
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if need_inpit and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    need_inpit = False
                    if photoss(text_input, num):
                        if num + num > 2048:
                            flag = False
                            flaggg = True
                        displaying_cells_photos(num + num, text_input, ceill)
                        num += num
                    else:
                        ceill = True
                        displaying_cells_photos(num, text_input, ceill)
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[0:-1]
                else:
                    text_input += event.unicode
                displaying_cells_photos(num, text_input, ceill)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 400 and event.pos[0] <= 550 and event.pos[1] >= 20 and event.pos[1] <= 70:
                    flag = False
                if event.pos[0] >= 50 and event.pos[0] <= 520 and event.pos[1] >= 620 and event.pos[1] <= 670:
                    need_inpit = True
                    ceill = False
            pygame.display.update()
    menu_launch()



menu_launch()