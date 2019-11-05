from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

rotate_y = 0
rotate_x = 0
buka = 0
sudut = 0


def kanan():

    # Blue side - TOP

    glTranslatef(-0.5, 0.5, 0.0)  # Not included
    glRotatef(sudut, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0, 0.0, 0.5)
    glVertex3f(0, 0.0, -0.5)
    glVertex3f(0.5, 0.0, -0.5)
    glVertex3f(0.5, 0.0, 0.5)
    glEnd()
    glRotatef(-sudut, 0.0, 0.0, 1.0)
    glTranslatef(0.5, -0.5, 0.0)  # Not included


def kiri():
    # Green side - TOP
    glTranslatef(0.5, 0.5, 0.0)  # Not included
    glRotatef(-sudut, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.5)
    glVertex3f(0.0, 0.0, -0.5)
    glVertex3f(-0.5, 0.0, -0.5)
    glVertex3f(-0.5, 0.0, 0.5)
    glEnd()
    glRotatef(sudut, 0.0, 0.0, 1.0)
    glTranslatef(-0.5, -0.5, 0.0)  # Not included


def display():
    # Clear screen and Z-buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset transformations
    glLoadIdentity()

    # Other Transformations
    # glTranslatef( 0.1, 0.0, 0.0 )     #  Not included
    # glRotatef( 180, 0.0, 1.0, 0.0 )   #  Not included

    # Rotate when user changes rotate_x and rotate_y
    glRotatef(rotate_x, 1.0, 0.0, 0.0)
    glRotatef(rotate_y, 0.0, 1.0, 0.0)

    # Other Transformations
    # glScalef( 2.0, 2.0, 0.0 )          # Not included

    # Multi-colored side - FRONT
    glBegin(GL_POLYGON)

    glColor3f(0.76, 0.56, 0.16)
    glVertex3f(0.5, -0.5, -0.5)      # P1 is red
    # glColor3f( 0.0, 1.0, 0.0 )
    glVertex3f(0.5, 0.5, -0.5)      # P2 is green
    # glColor3f( 0.0, 0.0, 1.0 )
    glVertex3f(-0.5, 0.5, -0.5)      # P3 is blue
    # glColor3f( 1.0, 0.0, 1.0 )
    glVertex3f(-0.5, -0.5, -0.5)      # P4 is purple

    glEnd()

    # White side - BACK
    glBegin(GL_POLYGON)
    # glColor3f(   1.0,  1.0, 1.0 )
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glEnd()

    # Purple side - RIGHT
    glBegin(GL_POLYGON)
    # glColor3f(  1.0,  0.0,  1.0 )
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glEnd()

    # Green side - LEFT
    glBegin(GL_POLYGON)
    # glColor3f(   0.0,  1.0,  0.0 )
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()

    # # Blue side - TOP
    # glBegin(GL_POLYGON)
    # glColor3f(   0.0,  0.0,  1.0 )
    # glVertex3f(  0.5,  0.5,  0.5 )
    # glVertex3f(  0.5,  0.5, -0.5 )
    # glVertex3f( -0.5,  0.5, -0.5 )
    # glVertex3f( -0.5,  0.5,  0.5 )
    # glEnd()

    # Red side - BOTTOM
    glBegin(GL_POLYGON)
    # glColor3f(   1.0,  0.0,  0.0 )
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()
    kanan()
    kiri()
    glFlush()
    glutSwapBuffers()


def specialKeys(key, x, y):

    global rotate_x
    global rotate_y
    # Right arrow - increase rotation by 5 degree
    if key == GLUT_KEY_RIGHT:
        rotate_y += 5
    elif key == GLUT_KEY_LEFT:
        rotate_y -= 5
    elif key == GLUT_KEY_UP:
        rotate_x += 5
    elif key == GLUT_KEY_DOWN:
        rotate_x -= 5

    # Request display update
    glutPostRedisplay()


def mouse(button, state, x, y):
    global buka
    global sudut
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and buka == 0:
        buka += 1
        print("ngeklik")
        glutTimerFunc(1, timer, 0)


def timer(value):
    global sudut
    sudut += 1
    glutPostRedisplay()
    if sudut < 120:
        glutTimerFunc(10, timer, 0)


def main():
    glutInit()

    # Request double buffered true color window with Z-buffer
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    # Create window
    glutCreateWindow("Kotak")

    # Enable Z-buffer depth test
    glEnable(GL_DEPTH_TEST)

    # Callback functions
    glutDisplayFunc(display)
    glutSpecialFunc(specialKeys)
    glutMouseFunc(mouse)

    # Pass control to GLUT for events
    glutMainLoop()


main()
