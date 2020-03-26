import pygame, sys

# 初始化 pygame
pygame.init()
# 设置显示创口的宽高元组
size = width, height = 400, 400
# 设置窗口
screen = pygame.display.set_mode(size)
# 设置颜色
RED = pygame.Color(255, 0, 0)

# 不断循环
while True:
    # 获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 修改状态
    

    # 画线
    pygame.draw.line(screen, RED, (0,0), (100, 100), 5)
    
    # 重新更新画面
    pygame.display.flip()

