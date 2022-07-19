import pygame
from pygame.constants import GL_CONTEXT_MAJOR_VERSION

XN = 0.4    
XN_1 = 0.4
LOWER_LIMIT = 900
UPPER_LIMIT = 1000
R_ACCURACY = 0.01
R = 0.001

def make_window(w,h,bc):
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Bifurcation Diagram')
    screen.fill(bc)
    surface = pygame.display.get_surface()
    return screen, surface

def update():
    global XN, LOWER_LIMIT, UPPER_LIMIT, R
    
    y = []
    for i in range(UPPER_LIMIT):
        XN_1 = R*XN*(1-XN)

        if i >= LOWER_LIMIT:
            y.append(XN_1)

        XN = XN_1

    return y   
    
def render(x, y, surface):
    global R
    print(x,y)
    # pass

def main():
    global R
    # Color Initialization
    color_black = pygame.Color(0,0,0)
    color_red = pygame.Color(178,34,34)
    color_white = pygame.Color(255,255,255)

    # Window Properties
    window_width = 1700
    window_height = 930
    window_background = color_white

    # Program Properties
    exit_program = False

    # Axis Properties

    screen, surface = make_window(window_width, window_height, window_background)

    while not exit_program:
        if R < 4:
            y = update()
        render(R, y, surface)
        R = R + R_ACCURACY

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit_program = True
                elif event.key == pygame.K_ESCAPE:
                    exit_program = True
            if event.type == pygame.QUIT:
                exit_program = True

        pygame.display.flip()

main()