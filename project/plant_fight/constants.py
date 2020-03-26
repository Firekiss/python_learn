import os

# 获取当前文件的目录的绝对地址
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 资源文件夹地址
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
# 背景图片地址
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
# 背景音乐地址
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/jntm.mp3')
# 游戏标题
TITLE_IMG = os.path.join(ASSETS_DIR, 'images/game_title.png')
# 游戏开始按钮
START_BTN_IMG = os.path.join(ASSETS_DIR, 'images/game_start.png')