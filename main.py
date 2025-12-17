import cv2
import mediapipe as mp

import pygame

import threading


class Movement_game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

        self.running = True
        # self.player_pos = pygame.Vector2(
        #     self.screen.get_width()/2, self.screen.get_height()/2)

        self.player_pos = pygame.Vector2(
           0, 0)
        self.displacement = 10
        self.cap = 0
        self.positionx =0
        self.positiony = 0
        

    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if len(keys) > 0:
            if keys[pygame.K_w]:
                self.player_pos.y -= self.displacement
            if keys[pygame.K_s]:
                self.player_pos.y += self.displacement
            if keys[pygame.K_a]:
                self.player_pos.x -= self.displacement
            if keys[pygame.K_d]:
                self.player_pos.x += self.displacement

    def gesture_control(self):

        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_hands = mp.solutions.hands

        previousx = 0
        previousy = 0
        previousz = 0

        # For webcam input:
        self.cap = cv2.VideoCapture(0)
        with mp_hands.Hands(
                model_complexity=0,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as hands:
            while self.running and self.cap.isOpened():
                success, image = self.cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    continue

                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)

                # Draw the hand annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:

                    for hand_landmarks in results.multi_hand_landmarks:

                        mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())
                
                    self.positionx = results.multi_hand_landmarks[0].landmark[8].x*1280
                    self.positiony = results.multi_hand_landmarks[0].landmark[8].y*740
                    currentz = results.multi_hand_landmarks[0].landmark[8].z

        
                    print(self.positionx)
                    print(self.positiony)

                    

                # Flip the image horizontally for a selfie-view display.
                cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
                if cv2.waitKey(5) & 0xFF == 27:
                    break
        self.cap.release()

    def game_loop(self):

        threading.Thread(
            target=self.gesture_control, daemon=True
        ).start()

        clock = pygame.time.Clock()

        while self.running:
            
            self.player_pos.x = 1280 - self.positionx
            self.player_pos.y = self.positiony

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("purple")

            pygame.draw.circle(self.screen, "red", self.player_pos, 20)
                
            self.keyboard_control()
                # if self.cap.isOpened():
                #     self.gesture_control()

            pygame.display.flip()

            clock.tick(30)

        pygame.quit()


game = Movement_game()
game.game_loop()
