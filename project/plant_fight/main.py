import pygame, sys
from constants import BG_IMG, BG_MUSIC, TITLE_IMG, START_BTN_IMG, BG_IMG_OVER, SCORE_COLOR
from game.plane import OurPlane, SmallEnemyPlane
from store.result import Score

def main():
    """
    游戏入口，main方法
    """
    pygame.init()

    # 游戏状态
    # 0 代表等待中
    # 1 代表游戏中
    # 2 代表游戏结束
    READY = 0
    PLAYING = 1
    END = 2
    # 窗口窗口大小配置
    width, height = 480, 852
    

    # 创建屏幕对象
    screen = pygame.display.set_mode((width, height))
    # 设置窗口名称
    pygame.display.set_caption('打飞机')

    # 加载背景图片
    bg = pygame.image.load(BG_IMG)
    bg_over = pygame.image.load(BG_IMG_OVER)
    # 加载标题图片
    title_img = pygame.image.load(TITLE_IMG)
    # 加载开始按钮图片
    start_btn_img = pygame.image.load(START_BTN_IMG)

    # 加载背景音乐
    pygame.mixer.music.load(BG_MUSIC)
    # 设置背景音乐的音量
    pygame.mixer.music.set_volume(0.2)
    # 无限循环播放背景音乐
    pygame.mixer.music.play(-1)

    # 获取游戏标题图片位置
    title_img_rect = title_img.get_rect()
    # 获取游戏标题图片尺寸
    title_img_width, title_img_height = title_img.get_size()
    # 设置初始位置
    title_img_rect.topleft = (
        (width - title_img_width) / 2,
        (height - title_img_height) / 4
    )

    # 获取游戏开始按钮图片位置
    start_btn_img_rect = start_btn_img.get_rect()
    start_btn_img_width, start_btn_img_height = start_btn_img.get_size()
    # 设置初始位置
    start_btn_img_rect.topleft = (
        (width - start_btn_img_width) / 2,
        (height - start_btn_img_height) / 2
    )
    
    # 初始化状态
    status = READY
    # 帧数计数器
    frame = 0
    clock = pygame.time.Clock()
    # 创建积分实例
    score = Score()
    # 我方飞机实例
    our_plane = OurPlane(screen)
    # 创建敌机精灵组
    enemies_group = pygame.sprite.Group()
    # 生成小型敌方飞机
    for i in range(6):
        small_enemy_plane = SmallEnemyPlane(screen)
        enemies_group.add(small_enemy_plane)

    # 创建积分文字
    score_font = pygame.font.Font('./demo/my_font.ttf', 32)
    # 获取显示屏的宽高
    s_wd, s_ht = screen.get_size()
    # 记录键盘按下的按钮
    key_down = None


    while True:
        clock.tick(60)
        frame += 1
        if frame == 60:
            frame = 0

        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == READY:
                    status = PLAYING
            elif event.type == pygame.KEYDOWN:
                if status == PLAYING:
                    key_down = event.key
                    if event.key == pygame.K_DOWN:
                        our_plane.move_down()
                    elif event.key == pygame.K_UP:
                        our_plane.move_up()
                    elif event.key == pygame.K_LEFT:
                        our_plane.move_left()
                    elif event.key == pygame.K_RIGHT:
                        our_plane.move_right()
                    elif event.key == pygame.K_SPACE:
                        our_plane.shoot()

        # 准备状态
        if status == READY:
            screen.blit(bg, bg.get_rect())
            screen.blit(title_img, title_img_rect)
            screen.blit(start_btn_img, start_btn_img_rect)
        elif status == PLAYING:
            screen.blit(bg, bg.get_rect())
            our_plane.blit_self()
            # 更新飞机
            if our_plane.update(frame, enemies_group, key_down):
                status = END
            # 更新绘制子弹
            our_plane.bullets.update(enemies_group, score)
            enemies_group.update()
            # 绘制当前的积分
            score_text = score_font.render('积分: {}'.format(score.score), False, SCORE_COLOR)
            screen.blit(score_text, (10, 10))
        elif status == END:
            screen.blit(bg_over, bg_over.get_rect())
            # 显示此次积分数值
            score_text = score_font.render('{}'.format(score.score), False, SCORE_COLOR)
            score_text_wd, score_text_ht = score_text.get_size()
            screen.blit(score_text, (
               (s_wd - score_text_wd) / 2,
               (s_ht - score_text_ht) / 2
            ))
        
        # 绘制
        pygame.display.flip() 




if __name__ == '__main__':
    main()