import pygame
import random
import sqlite3
import copy
import os
import shutil


class Field:
    def __init__(self, recommended=False):
        self.field = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.score = 0
        self.random_cube()
        self.random_cube()
        self.login = 'a'
        self.password = 'a'
        self.recommended = recommended
        self.left = 0
        self.right = 0
        self.top = 0
        self.down = 0
        self.left_s = 0
        self.right_s = 0
        self.top_s = 0
        self.down_s = 0

    def random_cube(self):
        cubes = []
        for y in range(len(self.field)):
            for x in range(len(self.field)):
                if self.field[y][x] == 0:
                    cubes.append(y * len(self.field) + x)
        randomcube = random.choice(cubes)
        self.field[randomcube // 4][randomcube % 4] = 2

    def left_move(self, flag=False):
        summ = 0
        connection = 0
        if flag:
            copy_l = copy.deepcopy(self.field)
            copy_s = self.score
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
                if x + 1 < len(self.field) and self.field[y][x] == self.field[y][x + 1] and self.field[y][x] != 0 and self.field[y][x] != 2048:
                    connection += 1
                    self.field[y][x] = self.field[y][x] * 2
                    self.score += self.field[y][x]
                    self.field[y][x + 1] = 0
                    summ += 1
        if summ > 0:
            self.random_cube()
        if flag:
            self.field = copy.deepcopy(copy_l)
            self.score = copy_s
        self.left = connection
        self.left_s = summ

    def right_move(self, flag=False):
        summ = 0
        connection = 0
        if flag:
            copy_l = copy.deepcopy(self.field)
            copy_s = self.score
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
                if x - 1 >= 0 and self.field[y][x] == self.field[y][x - 1] and self.field[y][x] != 0 and self.field[y][x] != 2048:
                    connection += 1
                    self.field[y][x] = self.field[y][x] * 2
                    self.score += self.field[y][x]
                    self.field[y][x - 1] = 0
                    summ += 1
        if summ > 0:
            self.random_cube()
        if flag:
            self.field = copy.deepcopy(copy_l)
            self.score = copy_s
        self.right = connection
        self.right_s = summ

    def down_move(self, flag=False):
        summ = 0
        connection = 0
        if flag:
            copy_l = copy.deepcopy(self.field)
            copy_s = self.score
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
                if y - 1 >= 0 and self.field[y][x] == self.field[y - 1][x] and self.field[y][x] != 0 and self.field[y][x] != 2048:
                    connection += 1
                    self.field[y][x] = self.field[y][x] * 2
                    self.field[y - 1][x] = 0
                    summ += 1
                    self.score += self.field[y][x]
        if summ > 0:
            self.random_cube()
        if flag:
            self.field = copy.deepcopy(copy_l)
            self.score = copy_s
        self.down = connection
        self.down_s = summ

    def top_move(self, flag=False):
        if flag:
            copy_l = copy.deepcopy(self.field)
            copy_s = self.score
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
                if y + 1 < len(self.field) and self.field[y][x] == self.field[y + 1][x] and self.field[y][x] != 0 and self.field[y][x] != 2048:
                    connection += 1
                    self.field[y][x] = self.field[y][x] * 2
                    self.field[y + 1][x] = 0
                    summ += 1
                    self.score += self.field[y][x]
        if summ > 0:
            self.random_cube()
        if flag:
            self.field = copy.deepcopy(copy_l)
            self.score = copy_s
        self.top = connection
        self.top_s = summ

    def __str__(self):
        for y in range(len(self.field)):
            print(self.field[y])
        return '------------------'

    def new_game(self):
        self.field = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        rating = open('rating.txt', 'a', encoding='utf-8')
        rating.write('\n' + str(self.score))
        rating.close()
        self.score = 0
        self.random_cube()
        self.random_cube()

    def recommended_move(self):
        self.left_move(True)
        self.right_move(True)
        self.down_move(True)
        self.top_move(True)
        if self.left >= self.right and self.down <= self.left and self.left >= self.top and self.left_s != 0:
            return 'left'
        elif self.right >= self.down and self.right >= self.top and self.right >= self.left and self.right_s != 0:
            return 'right'
        elif self.top >= self.right and self.top >= self.down and self.top >= self.left and self.top_s != 0:
            return 'top'
        elif self.down >= self.right and self.down >= self.top and self.down >= self.left and self.down_s:
            return 'down'
        else:
            if self.left_s != 0:
                return 'left'
            elif self.right_s != 0:
                return 'right'
            elif self.top_s != 0:
                return 'top'
            elif self.down_s != 0:
                return 'down'
            else:
                return 'Невозможно никуда походить'

    def max_score(self):
        con = sqlite3.connect("2048_accounts.db")
        cur = con.cursor()
        result = [i[:2] for i in cur.execute('SELECT login, password FROM players')]
        number = 0
        for player in range(len(result)):
            if result[player][0] == self.login and result[player][1] == self.password:
                number = player
                break
        max_score = [i[0] for i in cur.execute('SELECT max_score FROM max_score')][number]
        return max_score


def photoss(way, num):
    filename, file_extension = os.path.splitext(f'{way}')
    if os.path.isfile(f'{way}') and file_extension == '.jpg':
        shutil.copy(f'{way}', f'photos/{num}.jpg')
        return True
    else:
        return False




class Registration:
    def __init__(self):
        self.login = 'Гошан228'
        self.password = '332332'

    def check(self, login, password):
        con = sqlite3.connect("2048_accounts.db")
        cur = con.cursor()
        result = [i[0] for i in cur.execute('SELECT login FROM players')]
        registration_is_confirmed = True
        a = ''
        for player in result:
            if player == login:
                a = 'Пользователь под таким логином уже есть!'
                registration_is_confirmed = False
                break
        if len(login) <= 3 and registration_is_confirmed:
            registration_is_confirmed = False
            a = 'login слишком маленький, он должен состоять как минимум из 4 символов'
        elif len(password) <= 5 and registration_is_confirmed:
            registration_is_confirmed = False
            a = 'password слишком маленький, он должен состоять как минимум из 6 символов'
        return [registration_is_confirmed, a]

    def registration_player(self):
        con = sqlite3.connect("2048_accounts.db")
        cur = con.cursor()
        result = [i[0] for i in cur.execute('SELECT login FROM players')]
        if self.check(self.login, self.password)[0]:
            player = [(len(result) + 1, self.login, self.password)]
            cur.executemany('INSERT INTO players VALUES(?,?,?)', player)
            rating = [(len(result) + 1, 0)]
            cur.executemany('INSERT INTO max_score VALUES(?,?)', rating)
            con.commit()
            return 'Поздравляем с успешной регистрацией!'
        else:
            return self.check(self.login, self.password)[1]


class Entrance:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def check(self):
        entrance = False
        con = sqlite3.connect("2048_accounts.db")
        cur = con.cursor()
        result = [i[:2] for i in cur.execute('SELECT login, password FROM players')]
        a = ''
        for player in result:
            if self.login == player[0]:
                if self.password == player[1]:
                    return [True]
                else:
                    a = 'Неверный пароль!'
                    return [False, a]
                entrance = True
                break
        if entrance:
            a = 'Пользователя с таким логином не существует!'
        return [False, a]

    def entrance_player(self):
        if self.check()[0]:
            return True
        else:
            return self.check()[1]
