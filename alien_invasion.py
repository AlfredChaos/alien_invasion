import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
     # 初始化游戏并创建一个屏幕对象
     pygame.init()
     ai_settings = Settings()
     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
     pygame.display.set_caption("Alien Invasion")

     # 创建一个用于存储游戏统计信息的实例
     stats = GameStats(ai_settings)

     # 创建一艘飞船
     ship = Ship(screen)
     bullets = Group()

     # 创建一群外星人
     aliens = Group()
     gf.creat_fleet(ai_settings, screen, aliens, ship)

     # 开始游戏的循环
     while True:    
        gf.check_events(ship, bullets, ai_settings, screen)

        if stats.game_active:
            ship.update(ai_settings)
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
            gf.update_aliens(ai_settings, aliens, ship, screen, stats, bullets)
        
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()