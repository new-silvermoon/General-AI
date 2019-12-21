import OpenGL
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import pygame

class Simulation():
    screen = None
    pacman_pos_x = None
    pacman_pos_y = None
    west_pellet_pos_x = None
    west_pellet_pos_y = None
    east_pellet_pos_x = None
    east_pellet_pos_y = None
    spoon_pos_x = None
    spoon_pos_y = None
    actions_list = []
    has_spoon = False
    has_pellet = False


    def __init__(self,actions_list):
        self.pacman_pos_x = 250
        self.pacman_pos_y = 450
        self.west_pellet_pos_x = 50
        self.west_pellet_pos_y = 250
        self.east_pellet_pos_x = 450
        self.east_pellet_pos_y = 250
        self.spoon_pos_x = 250
        self.spoon_pos_y = 250
        self.actions_list = actions_list

        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))



    def draw_init_objects(self):
        done = False

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Press SPACE to begin', True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (250,250)

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.screen.fill((0,0,0))
                        self.start_animation()

            """Initial position of pacman"""
            pygame.draw.circle(self.screen,(255,255,0),(self.pacman_pos_x,self.pacman_pos_y),20)

            """Initial position of pellets"""
            #pygame.draw.circle(self.screen, (255, 255, 255), (self.west_pellet_pos_x, self.west_pellet_pos_y), 5)
            pygame.draw.circle(self.screen, (255, 255, 255), (self.east_pellet_pos_x, self.east_pellet_pos_y), 5)

            """Initial position of spoon"""
            pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(250, 250, 20, 20))

            self.screen.blit(text, textRect)

            pygame.display.flip()


    def start_animation(self):

        done = False
        dy = 1
        dx = 1

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Objective completed', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (250, 250)

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.screen.fill((0, 0, 0))

            """Moving towards spoon"""
            if "move to middle" in self.actions_list and self.has_spoon == False:
                self.pacman_pos_y -= dy
            elif "move to pellet" in self.actions_list and self.has_pellet == False:
                self.pacman_pos_x += dx

            pygame.draw.circle(self.screen, (255, 255, 0), (self.pacman_pos_x , self.pacman_pos_y), 20)

            if self.pacman_pos_x in range(self.east_pellet_pos_x-1,self.east_pellet_pos_x+2) and self.pacman_pos_y in range(self.east_pellet_pos_y-1,self.east_pellet_pos_y+2):
                self.has_pellet = True
                self.screen.blit(text, textRect)

            if self.pacman_pos_x in range(self.spoon_pos_x-1,self.spoon_pos_x+2) and self.pacman_pos_y in range(self.spoon_pos_y-1,self.spoon_pos_y+2):
                self.has_spoon = True


            if self.has_pellet == False:
                pygame.draw.circle(self.screen, (255, 255, 255), (self.east_pellet_pos_x, self.east_pellet_pos_y), 5)

            if self.has_spoon == False:
                pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(self.spoon_pos_x, self.spoon_pos_y, 20, 20))

            pygame.display.flip()







