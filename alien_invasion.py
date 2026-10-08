import sys
import pygame
from setting import Setting
from ship import ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """manage the resources and behaviors"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.setting = Setting()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invation")

        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()

        

    def run_game(self):
        """Begin the main loop of the game"""
        while True:
            self._check_event()
            self.update_screen()
            self._update_bullet()
            self.update_alien()
            self.clock.tick(60)
            self.ship.update()
            
            

            
    def _check_event(self):
        """检查一切的鼠标和键盘活动"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                self.key_down_event(event)
            elif event.type == pygame.KEYUP:
                self.key_up_event(event)
            

    def key_down_event(self,event):
        """响应按下的操作"""
        if event.key == pygame.K_RIGHT:
            self.ship.keep_move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.keep_move_left=True
        elif event.key == pygame.K_SPACE:
            print("1. SPACE detected")    
            self._fire_bullet()
        elif event.key ==pygame.K_q:
            pygame.quit()
            sys.exit()

    def key_up_event(self,event):
        """响应放开的操作"""
        if event.key == pygame.K_RIGHT:
            self.ship.keep_move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.keep_move_left=False


    def update_screen(self):
        """让最近绘制的屏幕可见"""
        self.screen.fill(self.setting.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)


        pygame.display.flip()

    def _fire_bullet(self):
        """fire!!!"""
        if len(self.bullets) < self.setting.bullet_max:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_bullet(self):
        """跟新子弹的位置并管理子弹"""
        self.bullets.update()
        #删除发射的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<0:
                self.bullets.remove(bullet)
                print(len(self.bullets))

    def create_fleet(self):
        """创建外星人舰队"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x,current_y = alien_width,alien_height
        while current_y < (self.setting.screen_height - 3*alien_height):
            while current_x < (self.setting.screen_width-2*alien_width):
                self.create_alien(current_x,current_y)
                current_x+=2*alien_width
            current_x = alien_width
            current_y+=2*alien_height

    def create_alien(self,x_position,y_postition):
        """创建外星人"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_postition
        self.aliens.add(new_alien)

    def update_alien(self):
        self.aliens.update()



if __name__ == '__main__':
    """create the instance of the game and exucute the game"""
    ai = AlienInvasion()
    ai.run_game()
    