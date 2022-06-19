import pygame
import os
from OpenGL.GL import *

def MTL(filename='bedroom_design.mtl'):
    contents = {}
    mtl = None
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
        elif mtl is None:
            raise ValueError("mtl file doesn't start with newmtl stmt")
        elif values[0] == 'map_Kd':
            # load the texture referred to by this declaration
            mtl[values[0]] = values[1]
            surf = pygame.image.load(mtl['map_Kd'])
            image = pygame.image.tostring(surf, 'RGBA', 1)
            ix, iy = surf.get_rect().size
            texid = mtl['texture_Kd'] = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texid)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA,
                GL_UNSIGNED_BYTE, image)
        else:
            mtl[values[0]] = list(map(float, values[1:]))
    return contents
class FaceGroup(object):
    def __init__(self):
        self.indices = []
        self.material_name = ""
class OBJ:
    
    def __init__(self, filename):
        self.vertices = []
        self.tex_coord = []
        self.normal = []
        self.face_group = []
        self.materials = []
        self.display_list_id = None
        self.filename = filename

      
    def readObj(self):
        current_face_group = None
        file = open(self.filename, 'r')
        for line in file:
            values = line.split()
            first = values[0]
            if first == "mtlib":
                self.mtl = MTL(values[1])
            # if first == '#':
            #     continue
            elif first == 'v':
                x, y, z = values[1:]
                vertex = (float(x), float(y), float(z))
                self.vertices.append(vertex)
            elif first == "vt":
                x, y, z = values[1:]
                texture = (float(x), float(y), float(z))
                self.textureCoord.append(texture)
            elif first == 'vn':
                x, y, z = values[1:]
                normal = (float(x), float(y), float(z))
                self.normals.append(normal)
            elif first == "usemtl":
                current_face_group = FaceGroup()
                current_face_group.material_name = values[1]
                self.face_group.append(current_face_group)
            elif first == "f":
                assert len(values[1:]) == 3
                for values in values[1:]:
                    v1, t1, n1 = values.split('/')
                    indices = (int(v1) - 1, int(t1) - 1, int(n1) - 1)
                current_face_group.indices.append(indices)
 
        gl_list = glGenLists(1)
        glNewList(gl_list, GL_COMPILE)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        for face in current_face_group.indices:
            vertices, normals, texture_coords, material = face
            mtl = self.mtl[material]
            if 'texture_Kd' in mtl:
                # use diffuse texmap
                glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
            else:
                # just use diffuse colour
                glColor(*mtl['Kd'])


            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normal[normals[i] - 1])
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.tex_coord[texture_coords[i] - 1])
                glVertex3fv(self.vertices[vertices[i] - 1])
                glEnd()
            glDisable(GL_TEXTURE_2D)
            glEndList()
