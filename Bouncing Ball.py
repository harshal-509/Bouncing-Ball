import sys, pygame
pygame.init()
size = width, height = 800, 400
speed = [100000000, 1]
background = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball")
ball = pygame.image.load("ball.jpg")
ballrect = ball.get_rect()
i=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(background)
    screen.blit(ball, ballrect)
    pygame.display.flip()