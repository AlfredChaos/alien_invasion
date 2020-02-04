import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按键
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例, 并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # 创建一群外星人
    aliens = Group()
    gf.creat_fleet(ai_settings, screen, aliens, ship)

    # 开始游戏的循环
    while True:    
        gf.check_events(ship, bullets, ai_settings, screen, stats, play_button, aliens, sb)

        if stats.game_active:
            ship.update(ai_settings)
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, sb, stats)
            gf.update_aliens(ai_settings, aliens, ship, screen, stats, bullets, sb)
        
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, sb)


run_game()