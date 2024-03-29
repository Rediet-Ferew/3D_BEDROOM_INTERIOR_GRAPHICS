import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

# IMPORT OBJECT LOADER
from objloader import *

def init():
    viewport = (1000,800)
    hx = viewport[0]
    hy = viewport[1]
    srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    glClearColor(.30, 0.20, 0.20, 1.0)
    # glViewport(0, 0, 500, 500)
    width, height = viewport
    gluPerspective(45.0, width/float(height), 1, 100.0)
    # glTranslatef(random.randrange(-5, 5), 0, -20)
    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    
obj = OBJ('bedroom_design.obj')
clock = pygame.time.Clock()
lx = 0
ly = 0
lz = -1
x = -5.0
z = 18.0
roll = 0

def main():
    init()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # GL.glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(x, 2.5, z, x + lx, 2.5 + ly, z + lz, roll + 0, 2.5, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        rx, ry = (0,0)
        tx, ty = (0,0)
        zpos = 5
        rotate = move = False
        while 1:
            
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                elif e.type == KEYDOWN and e.key == K_ESCAPE:
                    sys.exit()
                elif e.type == MOUSEBUTTONDOWN:
                    if e.button == 4: zpos = max(1, zpos-1)
                    elif e.button == 5: zpos += 1
                    elif e.button == 1: rotate = True
                    elif e.button == 3: move = True
                elif e.type == MOUSEBUTTONUP:
                    if e.button == 1: rotate = False
                    elif e.button == 3: move = False
                elif e.type == MOUSEMOTION:
                    i, j = e.rel
                    if rotate:
                        rx += i
                        ry += j
                    if move:
                        tx += i
                        ty -= j
                        rx, ry = (0,0)
                        tx, ty = (0,0)
                        zpos = 5
                        rotate = move = False
        
                    
        glTranslate(tx/20., ty/20., - zpos)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)
        glCallList(obj.gl_list)
        
        pygame.display.flip()
        pygame.time.wait(10)


main()