import random
import pygame
import OpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pyrr


def init():
    pygame.init()
    display = (700, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(.30, 0.20, 0.20, 1.0)
    # glViewport(0, 0, 500, 500)
    gluPerspective(45, (display[0] / display[1]), 0.1, 150.0)
    # glTranslatef(random.randrange(-5, 5), 0, -20)





lx = 0
ly = 0
lz = -1
roll = 0
x = -5
z = 18
def draw():
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

    gluLookAt(x, 2.5, z, x + lx, 2.5 + ly, z + lz, roll + 0, 2.5, 0)

    #Floor for bedroom
    glColor3f(0.3, 0.4, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-12, 0, -12)
    glVertex3f(-12, 0, 12)
    glVertex3f(12, 0, 12)
    glVertex3f(12, 0, -12)
    glEnd()

    #Wall For bedroom
    glColor3f(0.2, 0.6, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-12, 0, -12)
    glVertex3f(-12, 10, -12)
    glVertex3f(12, 10, -12)
    glVertex3f(12, 0, -12)
    glEnd()

    #Another bedroom wall
    glColor3f(0.2, 0.6, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-12, 0, -12)
    glVertex3f(-12, 10, -12)
    glVertex3f(-12, 10, 12)
    glVertex3f(-12, 0, 12)
    glEnd()


    #Bedroom Ceiling
    glColor3f(0.2, 0.6, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-12, 10, -12)
    glVertex3f(12, 10, -12)
    glVertex3f(12, 10, 12)
    glVertex3f(-12, 10, 12)
    glEnd()

    glFlush()



def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()


