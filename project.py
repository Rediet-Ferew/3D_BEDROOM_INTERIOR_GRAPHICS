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
    display = (1200, 800)
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
    glVertex3f(-12, 0, -12)
    glVertex3f(-12, 10, -12)
    glVertex3f(12, 10, -12)
    glVertex3f(12, 0, -12)
    glEnd()

    #Another bedroom wall
    glColor3f(0.2, 0.8, 0.9)
    glBegin(GL_QUADS)
    glVertex3f(-12, 0, -12)
    glVertex3f(-12, 10, -12)
    glVertex3f(-12, 10, 12)
    glVertex3f(-12, 0, 12)
    glEnd()

    #yet another wall
    glColor3f(0.2, 0.8, 0.9)
    glBegin(GL_QUADS)
    glVertex3f(12, 0, -12)
    glVertex3f(12, 10, -12)
    glVertex3f(12, 10, 12)
    glVertex3f(12, 0, 12)
    glEnd()
    #Bedroom Ceiling
    glColor3f(0.9, 0.6, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-12, 10, -12)
    glVertex3f(12, 10, -12)
    glVertex3f(12, 10, 12)
    glVertex3f(-12, 10, 12)
    glEnd()
    #Bedroom Door

    ##LeftWall from Door
    # glColor3f(0.9, 0.0, 0.5)
    # glBegin(GL_QUADS)
    # glVertex3f(-12, 0, 12)
    # glVertex3f(-12, 10, 12)
    # glVertex3f(-8, 10, 12)
    # glVertex3f(-8, 0, 12)
    # glEnd()
    #
    # #RightWall from Door
    # glColor3f(0.9, 0.9, 0.5)
    # glBegin(GL_QUADS)
    # glVertex3f(-6, 0, 12)
    # glVertex3f(-6, 8, 12)
    # glVertex3f(12, 8, 12)
    # glVertex3f(12, 0, 12)
    # glEnd()
    #
    # glColor3f(0.9, 0.9, 0.7)
    # glBegin(GL_QUADS)
    # glVertex3f(-6, 10, 12)
    # glVertex3f(-6, 8, 12)
    # glVertex3f(-8, 10, 12)
    # glVertex3f(-8, 10, 12)
    # glEnd()
    #
    # #Lines for lining the door
    # glColor3f(0.3, 0.9, 0.7)
    #
    # glBegin(GL_LINES)
    # glVertex3f(-6, 5, 12)
    # glVertex3f(-3, 5, 12)
    # glEnd()
    #
    # glBegin(GL_LINES)
    # glVertex3f(-6, 5, 12)
    # glVertex3f(-6, 0, 12)
    # glEnd()
    #
    # glBegin(GL_LINES)
    # glVertex3f(-3, 0, 12)
    # glVertex3f(-3, 5, 12)
    # glEnd()

    #drawBed

    glBegin(GL_QUADS)
    #back of kumsatn
    glVertex3f(1.5, 0.9, -1.5)
    glVertex3f(1.5, 5, -1.5)
    glVertex3f(4, 5, -1.5)
    glVertex3f(4, 0.9, -1.5)

    #left of kumsatn
    glVertex3f(1.5, 0.9, -1.5)
    glVertex3f(1.5, 5, -1.5)
    glVertex3f(1.5, 5, 1.5)
    glVertex3f(1.5, 0.9, 1.5)
    #right
    glVertex3f(4, 0.9, -1.5)
    glVertex3f(4, 5, -1.5)
    glVertex3f(4, 5, 1.5)
    glVertex3f(4, 0.9, 1.5)
    #
    #front
    #frontleft
    glVertex3f(1.5, 0.9, 1.5)
    glVertex3f(1.5, 5, 1.5)
    glVertex3f(2.75, 5, 1.5)
    glVertex3f(2.75, 0.9, 1.5)
    # glColor3f(1.0, 0.0, 0.0)

    #front right
    glVertex3f(2.8, 0.9, 1.5)
    glVertex3f(2.8, 5, 1.5)
    glVertex3f(4, 5, 1.5)
    glVertex3f(4, 0.9, 1.5)

    glVertex3f(1.5, 5, 0)
    glVertex3f(1.5, 5, 1.5)
    glVertex3f(4, 5, 0)
    glVertex3f(4, 5, 1.5)
    glEnd()

    #Lines for kumsatn
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    #left front
    glVertex3f(1.8, 0.8, 0.6)
    glVertex3f(1.8, 5.15, 0.6)
    #left back
    glVertex3f(1.8, 0.8, -2.45)
    glVertex3f(1.8, 5.15, -2.45)
    #left middle
    glVertex3f(3.155, 0.8, 0.6)
    glVertex3f(3.155, 5.15, 0.6)
    #right middle
    glVertex3f(3.2, 0.8, 0.6)
    glVertex3f(3.2, 5.15, 0.6)
    # # rightmiddle
    # glVertex3f(0.25, 0.8, 0.5)
    # glVertex3f(0.25, 5.15, 0.5)
    #floor left
    glVertex3f(1.85, 0.8, 0.5)
    glVertex3f(3.18, 0.8, 0.5)

    # floor right
    glVertex3f(3.25, 0.8, 0.5)
    glVertex3f(4.55, 0.8, 0.5)
    # #upper left
    glVertex3f(1.85, 5.15, 0.5)
    glVertex3f(3.18, 5.15, 0.5)
    # #upper right
    glVertex3f(3.25, 5.15, 0.5)
    glVertex3f(4.55, 5.15, 0.5)
    #right front
    glVertex3f(4.48, 0.8, 0.6)
    glVertex3f(4.48, 5.15, 0.6)

    #upper left left
    glVertex3f(1.85, 5.15, -2.45)
    glVertex3f(1.85, 5.15, 0.6)

    glVertex3f(1.85, 0.8, -2.45)
    glVertex3f(1.85, 0.8, 0.6)
    glEnd()



    glColor3f(0.5, 0.5, 0.5)
    # glPushMatrix()
    # glTranslatef(0.1, 2.5, 0.5)
    # glRotatef(90.0, 0.0, 1.0, 0.0)
    # glutSolidTorus(0.03, 0.1, 100, 100)
    # glPopMatrix()

    #Add Alga
    glColor3f(0.3, 0.2, 0.2)
    glBegin(GL_QUADS)
    #Back of Alga
    glVertex3f(-10, 0, -10)
    glVertex3f(-10, 2.2, -10)
    glVertex3f(-1, 2.2, -10)
    glVertex3f(-1, 0, -10)

    #Left of alga
    glColor3f(0.1, 0.5, 0.5)
    glVertex3f(-9.85, 0, -10)
    glVertex3f(-9.85, 0.8, -10)
    glVertex3f(-9, 0.8, 1)
    glVertex3f(-9, 0, 1)

    #right of alga
    glColor3f(0.8, 0.5, 0.5)
    glVertex3f(-1.15, 0, -10)
    glVertex3f(-1.15, 0.8, -10)
    glVertex3f(-1.95, 0.8, 1)
    glVertex3f(-1.95, 0, 1)
    #front of alga
    glColor3f(0.1, 0.2, 0.3)
    glVertex3f(-9, 0, 1)
    glVertex3f(-9, 0.8, 1)
    glVertex3f(-1.95, 0.8, 1)
    glVertex3f(-1.95, 0, 1)

    #Frash Adding
    glColor3f(0.0, 0.0, 0.0)

    glVertex3f(-9.90, 0.9, -10)
    glVertex3f(-1.25, 0.9, -10)
    glVertex3f(-1.8, 0.7, 0.3)
    glVertex3f(-9.15, 0.7, 0.3)
    glEnd()

    #Dresser
    glBegin(GL_QUADS)
    #back of dresser
    glColor3f(0.0, 0.0, 0.0)

    glVertex3f(-1.6, 0.9, -1.5)
    glVertex3f(-1.6, 2.5, -1.5)
    glVertex3f(0.5, 2.5, -1.5)
    glVertex3f(0.5, 0.9, -1.5)

    #left Dresser
    glColor3f(0.9, 0.9, 0.9)
    glVertex3f(-1.6, 0.9, -1.5)
    glVertex3f(-1.6, 2.5, -1.5)
    glVertex3f(-1.6, 2.5, 1.5)
    glVertex3f(-1.6, 0.9, 1.5)

    #right of dresser
    glVertex3f(0.5, 0.9, -1.5)
    glVertex3f(0.5, 2.5, -1.5)
    glVertex3f(0.5, 2.5, 1.5)
    glVertex3f(0.5, 0.9, 1.5)

    #front of dresser left
    glVertex3f(-1.6, 0.9, 1.5)
    glVertex3f(-1.6, 2.5, 1.5)
    glVertex3f(-.5, 2.5, 1.5)
    glVertex3f(-.5, 0.9, 1.5)

    #front of dresser right

    glVertex3f(-.6, 0.9, 1.5)
    glVertex3f(-.6, 2.5, 1.5)
    glVertex3f(.5, 2.5, 1.5)
    glVertex3f(.5, 0.9, 1.5)


    #upper of dresser
    glVertex3f(-1.6, 2.5, 1.5)
    glVertex3f(-1.6, 2.5, 1.5)
    glVertex3f(0.5, 2.5, 1.5)
    glVertex3f(0.5, 2.5, 1.5)


    #floor of dresser
    glVertex3f(-1.6, 2.5, 1.5)
    glVertex3f(-1.6, 2.5, 1.5)
    glVertex3f(0.5, 2.5, 1.5)
    glVertex3f(0.5, 2.5, 1.5)



    glEnd()


    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-1.6, 0.9, 1.5)
    glVertex3f(-1.6, 2.5, 1.5)

    glVertex3f(-.5, 2.5, 1.5)
    glVertex3f(-.5, 0.9, 1.5)

    glVertex3f(-.6, 0.9, 1.5)
    glVertex3f(-.6, 2.5, 1.5)
    glVertex3f(.5, 2.5, 1.5)
    glVertex3f(.5, 0.9, 1.5)

    glVertex3f(-.6, 0.9, 1.5)
    glVertex3f(-.6, 2.5, 1.5)
    glVertex3f(.5, 2.5, 1.5)
    glVertex3f(.5, 0.9, 1.5)

    glEnd()

    #mirror and dresser
    glColor(0.2, 0.2, 0.2)
    glBegin(GL_QUADS)

    #side of dresser under mirror
    glVertex3f(-12, 0, 5.5)
    glVertex3f(-12, 1.5, 5.5)
    glVertex3f(-10.5, 1.5, 5.5)
    glVertex3f(-10.5, 0, 5.5)

    #front of dresser under mirror
    glVertex3f(-10.5, 0, 5.5)
    glVertex3f(-10.5, 1.5, 5.5)
    glVertex3f(-10.5, 1.5, 2.5)
    glVertex3f(-10.5, 0, 2.5)

    #back of dresser under mirror
    glVertex3f(-12, 0, 5.5)
    glVertex3f(-12, 1.5, 5.5)
    glVertex3f(-12, 1.5, 2.5)
    glVertex3f(-12, 0, 2.5)

    #other side of dresser under mirror

    glVertex3f(-12, 0, 2.5)
    glVertex3f(-12, 1.5, 2.5)
    glVertex3f(-10.5, 1.5, 2.5)
    glVertex3f(-10.5, 0, 2.5)

    #ceiling of dresser under mirror
    glColor3f(0.1, 0.1, 0.1)
    glVertex3f(-12, 1.5, 5.5)
    glVertex3f(-12, 1.5, 5.5)
    glVertex3f(-10.5, 1.5, 2.5)
    glVertex3f(-10.5, 1.5, 2.5)

    #floor of dresser above mirror
    glVertex3f(-12, 0, 5.5)
    glVertex3f(-12, 0, 5.5)
    glVertex3f(-10.5, 0, 2.5)
    glVertex3f(-10.5, 0, 2.5)
    glEnd()
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


