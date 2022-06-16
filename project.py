import random
import pygame
import OpenGL
import pygame
from OpenGL import GLU, GL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pyrr


def init():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(.30, 0.20, 0.20, 1.0)
    # glViewport(0, 0, 500, 500)
    gluPerspective(45, (display[0] / display[1]), 0.1, 150.0)
    # glTranslatef(random.randrange(-5, 5), 0, -20)

lx = 0
ly = 0
lz = -1
x = -5.0
z = 18.0
roll = 0
def draw():
    # glMatrixMode(GL_MODELVIEW)



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
    glVertex3f(-10, 0, -10)
    glVertex3f(-10, 8, -10)
    glVertex3f(10, 8, -10)
    glVertex3f(10, 0, -10)
    glEnd()

    #Another bedroom wall
    glColor3f(0.2, 0.8, 0.9)
    glBegin(GL_QUADS)
    glVertex3f(-10, 0, -10)
    glVertex3f(-10, 8, -10)
    glVertex3f(-10, 8, 10)
    glVertex3f(-10, 0, 10)
    glEnd()

    #Bedroom Ceiling
    glColor3f(0.9, 0.6, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-10, 8, -10)
    glVertex3f(10, 8, -10)
    glVertex3f(10, 8, 10)
    glVertex3f(-10, 8, 10)
    glEnd()
    #Bedroom Door

    #LeftWall from Door
    glColor3f(0.9, 0.0, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-10, 0, 10)
    glVertex3f(-10, 8, 10)
    glVertex3f(-6, 8, 10)
    glVertex3f(-6, 0, 10)
    glEnd()

    #RightWall from Door
    glColor3f(0.9, 0.9, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-3, 0, 10)
    glVertex3f(-3, 8, 10)
    glVertex3f(10, 8, 10)
    glVertex3f(10, 0, 10)
    glEnd()

    glColor3f(0.9, 0.9, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-3, 8, 10)
    glVertex3f(-3, 6, 10)
    glVertex3f(-6, 6, 10)
    glVertex3f(-6, 8, 10)
    glEnd()

    #Lines for lining the door
    glColor3f(0.3, 0.9, 0.7)
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex3f(-6, 5, 10)
    glVertex3f(-3, 5, 10)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-6, 5, 10)
    glVertex3f(-6, 0, 10)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-3, 0, 10)
    glVertex3f(-3, 5, 10)
    glEnd()

    #drawBed

    # glBegin(GL_QUADS)
    # glVertex3f(-2, -0.2, 2)
    # glVertex3f(2, -0.2, 2)
    # glVertex3f(2, 0.2, 2)
    # glVertex3f(-2, 0.2, 2)
    # glEnd()
    glFlush()



def main():
    init()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # GL.glLoadIdentity()
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GLU.gluLookAt(x, 2.5, z, x + lx, 2.5 + ly, z + lz, roll + 0, 2.5, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()


