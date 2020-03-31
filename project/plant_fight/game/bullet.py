import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, plane, speed=30):
        super().__init__()
        # 绘制屏幕对象
        self.screen = screen
        # 发射子弹的飞机
        self.plane = plane
        self.speed = speed
        self.image = pygame.image.load(constants.BULLET_IMG)
        self.sound = pygame.mixer.Sound(constants.BULLET_SOUND)
        # 设置音量
        self.sound.set_volume(0.3)
        # 播放射击的声音
        self.sound.play()
        # 设置子弹的位置
        # 首先获取到初始位置
        self.rect = self.image.get_rect()
        # 设置中间位置
        self.rect.centerx = self.plane.rect.centerx
        # 设置定点位置
        self.rect.top = self.plane.rect.top

    def update(self, enemies_group, score):
        # 更新子弹状态
        self.rect.top -= self.speed
        if self.rect.top <= 0:
            self.remove(self.plane.bullets)
        self.screen.blit(self.image, self.rect)
        # 检测子弹是否碰撞到地方飞机
        sprites = pygame.sprite.spritecollide(self, enemies_group, False)
        for sprite in sprites:
            # 将子弹从精灵组中去除
            self.kill()
            # 将被子弹击落的飞机 添加爆炸动画 然后从精灵组中移除
            sprite.borken_down()
            sprite.kill()
            score.score += constants.SMALL_ENEMY_PLANE_DESTORY_SCORE

    


