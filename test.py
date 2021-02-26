# DIO
    if keys[pygame.K_a] and dio_hit is False:
        for el in dio_group:
            el.remove(dio_group)
        dio_group.add(dio_walking_r)
        dio_cur_sprite = dio_walking_r
        dio_walking_r.rect.x = dio_x
        dio_walking_r.rect.x -= 10
        dio_x = dio_walking_r.rect.x
        dio_look = 2

    elif keys[pygame.K_d] and dio_hit is False:
        for el in dio_group:
            el.remove(dio_group)
        dio_group.add(dio_walking)
        dio_cur_sprite = dio_walking
        dio_walking.rect.x = dio_x
        dio_walking.rect.x += 10
        dio_x = dio_walking.rect.x
        dio_look = 1

    elif keys[pygame.K_k]:
        for el in dio_group:
            el.remove(dio_group)
        if dio_look == 1:
            sprite = dio_weakattack
            sprite.rect.x = dio_x
            another = dio_standing
        else:
            sprite = dio_weakattack_r
            sprite.rect.x = dio_x - 90
            another = dio_standing_r
        dio_group.add(sprite)
        dio_cur_sprite = sprite
        if sprite.cur_frame == 3:
            sprite.remove(dio_group)
            dio_group.add(another)
            dio_cur_sprite = another
            another.rect.x = dio_x
        elif pygame.sprite.collide_mask(sprite, jotaro_cur_sprite) and sprite.cur_frame == 1:
            jotaro_hit = True
            for el in jotaro_group:
                el.remove(jotaro_group)
            if dio_look == 1:
                jotaro_cur_sprite = jotaro_weakhert
                jotaro_group.add(jotaro_weakhert)
                jotaro_weakhert.rect.x = jotaro_x + 80
                jotaro_look = 2
            else:
                jotaro_cur_sprite = jotaro_weakhert_r
                jotaro_group.add(jotaro_weakhert_r)
                jotaro_weakhert_r.rect.x = jotaro_x + 20
                jotaro_look = 1
            jotaro_hp -= 8
            joseph_hit_m.play()
        if jotaro_weakhert.cur_frame == 2 or jotaro_weakhert_r.cur_frame == 2:
            jotaro_hit = False
            jotaro_cur_sprite = jotaro_standing
            jotaro_group.add(jotaro_standing)
            jotaro_standing.rect.x = jotaro_x

    elif jotaro_weakhert.cur_frame == 2 or jotaro_weakhert_r.cur_frame == 2:
        jotaro_hit = False
        jotaro_cur_sprite = jotaro_standing
        jotaro_group.add(jotaro_standing)
        jotaro_standing.rect.x = jotaro_x

    elif keys[pygame.K_j]:
        for el in dio_group:
            el.remove(dio_group)
        if dio_look == 1:
            sprite = dio_mediumattack
            sprite.rect.x = dio_x - 140
            another = dio_standing
        else:
            sprite = dio_mediumattack_r
            sprite.rect.x = dio_x - 100
            another = dio_standing_r
        dio_group.add(sprite)
        dio_cur_sprite = sprite
        if sprite.cur_frame == 8:
            sprite.remove(dio_group)
            dio_group.add(another)
            dio_cur_sprite = another
            another.rect.x = dio_x
        elif pygame.sprite.collide_mask(sprite, jotaro_cur_sprite) and (sprite.cur_frame == 4):
            jotaro_hit = True
            for el in jotaro_group:
                el.remove(jotaro_group)
            if dio_look == 1:
                jotaro_cur_sprite = jotaro_mediumhert
                jotaro_group.add(jotaro_mediumhert)
                jotaro_mediumhert.rect.x = jotaro_x + 90
                jotaro_look = 2
            else:
                jotaro_cur_sprite = jotaro_mediumhert_r
                jotaro_group.add(jotaro_mediumhert_r)
                jotaro_mediumhert_r.rect.x = jotaro_x + 20
                jotaro_look = 1
            jotaro_hp -= 12
            joseph_hit_m.play()
        if jotaro_mediumhert.cur_frame == 3 or jotaro_mediumhert_r.cur_frame == 3:
            jotaro_hit = False
            jotaro_cur_sprite = jotaro_standing
            jotaro_group.add(jotaro_standing)
            jotaro_standing.rect.x = jotaro_x

    elif jotaro_mediumhert.cur_frame == 3 or jotaro_mediumhert_r.cur_frame == 3:
        jotaro_hit = False
        jotaro_cur_sprite = jotaro_standing
        jotaro_group.add(jotaro_standing)
        jotaro_standing.rect.x = jotaro_x

    elif keys[pygame.K_h]:
        for el in dio_group:
            el.remove(dio_group)
        if dio_look == 1:
            sprite = dio_heavyattack
            sprite.rect.x = dio_x
            another = dio_standing
        else:
            sprite = dio_heavyattack_r
            sprite.rect.x = dio_x - 120
            another = dio_standing_r
        dio_group.add(sprite)
        dio_cur_sprite = sprite
        if sprite.cur_frame == 8:
            sprite.remove(dio_group)
            dio_group.add(another)
            dio_cur_sprite = another
            another.rect.x = dio_x
        elif pygame.sprite.collide_mask(sprite, jotaro_cur_sprite) and (sprite.cur_frame == 5):
            jotaro_hit = True
            for el in jotaro_group:
                el.remove(jotaro_group)
            if dio_look == 1:
                jotaro_cur_sprite = jotaro_heavyhert
                jotaro_group.add(jotaro_heavyhert)
                jotaro_heavyhert.rect.x = jotaro_x + 90
                jotaro_look = 2
            else:
                jotaro_cur_sprite = jotaro_heavyhert
                jotaro_group.add(jotaro_heavyhert)
                jotaro_heavyhert.rect.x = jotaro_x + 20
                jotaro_look = 1
            jotaro_hp -= 18
            joseph_hit_m.play()
        if jotaro_heavyhert.cur_frame == 15 or jotaro_heavyhert.cur_frame == 15:
            jotaro_hit = False
            jotaro_cur_sprite = jotaro_standing
            jotaro_group.add(jotaro_standing)
            jotaro_standing.rect.x = jotaro_x

    elif jotaro_heavyhert.cur_frame == 15 or jotaro_heavyhert.cur_frame == 15:
        jotaro_hit = False
        jotaro_cur_sprite = jotaro_standing
        jotaro_group.add(jotaro_standing)
        jotaro_standing.rect.x = jotaro_x

    elif dio_hit is False:
        for el in dio_group:
            el.remove(dio_group)
        if dio_look == 1:
            dio_group.add(dio_standing)
            dio_cur_sprite = dio_standing
            dio_standing.rect.x = dio_x
        else:
            dio_group.add(dio_standing_r)
            dio_cur_sprite = dio_standing_r
            dio_standing_r.rect.x = dio_x
        dio_walking.cur_frame = 0
        dio_walking_r.cur_frame = 0
        dio_weakattack.cur_frame = 0
        dio_weakattack_r.cur_frame = 0
        dio_mediumattack.cur_frame = 0
        dio_mediumattack_r.cur_frame = 0
        dio_heavyattack.cur_frame = 0
        dio_heavyattack_r.cur_frame = 0
        dio_weakhert.cur_frame = 0
        dio_weakhert_r.cur_frame = 0
        dio_mediumhert.cur_frame = 0
        dio_mediumhert_r.cur_frame = 0
        dio_heavyhert.cur_frame = 0
        dio_heavyhert_r.cur_frame = 0