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
        self.mask = pygame.mask.from_surface(self.image)


background = Background()

dio_walking = AnimatedSprite(load_image("dio_walking.png", -1), 16, 1, 100, 300, 1)
dio_walking.remove(player_group)

dio_walking_r = AnimatedSprite(load_image("dio_walking_r.png", -1), 16, 1, 100, 300, 1)
dio_walking_r.remove(player_group)

dio_standing = AnimatedSprite(load_image("dio_standing.png", -1), 16, 1, 100, 300, 1)
dio_x = dio_standing.rect.x

dio_standing_r = AnimatedSprite(load_image("dio_standing_r.png", -1), 16, 1, 100, 300, 1)
dio_x = dio_standing_r.rect.x

dio_weakattack = AnimatedSprite(load_image("dio_weakattack.png", -1), 4, 1, 100, 300, 1)
dio_weakattack.rect.y -= 2
dio_weakattack.remove(player_group)

dio_weakattack_r = AnimatedSprite(load_image("dio_weakattack_r.png", -1), 4, 1, 100, 300, 1)
dio_weakattack_r.rect.y -= 2
dio_weakattack_r.remove(player_group)

dio_mediumattack = AnimatedSprite(load_image("dio_medattack.png", -1), 9, 1, 100, 300, 1)
dio_mediumattack.remove(player_group)
dio_mediumattack.rect.y += 2

dio_mediumattack_r = AnimatedSprite(load_image("dio_medattack_r.png", -1), 9, 1, 100, 300, 1)
dio_mediumattack_r.remove(player_group)
dio_mediumattack_r.rect.y += 2

dio_heavyattack = AnimatedSprite(load_image("dio_heavyattack.png", -1), 9, 1, 100, 300, 1)
dio_heavyattack.rect.y -= 14
dio_heavyattack.remove(player_group)

dio_heavyattack_r = AnimatedSprite(load_image("dio_heavyattack_r.png", -1), 9, 1, 100, 300, 1)
dio_heavyattack_r.rect.y -= 14
dio_heavyattack_r.remove(player_group)

jotaro_walking = AnimatedSprite(load_image("joseph_walking.png", -1), 10, 1, 800, 300, 2)
jotaro_walking.rect.y -= 5
jotaro_walking.remove(player_group)

jotaro_walking_r = AnimatedSprite(load_image("joseph_walking_r.png", -1), 10, 1, 800, 300, 2)
jotaro_walking_r.rect.y -= 5
jotaro_walking_r.remove(player_group)

jotaro_standing = AnimatedSprite(load_image("joseph_standing2.png", -1), 16, 1, 700, 300, 2)
jotaro_standing.rect.y -= 4
jotaro_x = jotaro_standing.rect.x

jotaro_standing_r = AnimatedSprite(load_image("joseph_standing2_r.png", -1), 16, 1, 700, 300, 2)
jotaro_standing_r.rect.y -= 4
jotaro_x = jotaro_standing_r.rect.x

jotaro_weakattack = AnimatedSprite(load_image("joseph_weakattack.png", -1), 4, 1, 700, 300, 2)
jotaro_weakattack.rect.y -= 3
jotaro_weakattack.remove(player_group)

jotaro_weakattack_r = AnimatedSprite(load_image("joseph_weakattack_r.png", -1), 4, 1, 700, 300, 2)
jotaro_weakattack_r.rect.y -= 3
jotaro_weakattack_r.remove(player_group)

jotaro_mediumattack = AnimatedSprite(load_image("joseph_medattack.png", -1), 9, 1, 700, 300, 2)
jotaro_mediumattack.rect.y -= 8
jotaro_mediumattack.remove(player_group)

jotaro_mediumattack_r = AnimatedSprite(load_image("joseph_medattack_r.png", -1), 9, 1, 700, 300, 2)
jotaro_mediumattack_r.rect.y -= 8
jotaro_mediumattack_r.remove(player_group)

jotaro_heavyattack = AnimatedSprite(load_image("joseph_heavyattack.png", -1), 9, 1, 700, 300, 2)
jotaro_heavyattack.rect.y -= 26
jotaro_heavyattack.remove(player_group)

jotaro_heavyattack_r = AnimatedSprite(load_image("joseph_heavyattack_r.png", -1), 9, 1, 700, 300, 2)
jotaro_heavyattack_r.rect.y -= 26
jotaro_heavyattack_r.remove(player_group)

# направление персонажей 1 - направо 2 - налево
jotaro_look = 2
dio_look = 1
FPS = 16

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
    # JOTARO
    if keys[pygame.K_LEFT]:
        for el in player_group:
            if el.type == 2:
                el.remove(player_group)
        player_group.add(jotaro_walking)
        jotaro_walking.rect.x = jotaro_x
        jotaro_walking.rect.x -= 10
        jotaro_x = jotaro_walking.rect.x
        jotaro_look = 2

    elif keys[pygame.K_RIGHT]:
        for el in player_group:
            if el.type == 2:
                el.remove(player_group)
        player_group.add(jotaro_walking_r)
        jotaro_walking_r.rect.x = jotaro_x
        jotaro_walking_r.rect.x += 10
        jotaro_x = jotaro_walking_r.rect.x
        jotaro_look = 1

    elif keys[pygame.K_KP_3]:
        for el in player_group:
            if el.type == 2:
                el.remove(player_group)
        if jotaro_look == 1:
            sprite = jotaro_weakattack_r
            sprite.rect.x = jotaro_x + 40
            another = jotaro_standing_r
        else:
            sprite = jotaro_weakattack
            sprite.rect.x = jotaro_x + 30
            another = jotaro_standing
        player_group.add(sprite)
        if sprite.cur_frame == 3:
            sprite.remove(player_group)
            player_group.add(another)
            another.rect.x = jotaro_x

    elif keys[pygame.K_KP_2]:
        for el in player_group:
            if el.type == 2:
                el.remove(player_group)
        if jotaro_look == 1:
            sprite = jotaro_mediumattack_r
            sprite.rect.x = jotaro_x + 40
            another = jotaro_standing_r
        else:
            sprite = jotaro_mediumattack
            sprite.rect.x = jotaro_x + 10
            another = jotaro_standing
        player_group.add(sprite)
        if sprite.cur_frame == 8:
            sprite.remove(player_group)
            player_group.add(another)
            another.rect.x = jotaro_x

    elif keys[pygame.K_KP_1]:
        for el in player_group:
            if el.type == 2:
                el.remove(player_group)
        if jotaro_look == 1:
            sprite = jotaro_heavyattack_r
            sprite.rect.x = jotaro_x + 33
            another = jotaro_standing_r
        else:
            sprite = jotaro_heavyattack
            sprite.rect.x = jotaro_x + 33
            another = jotaro_standing
        player_group.add(sprite)
        if sprite.cur_frame == 8:
            sprite.remove(player_group)
            player_group.add(another)
            another.rect.x = jotaro_x

    else:
        for el in player_group:
            if el.type == 2:
                el.remove(player_group)
        if jotaro_look == 1:
            player_group.add(jotaro_standing_r)
            jotaro_standing_r.rect.x = jotaro_x
        else:
            player_group.add(jotaro_standing)
            jotaro_standing.rect.x = jotaro_x
        jotaro_walking.cur_frame = 0
        jotaro_walking_r.cur_frame = 0
        jotaro_weakattack.cur_frame = 0
        jotaro_weakattack_r.cur_frame = 0
        jotaro_mediumattack.cur_frame = 0
        jotaro_mediumattack_r.cur_frame = 0
        jotaro_heavyattack.cur_frame = 0
        jotaro_heavyattack_r.cur_frame = 0
    # DIO
    if keys[pygame.K_a]:
        for el in player_group:
            if el.type == 1:
                el.remove(player_group)
        player_group.add(dio_walking_r)
        dio_walking_r.rect.x = dio_x
        dio_walking_r.rect.x -= 10
        dio_x = dio_walking_r.rect.x
        dio_look = 2

    elif keys[pygame.K_d]:
        for el in player_group:
            if el.type == 1:
                el.remove(player_group)
        player_group.add(dio_walking)
        dio_walking.rect.x = dio_x
        dio_walking.rect.x += 10
        dio_x = dio_walking.rect.x
        dio_look = 1

    elif keys[pygame.K_k]:
        for el in player_group:
            if el.type == 1:
                el.remove(player_group)
        if dio_look == 1:
            sprite = dio_weakattack
            sprite.rect.x = dio_x
            another = dio_standing
        else:
            sprite = dio_weakattack_r
            sprite.rect.x = dio_x - 55
            another = dio_standing_r
        player_group.add(sprite)
        if sprite.cur_frame == 3:
            sprite.remove(player_group)
            player_group.add(another)
            another.rect.x = dio_x

    elif keys[pygame.K_j]:
        for el in player_group:
            if el.type == 1:
                el.remove(player_group)
        if dio_look == 1:
            sprite = dio_mediumattack
            sprite.rect.x = dio_x - 70
            another = dio_standing
        else:
            sprite = dio_mediumattack_r
            sprite.rect.x = dio_x - 60
            another = dio_standing_r
        player_group.add(sprite)
        if sprite.cur_frame == 8:
            sprite.remove(player_group)
            player_group.add(another)
            another.rect.x = dio_x

    elif keys[pygame.K_h]:
        for el in player_group:
            if el.type == 1:
                el.remove(player_group)
        if dio_look == 1:
            sprite = dio_heavyattack
            sprite.rect.x = dio_x + 10
            another = dio_standing
        else:
            sprite = dio_heavyattack_r
            sprite.rect.x = dio_x - 80
            another = dio_standing_r
        player_group.add(sprite)
        if sprite.cur_frame == 8:
            sprite.remove(player_group)
            player_group.add(another)
            another.rect.x = dio_x

    else:
        for el in player_group:
            if el.type == 1:
                el.remove(player_group)
        if dio_look == 1:
            player_group.add(dio_standing)
            dio_standing.rect.x = dio_x
        else:
            player_group.add(dio_standing_r)
            dio_standing_r.rect.x = dio_x
        dio_walking.cur_frame = 0
        dio_walking_r.cur_frame = 0
        dio_weakattack.cur_frame = 0
        dio_weakattack_r.cur_frame = 0
        dio_mediumattack.cur_frame = 0
        dio_mediumattack_r.cur_frame = 0
        dio_heavyattack.cur_frame = 0
        dio_heavyattack_r.cur_frame = 0
    clock.tick(FPS)
pygame.quit()
