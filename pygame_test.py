import pygame


def action_loop(up_displacement, down_displacement, right_displacement, left_displacement):
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    dot_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill("purple")
            pygame.draw.circle(screen,"red",dot_pos, 40)

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_w]:
            #     dot_pos.y -= 15
            # if keys[pygame.K_s]:
            #     dot_pos.y += 15 
            # if keys[pygame.K_a]:
            #     dot_pos.x -= 15 
            # if keys[pygame.K_d]:
            #     dot_pos.x += 15 

            
            dot_pos.y -= up_displacement
            
            dot_pos.y += down_displacement
    
            dot_pos.x -= left_displacement
        
            dot_pos.x += 15 

            pygame.display.flip()

            dt = clock.tick(60)/1000

    pygame.quit()