import pygame
import MineMath


# define a main function
def main(bs, bd, fd):
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("Bomb.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("MineSweeper")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((256, 256))

    clicked0 = pygame.image.load("ClickedZero.png")
    clicked1 = pygame.image.load("ClickedOne.png")
    clicked2 = pygame.image.load("ClickedTwo.png")
    clicked3 = pygame.image.load("ClickedThree.png")
    clicked4 = pygame.image.load("ClickedFour.png")
    unclicked = pygame.image.load("Unclicked.png")
    bomb = pygame.image.load("Bomb.png")
    font = pygame.font.SysFont("papyrus", 24)
    text = font.render("Game Over", True, (128, 0, 0))

    x = 0
    y = 0
    while x < 8:
        while y < 8:
            screen.blit(unclicked, ((y*32), (x*32)))
            y += 1
        y = 0
        x += 1
    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                coorx = int(pos[0] / 32)
                coory = int(pos[1] / 32)
                if bs[str(coorx) + str(coory)] == "B":
                    screen.blit(bomb, ((coorx*32), (coory*32)))
                    screen.blit(text, (64, 104))
                elif bs[str(coorx) + str(coory)] == "0":
                    screen.blit(clicked0, ((coorx*32), (coory*32)))
                elif bs[str(coorx) + str(coory)] == "1":
                    screen.blit(clicked1, ((coorx*32), (coory*32)))
                elif bs[str(coorx) + str(coory)] == "2":
                    screen.blit(clicked2, ((coorx*32), (coory*32)))
                elif bs[str(coorx) + str(coory)] == "3":
                    screen.blit(clicked3, ((coorx*32), (coory*32)))
                elif bs[str(coorx) + str(coory)] == "4":
                    screen.blit(clicked4, ((coorx*32), (coory*32)))
                pygame.display.flip()

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


bombspaces, bombdisplay, flagdisplay = MineMath.minedata()
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main(bombspaces, bombdisplay, flagdisplay)
