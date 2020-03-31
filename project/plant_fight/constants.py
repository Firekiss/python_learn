import os, pygame

# 获取当前文件的目录的绝对地址
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 资源文件夹地址
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
# 背景图片地址
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
# 游戏结束的背景图片
BG_IMG_OVER = os.path.join(ASSETS_DIR, 'images/game_over.png')
# 背景音乐地址
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/jntm.mp3')
# 游戏标题
TITLE_IMG = os.path.join(ASSETS_DIR, 'images/game_title.png')
# 游戏开始按钮
START_BTN_IMG = os.path.join(ASSETS_DIR, 'images/game_start.png')

# 我方飞机图片1
PLANE_IMG_1 = os.path.join(ASSETS_DIR, 'images/hero1.png')
# 我方飞机图片2
PLANE_IMG_2 = os.path.join(ASSETS_DIR, 'images/hero2.png')
# 我方飞机坠毁图片组
PLANE_DESTORY_IMGS = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png'),
]
# 我方飞机坠毁音乐
PLANE_DESTORY_SOUND = os.path.join(ASSETS_DIR, 'sounds/game_over.wav')

# 子弹发射的音乐
BULLET_SOUND = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')
# 子弹发射的图片
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')

# 敌方小型飞机图片
SMALL_ENEMY_PLANE_IMG = os.path.join(ASSETS_DIR, 'images/enemy1.png')
# 敌方小型飞机坠毁图片组
SMALL_ENEMY_PLANE_DESTORY_IMGS = [
    os.path.join(ASSETS_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down4.png'),
]
# 敌方小型飞机坠毁音乐
SMALL_ENEMY_PLANE_DESTORY_SOUND = os.path.join(ASSETS_DIR, 'sounds/enemy1_down.wav')

# 每击倒一架敌方飞机所获得的积分
SMALL_ENEMY_PLANE_DESTORY_SCORE = 10
# 积分字体颜色
SCORE_COLOR = pygame.Color(0, 0, 0)
