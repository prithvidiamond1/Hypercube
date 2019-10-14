
import pygame

from OpenGL.GL import *
from OpenGL.GLU import *

import math
import numpy

pygame.init()

pygame.display.set_mode((1280, 720), pygame.OPENGL|pygame.DOUBLEBUF)
pygame.display.set_caption('TESSARCT')

gluPerspective(90, (1280/720), 0.1, 50)

glTranslate(0, 0, -2)

# glRotatef(290, 1, 1, 1)
glRotatef(250, 0, 1, 0)

theta = 0

while 0 <= theta < 360:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    theta += 0.5
    if theta >= 359:
        theta = 0
    else:
        pass

    omega = theta * (math.pi/180)

    # print(omega)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    dbrotation_mat = [[math.cos(omega), (math.sin(omega)), 0, 0],
                      [-(math.sin(omega)), math.cos(omega), 0, 0],    # reversed xy rotation direction
                      [0, 0, math.cos(omega), -(math.sin(omega))],
                      [0, 0, math.sin(omega), math.cos(omega)]]

    zw_rotation_mat = [[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, math.cos(omega), -(math.sin(omega))],
                       [0, 0, math.sin(omega), math.cos(omega)]]

    xy_rotation_mat = [[math.cos(omega), -(math.sin(omega)), 0, 0],
                       [(math.sin(omega)), math.cos(omega), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]]

    ###################

    hypercube_coords = [
        [-1, 1, 1, 1],
        [-1, 1, -1, 1],
        [1, 1, -1, 1],
        [1, 1, 1, 1],
        [-1, -1, 1, 1],
        [-1, -1, -1, 1],
        [1, -1, -1, 1],
        [1, -1, 1, 1],
        [-1, 1, 1, -1],
        [-1, 1, -1, -1],
        [1, 1, -1, -1],
        [1, 1, 1, -1],
        [-1, -1, 1, -1],
        [-1, -1, -1, -1],
        [1, -1, -1, -1],
        [1, -1, 1, -1]
    ]

    projected_coords = []

    p = 2.5  # projection offset

    for i in hypercube_coords:
        x = i[0]
        y = i[1]
        z = i[2]
        w = i[3]

        rotatedpoint_mat = numpy.dot(dbrotation_mat, [[x],[y],[z],[w]])

        r_x = rotatedpoint_mat[0][0]
        r_y = rotatedpoint_mat[1][0]
        r_z = rotatedpoint_mat[2][0]
        r_w = rotatedpoint_mat[3][0]

        p_x = r_x / (r_w + p)
        p_y = r_y / (r_w + p)
        p_z = r_z / (r_w + p) #p_w not required as we are projecting 4D to 3D i.e 4 co-ords to 3 co-ords

        projected_coords.append([p_x, p_y, p_z])

    # print(projected_coords, len(projected_coords))

    ###################

    def tesseract():
        l = projected_coords
        glBegin(GL_LINES)

        glVertex3f(l[0][0], l[0][1], l[0][2])     #
        glVertex3f(l[1][0], l[1][1], l[1][2])     #

        glVertex3f(l[1][0], l[1][1], l[1][2])     #
        glVertex3f(l[9][0], l[9][1], l[9][2])     #

        glVertex3f(l[2][0], l[2][1], l[2][2])     #
        glVertex3f(l[10][0], l[10][1], l[10][2])  #

        glVertex3f(l[7][0], l[7][1], l[7][2])     #
        glVertex3f(l[4][0], l[4][1], l[4][2])     #

        glVertex3f(l[4][0], l[4][1], l[4][2])     #
        glVertex3f(l[5][0], l[5][1], l[5][2])     #

        glVertex3f(l[5][0], l[5][1], l[5][2])     #
        glVertex3f(l[6][0], l[6][1], l[6][2])     #

        glVertex3f(l[6][0], l[6][1], l[6][2])     #
        glVertex3f(l[7][0], l[7][1], l[7][2])     #

        glVertex3f(l[7][0], l[7][1], l[7][2])     #
        glVertex3f(l[3][0], l[3][1], l[3][2])     #

        glVertex3f(l[3][0], l[3][1], l[3][2])     #
        glVertex3f(l[11][0], l[11][1], l[11][2])  #

        glVertex3f(l[1][0], l[1][1], l[1][2])     #
        glVertex3f(l[2][0], l[2][1], l[2][2])     #

        glVertex3f(l[1][0], l[1][1], l[1][2])     #
        glVertex3f(l[0][0], l[0][1], l[0][2])     #

        glVertex3f(l[2][0], l[2][1], l[2][2])     #
        glVertex3f(l[6][0], l[6][1], l[6][2])     #

        glVertex3f(l[2][0], l[2][1], l[2][2])     #
        glVertex3f(l[3][0], l[3][1], l[3][2])     #

        glVertex3f(l[1][0], l[1][1], l[1][2])     #
        glVertex3f(l[5][0], l[5][1], l[5][2])     #

        glVertex3f(l[4][0], l[4][1], l[4][2])     #
        glVertex3f(l[12][0], l[12][1], l[12][2])  #

        glVertex3f(l[13][0], l[13][1], l[13][2])  #
        glVertex3f(l[5][0], l[5][1], l[5][2])     #

        glVertex3f(l[14][0], l[14][1], l[14][2])  #
        glVertex3f(l[6][0], l[6][1], l[6][2])     #

        glVertex3f(l[15][0], l[15][1], l[15][2])  #
        glVertex3f(l[7][0], l[7][1], l[7][2])     #

        glVertex3f(l[8][0], l[8][1], l[8][2])     #
        glVertex3f(l[0][0], l[0][1], l[0][2])     #

        glVertex3f(l[3][0], l[3][1], l[3][2])     #
        glVertex3f(l[0][0], l[0][1], l[0][2])     #

        glVertex3f(l[4][0], l[4][1], l[4][2])     #
        glVertex3f(l[0][0], l[0][1], l[0][2])     #

        glVertex3f(l[9][0], l[9][1], l[9][2])     #
        glVertex3f(l[8][0], l[8][1], l[8][2])     #

        glVertex3f(l[9][0], l[9][1], l[9][2])     #
        glVertex3f(l[10][0], l[10][1], l[10][2])  #

        glVertex3f(l[14][0], l[14][1], l[14][2])  #
        glVertex3f(l[10][0], l[10][1], l[10][2])  #

        glVertex3f(l[15][0], l[15][1], l[15][2])  #
        glVertex3f(l[14][0], l[14][1], l[14][2])  #

        glVertex3f(l[12][0], l[12][1], l[12][2])  #
        glVertex3f(l[15][0], l[15][1], l[15][2])  #

        glVertex3f(l[11][0], l[11][1], l[11][2])  #
        glVertex3f(l[10][0], l[10][1], l[10][2])  #

        glVertex3f(l[13][0], l[13][1], l[13][2])  #
        glVertex3f(l[12][0], l[12][1], l[12][2])  #

        glVertex3f(l[11][0], l[11][1], l[11][2])  #
        glVertex3f(l[8][0], l[8][1], l[8][2])     #

        glVertex3f(l[13][0], l[13][1], l[13][2])  #
        glVertex3f(l[14][0], l[14][1], l[14][2])  #

        glVertex3f(l[11][0], l[11][1], l[11][2])  #
        glVertex3f(l[15][0], l[15][1], l[15][2])  #

        glVertex3f(l[13][0], l[13][1], l[13][2])  #
        glVertex3f(l[9][0], l[9][1], l[9][2])     #

        glVertex3f(l[8][0], l[8][1], l[8][2])     #
        glVertex3f(l[12][0], l[12][1], l[12][2])  #

        glEnd()

    displaylist1 = glGenLists(1)
    glNewList(displaylist1, GL_COMPILE)
    tesseract()
    glEndList()

    ###################

    glMatrixMode(GL_MODELVIEW)

    glCallList(displaylist1)

    pygame.display.flip()

    projected_coords.clear()

    pygame.time.delay(5)

pygame.quit()
quit()
