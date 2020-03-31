import pygame
import constants
import re, random
from game.bullet import Bullet

frame_regex = re.compile(r'^\d*[0-4]$')

class Plane(pygame.sprite.Sprite):
    # 飞机的绘制图片列表
    plane_imgs = []
    # 飞机毁灭时用来绘制的图片
    destory_imgs = []
    # 飞机毁灭时的音乐
    destory_sound = None
    # 飞机当前的状态
    active = True
    # 飞机的子弹组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=2):
        super().__init__()
        # 主屏幕
        self.screen = screen
        self.screen_wd, self.screen_ht = self.screen.get_size()
        self._imgs = []
        self._destory_imgs = []
        self._destory_sound = None
        # 加载静态资源
        self.source_load()
        #  设置飞机飞行速度
        self.speed = speed
        # 设置飞机位置
        self.rect = self._imgs[0].get_rect()
        self.wd, self.ht = self._imgs[0].get_size()
        self.rect.left = int((self.screen_wd - self.wd) / 2)
        self.rect.top = int(self.screen_ht - self.ht  - 10)


    def source_load(self):
        for img in self.plane_imgs:
            self._imgs.append(pygame.image.load(img))
        for img in self.destory_imgs:
            self._destory_imgs.append(pygame.image.load(img))
        if self.destory_sound:
            self._destory_sound = pygame.mixer.Sound(self.destory_sound)


    def blit_self(self):
        self.screen.blit(self._imgs[0], self.rect)

    def move_up(self):
        self.rect.top -= self.speed

    def move_down(self):
        self.rect.top += self.speed

    def move_left(self):
        self.rect.left -= self.speed

    def move_right(self):
        self.rect.left += self.speed

    # 飞机坠毁
    def borken_down(self):
        if self._destory_sound:
            self._destory_sound.play()
        for img in self._destory_imgs:
            self.screen.blit(img, self.rect)
        self.active = False

    # 飞机的射击功能
    def shoot(self):
        bul = Bullet(self.screen, self)
        self.bullets.add(bul)
 

class OurPlane(Plane):
    plane_imgs = [constants.PLANE_IMG_1, constants.PLANE_IMG_2]
    destory_imgs = constants.PLANE_DESTORY_IMGS
    destory_sound = constants.PLANE_DESTORY_SOUND

    def update(self, frame, enemies_group, key_down):
        # 保证持续移动
        self.move(key_down)
        # 切换飞机的动画效果
        if frame_regex.match(str(frame)):
            self.screen.blit(self._imgs[0], self.rect)
        else:
            self.screen.blit(self._imgs[1], self.rect)
        # 检测飞机是否撞击到了敌方飞机
        if pygame.sprite.spritecollide(self, enemies_group, False):
            self.borken_down()
            self.active = False
            # 返回 False 代表游戏已经结束了
            return True
        return False


    def move(self, key):
        if key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        super().move_up()
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_left(self):
        super().move_left()
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_down(self):
        super().move_down()
        if self.rect.top + self.ht >= self.screen_ht:
            self.rect.top = self.screen_ht - self.ht
    
    def move_right(self):
        super().move_right()
        if self.rect.left + self.wd >= self.screen_wd:
            self.rect.left = self.screen_wd - self.wd


class SmallEnemyPlane(Plane):
    # 飞机的绘制图片列表
    plane_imgs = [constants.SMALL_ENEMY_PLANE_IMG]
    # 飞机毁灭时用来绘制的图片
    destory_imgs = constants.SMALL_ENEMY_PLANE_DESTORY_IMGS
    # 飞机毁灭时的音乐
    destory_sound = constants.SMALL_ENEMY_PLANE_DESTORY_SOUND
    # 飞机当前的状态
    active = True


    def __init__(self, screen, speed=3):
        super().__init__(screen, speed)
        self.rect.left = random.randint(0, self.screen_wd - self.wd)
        self.rect.top = random.randint(-5 * self.ht, -self.ht)

    def update(self):
        self.move_down()
        self.blit_self()
        if self.rect.top > self.screen_ht:
            self.active = False
            self.kill()