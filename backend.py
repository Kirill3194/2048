import pygame
import random
import sqlite3


class Field:
    def __init__(self, login, password, recommended=False):
        self.field = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.score = 0
        self.random_cube()
        self.random_cube()
        self.login = login
        self.password = password
        self.recommended = recommended
        self.left = 0
        self.right = 0
        self.top = 0
        self.down = 0


    def recommended_move(self):
        field_copy = self.field.copy()
        self.left_move()
        self.field = field_copy.copy()
        self.right_move()
        self.field = field_copy.copy()
        self.down_move()
        self.field = field_copy.copy()
        self.top_move()
        self.field = field_copy.copy()
        if self.left >= self.right and self.down <= self.left and self.left >= self.top:
            return 'left'
        elif self.right >= self.down and self.right >= self.top and self.right >= self.left:
            return 'right'
        elif self.top >= self.right and self.top >= self.down and self.top >= self.left:
            return 'top'
        elif self.down >= self.right and self.down >= self.top and self.down >= self.left:
            return 'down'

    def random_cube(self):
        cubes = []
        for y in range(len(self.field)):
            for x in range(len(self.field)):
                if self.field[y][x] == 0:
                    cubes.append(y * len(self.field) + x)
        randomcube = random.choice(cubes)
        self.field[randomcube // 4][randomcube % 4] = 2

    def left_move(self):
        summ = 0
        connection = 0
        for y in range(len(self.field)):
            for x in range(len(self.field)):
                for cord_x in range(len(self.field)):
                    change_x = cord_x - 1
                    if self.field[y][cord_x] == 0:
                        continue
                    while change_x >= 0:
                        if self.field[y][change_x] == 0:
                            self.field[y][change_x] = self.field[y][change_x + 1]
                            self.field[y][change_x + 1] = 0
                            summ += 1
                        else:
                            break
                        change_x -= 1
                if x + 1 < len(self.field) and self.field[y][x] == self.field[y][x + 1] and self.field[y][x] != 0:
                    connection += 1
                    self.field[y][x] = self.field[y][x] * 2
                    self.score += self.field[y][x]
                    self.field[y][x + 1] = 0
                    summ += 1
        if summ > 0:
            self.random_cube()
        self.left = connection

    def right_move(self):
        summ = 0
        connection = 0
        for y in range(len(self.field)):
            for x in range(len(self.field) - 1, -1, -1):
                for cord_x in range(len(self.field) - 1, -1, -1):
                    change_x = cord_x + 1
                    if self.field[y][cord_x] == 0:
                        continue
                    while change_x < len(self.field):
                        if self.field[y][change_x] == 0:
                            self.field[y][change_x] = self.field[y][change_x - 1]
                            self.field[y][change_x - 1] = 0
                            summ += 1
                        else:
                            break
                        change_x += 1
                if x - 1 >= 0 and self.field[y][x] == self.field[y][x - 1] and self.field[y][x] != 0:
                    connection += 1
                    self.field[y][x] = self.field[y][x] * 2
                    self.score += self.field[y][x]
                    self.field[y][x - 1] = 0
                    summ += 1
        if summ > 0:
            self.random_cube()
        self.right = connection

    def down_move(self):
        summ = 0
        connection = 0
        for x in range(len(self.field)):
            for y in range(len(self.field) - 1, -1, -1):
                for cord_y in range(len(self.field) - 1, -1, -1):
                    change_y = cord_y + 1
                    if self.field[cord_y][x] == 0:
                        continue
                    while change_y < len(self.field):
                        if self.field[change_y][x] == 0:
                            self.field[change_y][x] = self.field[change_y - 1][x]
                            self.field[change_y - 1][x] = 0
                            summ += 1
                        else:
                            break
                        change_y += 1
                if y - 1 >= 0 and self.field[y][x] == self.field[y - 1][x] and self.field[y][x] != 0:
                    connection += 1
                    self.field[y][x] = self.field[y][x] * 2
                    self.field[y - 1][x] = 0
                    summ += 1
                    self.score += self.field[y][x]
        if summ > 0:
            self.random_cube()
        self.down = connection

    def top_move(self):
        summ = 0
        connection = 0
        for x in range(len(self.field)):
            for y in range(len(self.field)):
                for cord_y in range(len(self.field)):
                    change_y = cord_y - 1
                    if self.field[cord_y][x] == 0:
                        continue
                    while change_y >= 0:
                        if self.field[change_y][x] == 0:
                            self.field[change_y][x] = self.field[change_y + 1][x]
                            self.field[change_y + 1][x] = 0
                            summ += 1
                        else:
                            break
                        change_y -= 1
                if y + 1 < len(self.field) and self.field[y][x] == self.field[y + 1][x] and self.field[y][x] != 0:
                    connection += 1
                    self.field[y][x] = self.field[y][x] * 2
                    self.field[y + 1][x] = 0
                    summ += 1
                    self.score += self.field[y][x]
        if summ > 0:
            self.random_cube()
        self.top = connection

    def __str__(self):
        for y in range(len(self.field)):
            print(self.field[y])
        return '------------------'

    def move(self, side):
        if side == 'l':
            self.left_move()
        if side == 'r':
            self.right_move()
        if side == 'd':
            self.down_move()
        if side == 't':
            self.top_move()
        if side == 'new':
            self.new_game()

    def new_game(self):
        self.field = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        con = sqlite3.connect("2048_accounts.db")
        cur = con.cursor()
        result = [i[:2] for i in cur.execute('SELECT login, password FROM players')]
        number = 0
        for player in range(len(result)):
            if result[player][0] == self.login and result[player][1] == self.password:
                number = player
                break
        max_score = [i[0] for i in cur.execute('SELECT max_score FROM max_score')]
        if max_score[number][0] < self.score:
            cur.execute("""UPDATE max_score
                                SET max_score = (?)
                                WHERE id_score = (?)""", [self.score, number + 1])
        self.score = 0
        self.random_cube()
        self.random_cube()


class Registration:
    def __init__(self):
        self.login = 'Гошан228'
        self.password = '332332'

    def check(self, login, password):
        con = sqlite3.connect("2048_accounts.db")
        cur = con.cursor()
        result = [i[0] for i in cur.execute('SELECT login FROM players')]
        registration_is_confirmed = True
        for player in result:
            if player == login:
                print('Пользователь под таким логином уже есть!')
                registration_is_confirmed = False
                break
        if len(login) <= 3 and registration_is_confirmed:
            registration_is_confirmed = False
            print('login слишком маленький, он должен состоять как минимум из 4 символов')
        elif len(password) <= 5 and registration_is_confirmed:
            registration_is_confirmed = False
            print('password слишком маленький, он должен состоять как минимум из 6 символов')
        return registration_is_confirmed

    def registration_player(self):
        con = sqlite3.connect("2048_accounts.db")
        cur = con.cursor()
        result = [i[0] for i in cur.execute('SELECT login FROM players')]
        if self.check(self.login, self.password):
            player = [(len(result) + 1, self.login, self.password)]
            cur.executemany('INSERT INTO players VALUES(?,?,?)', player)
            rating = [(len(result) + 1, 0)]
            cur.executemany('INSERT INTO max_score VALUES(?,?)', rating)
            con.commit()
            print('Поздравляем с успешной регистрацией!')


class Entrance:
    def __init__(self):
        self.login = 'Гошан228'
        self.password = '332332'

    def check(self):
        entrance = False
        con = sqlite3.connect("2048_accounts.db")
        cur = con.cursor()
        result = [i[:2] for i in cur.execute('SELECT login, password FROM players')]
        for player in result:
            if self.login == player[0]:
                if self.password == player[1]:
                    return True
                else:
                    print('Неверный пароль!')
                entrance = True
                break
        if entrance:
            print('Пользователя с таким логином не существует!')
        return False

    def entrance_player(self):
        if self.check():
            print("Игра началась!")
            print("Выбирайте сторону куда хотите ходить:\n"
                  "нажимайте стрелочку влево если вы хотите пойти влево\n"
                  "нажимайте стрелочку вправо если вы хотите пойти вправо\n"
                  "нажимайте стрелочку вверх если вы хотите пойти вверх\n"
                  "нажимайте стрелочку вниз если вы хотите пойти вниз\n"
                  "напишите new если вы хотите начать новую игру")
            self.Field1 = Field(self.login, self.password)
            print(self.Field1)
            a = input()
            while a != '0':
                self.Field1.move(a)
                print(self.Field1)
                a = input()