import cv2
import mediapipe as mp

import pygame

class Movement_game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.running = True
        self.player_pos = pygame.Vector2(self.screen.get_width()/2,self.screen.get_height()/2)
        self.displacement = 10

    # def player(self):
    #     self.player_pos = pygame.Vector2(self.screen.get_width()/2,self.screen.get_height()/2)

    def keyboard_movement(self):
        keys = pygame.key.get_pressed()
        if len(keys)>0:
            if keys[pygame.K_w]:
                self.player_pos.y -= self.displacement
            if keys[pygame.K_s]:
                self.player_pos.y += self.displacement 
            if keys[pygame.K_a]:
                self.player_pos.x -= self.displacement 
            if keys[pygame.K_d]:
                self.player_pos.x += self.displacement


    def game_loop(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.screen.fill("purple")
                pygame.draw.circle(self.screen,"red",self.player_pos, 20)

                self.keyboard_movement()

                pygame.display.flip()


        pygame.quit()




game = Movement_game()
game.game_loop()