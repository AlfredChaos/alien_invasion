import pygame
import os
import sys

from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(os.path.abspath(os.path.dirname(os.path.abspath(sys.argv[0])) + os.path.sep) + "\\images\\ship.bmp")
        #print(os.path.abspath(os.path.dirname(os.path.abspath(sys.argv[0])) + os.path.sep + ".") + "\\images\\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = self.rect.centerx

        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self, ai_settings):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx