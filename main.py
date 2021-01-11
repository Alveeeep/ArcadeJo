import pygame
import os
import random
import sys

pygame.init()
size = width, height = 1000, 570
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
pygame.display.set_caption("jojo")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


FPS = 16


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Перемещение героя", "",
                  "Герой двигается",
                  "Карта на месте"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, type):
        super().__init__(player_group, all_sprites)
        self.frames = []
        self.type = type
        self.sheet = sheet
        self.columns = columns
        self.rows = rows
        self.cut_sheet(self.sheet, self.columns, self.rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Background(pygame.sprite.Sprite):
    image = load_image("jojofon.jpg")

    def __init__(self):
        super().__init__(walls_group, all_sprites)
        self.image = Background.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
    # self.rect.bottom = height


background = Background()

dio_walking = AnimatedSprite(load_image("dio_walking.png", -1), 16, 1, 100, 300, 1)
dio_walking.remove(player_group)

dio_walking_r = AnimatedSprite(load_image("dio_walking_r.png", -1), 16, 1, 100, 300, 1)
dio_walking_r.remove(player_group)

jotaro_walking = AnimatedSprite(load_image("jotaro_walking2.png", -1), 16, 1, 800, 300, 2)
jotaro_walking.remove(player_group)

jotaro_walking_r = AnimatedSprite(load_image("jotaro_walking2_r.png", -1), 16, 1, 800, 300, 2)
jotaro_walking_r.remove(player_group)

dio_standing = AnimatedSprite(load_image("dio_standing.png", -1), 16, 1, 100, 300, 1)
dio_x = dio_standing.rect.x

jotaro_standing = AnimatedSprite(load_image("jotaro_standing.png", -1), 16, 1, 800, 300, 2)
jotaro_x = jotaro_standing.rect.x

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('white'))
    walls_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_group.add(jotaro_walking)
        jotaro_walking_r.remove(player_group)
        jotaro_standing.remove(player_group)
        jotaro_walking.rect.x = jotaro_x
        jotaro_walking.rect.x -= 10
        jotaro_x = jotaro_walking.rect.x
    elif keys[pygame.K_RIGHT]:
        player_group.add(jotaro_walking_r)
        jotaro_walking.remove(player_group)
        jotaro_standing.remove(player_group)
        jotaro_walking_r.rect.x = jotaro_x
        jotaro_walking_r.rect.x += 10
        jotaro_x = jotaro_walking_r.rect.x
    else:
        jotaro_walking.remove(player_group)
        jotaro_walking_r.remove(player_group)
        player_group.add(jotaro_standing)
        jotaro_walking.cur_frame = 0
        jotaro_walking_r.cur_frame = 0
        jotaro_standing.rect.x = jotaro_x
    if keys[pygame.K_a]:
        player_group.add(dio_walking_r)
        dio_walking.remove(player_group)
        dio_standing.remove(player_group)
        dio_walking_r.rect.x = dio_x
        dio_walking_r.rect.x -= 10
        dio_x = dio_walking_r.rect.x
    elif keys[pygame.K_d]:
        player_group.add(dio_walking)
        dio_walking_r.remove(player_group)
        dio_standing.remove(player_group)
        dio_walking.rect.x = dio_x
        dio_walking.rect.x += 10
        dio_x = dio_walking.rect.x
    else:
        dio_walking.remove(player_group)
        dio_walking_r.remove(player_group)
        player_group.add(dio_standing)
        dio_walking.cur_frame = 0
        dio_walking_r.cur_frame = 0
        dio_standing.rect.x = dio_x
    clock.tick(FPS)
pygame.quit()
