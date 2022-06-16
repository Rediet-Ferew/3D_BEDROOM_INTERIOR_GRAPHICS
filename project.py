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

    #LeftWall from Door
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
    glVertex3f(-1.5, 0.9, -1.5)
    glVertex3f(-1.5, 5, -1.5)
    glVertex3f(1.5, 5, -1.5)
    glVertex3f(1.5, 0.9, -1.5)

    #left of kumsatn
    glVertex3f(-1.5, 0.9, -1.5)
    glVertex3f(-1.5, 5, -1.5)
    glVertex3f(-1.5, 5, 1.5)
    glVertex3f(-1.5, 0.9, 1.5)
    #right
    glVertex3f(1.5, 0.9, -1.5)
    glVertex3f(1.5, 5, -1.5)
    glVertex3f(1.5, 5, 1.5)
    glVertex3f(1.5, 0.9, 1.5)

    #front
    glVertex3f(-1.5, 0.9, 1.5)
    glVertex3f(-1.5, 5, 1.5)
    glVertex3f(1.5, 5, 1.5)
    glVertex3f(1.5, 0.9, 1.5)
    glColor3f(1.0, 0.0, 0.0)

    glEnd()

    #Lines for kumsatn
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    #left front
    glVertex3f(-1.3, 0.8, 0.5)
    glVertex3f(-1.3, 5.15, 0.5)
    #left back
    glVertex3f(-1.3, 0.8, -2.6)
    glVertex3f(-1.3, 5.15, -2.6)
    #right front
    glVertex3f(1.9, 0.8, 0.5)
    glVertex3f(1.9, 5.15, 0.5)
    #middle
    glVertex3f(0.25, 0.8, 0.5)
    glVertex3f(0.25, 5.15, 0.5)
    #floor
    glVertex3f(-1.3, 0.8, 0.5)
    glVertex3f(1.9, 0.8, 0.5)
    #upper
    glVertex3f(-1.3, 5.15, 0.5)
    glVertex3f(1.9, 5.15, 0.5)
    #upperleft
    glVertex3f(-1.3, 5.15, -2.6)
    glVertex3f(-1.3, 5.15, 0.5)
    glEnd()
    glFlush()
    glColor3f(0.5, 0.5, 0.5)
    # glPushMatrix()
    # glTranslatef(0.1, 2.5, 0.5)
    # glRotatef(90.0, 0.0, 1.0, 0.0)
    # glutSolidTorus(0.03, 0.1, 100, 100)
    # glPopMatrix()



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


