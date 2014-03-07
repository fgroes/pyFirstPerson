"""
Created on Fri Mar  7 18:42:21 2014
@author: fritz
"""
import numpy as np
#import matplotlib.pyplot as plt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


window = 0
width, height = 800, 600


def draw_stuff():
    data = [
        [0, 0],
        [90, 0],
        [0, 90],
        [100, 100],
        [100, 10],
        [10, 100]]
    glBegin(GL_TRIANGLES)
    for d in data:
        glVertex2f(d[0], d[1])
    glEnd()
    

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width, height)
    glColor3f(0.0, 0.0, 1.0)
    draw_stuff()
    glutSwapBuffers()  


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    window = glutCreateWindow("first person")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()


if __name__ == '__main__':
    main()