from constants import *
import sys, pygame, main_block

clock = pygame.time.Clock()
screen_size = pygame.FULLSCREEN
surface = pygame.display.set_mode((0, 0), screen_size)
pygame.init()


all_group = 0

state = "" #main, pause, running





def main():
    running = True
    global state

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_p:

                    # value_if_true if condition else value_if_false

                    state = "paused" if state == "running" else "running"
                    # if state == "running":
                    #     state = "paused"
                    # else:
                    #     state = "running"

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    state = "running"

        draw()


    pygame.quit()
    sys.exit()



def draw():

    if state == "main":
        surface.fill((100, 100, 255))#background
        pygame.display.flip()


    if state == "running":
        surface.fill((100, 100, 100))#background
        all_group.draw(surface)
        pygame.display.flip()
        update()


    if state == "paused":
        pass







def update():
    all_group.update()

if __name__ == "__main__":


    all_group = pygame.sprite.Group()
    all_group.add(main_block.Main_block(50, 50))
    state = "main"
    main()
