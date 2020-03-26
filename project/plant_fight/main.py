import pygame, sys
from constants import BG_IMG, BG_MUSIC, TITLE_IMG, START_BTN_IMG


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
    # 加载标题图片
    title_img = pygame.image.load(TITLE_IMG)
    # 加载开始按钮图片
    start_btn_img = pygame.image.load(START_BTN_IMG)

    # 加载背景音乐
    pygame.mixer.music.load(BG_MUSIC)
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


    while True:
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == READY:
                    status = PLAYING
                    print(' >>> 进入游戏进行状态')


        # 准备状态
        if status == READY:
            screen.blit(bg, bg.get_rect())
            screen.blit(title_img, title_img_rect)
            screen.blit(start_btn_img, start_btn_img_rect)
        elif status == PLAYING:
            screen.blit(bg, bg.get_rect())


        # 更新游戏状态
        
        # 绘制
        pygame.display.flip() 




if __name__ == '__main__':
    main()