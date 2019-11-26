from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

rotateX, rotateY, box, boxposY, rotatelid, openstat = 0, 0, 0, 0, 0, 0
boxlength = 0.5

def drawbox(length, stat = 0):

    glPushMatrix()
    # Other Transformations
    if stat == openstat:
        glTranslatef( 0.0, -boxposY, 0.0 )     # Not included
        # glRotatef( 180, 0.0, 1.0, 0.0 )   # Not included
        # glScalef( 2.0, 2.0, 0.0 )         # Not included

    # FRONT
    glBegin(GL_POLYGON)
    glColor3f(0.76, 0.56, 0.16)
    glVertex3f( length,-length,-length)
    glVertex3f( length, length,-length)
    glVertex3f(-length, length,-length)
    glVertex3f(-length,-length,-length)
    glEnd()

    # BACK
    glBegin(GL_POLYGON)
    glVertex3f( length,-length, length)
    glVertex3f( length, length, length)
    glVertex3f(-length, length, length)
    glVertex3f(-length,-length, length)
    glEnd()

    # RIGHT
    glBegin(GL_POLYGON)
    glVertex3f( length,-length,-length)
    glVertex3f( length, length,-length)
    glVertex3f( length, length, length)
    glVertex3f( length,-length, length)
    glEnd()

    # LEFT
    glBegin(GL_POLYGON)
    glVertex3f(-length,-length, length)
    glVertex3f(-length, length, length)
    glVertex3f(-length, length,-length)
    glVertex3f(-length,-length,-length)
    glEnd()

    # TOP
    # glBegin(GL_POLYGON)
    # glVertex3f( length, length,  length)
    # glVertex3f( length, length, -length)
    # glVertex3f(-length, length, -length)
    # glVertex3f(-length, length,  length)
    # glEnd()

    # BOTTOM
    glBegin(GL_POLYGON)
    glVertex3f( length,-length,-length)
    glVertex3f( length,-length, length)
    glVertex3f(-length,-length, length)
    glVertex3f(-length,-length,-length)
    glEnd()

    # draw the lid
    if stat == 1:
        lidstat = 1
    else:
        lidstat = 0
    lid(length, lidstat)

    # draw outer edge - inner edge
    boxedge(length)
    boxedge(length-0.005)

    glPopMatrix()


def boxedge(l):

    glLineWidth(2)

    # bottom
    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    glVertex3f(-l,-l,-l)
    glVertex3f(-l,-l, l)
    glVertex3f( l,-l, l)
    glVertex3f( l,-l,-l)
    glEnd()

    # side
    glBegin(GL_LINES)
    glVertex3f(-l,-l,-l)
    glVertex3f(-l, l,-l)
    glVertex3f(-l,-l, l)
    glVertex3f(-l, l, l)
    glVertex3f( l,-l, l)
    glVertex3f( l, l, l)
    glVertex3f( l,-l,-l)
    glVertex3f( l, l,-l)
    glEnd()

    if boxlength == l:
        glBegin(GL_LINE_LOOP)
        glVertex3f(-l, l,-l)
        glVertex3f(-l, l, l)
        glVertex3f( l, l, l)
        glVertex3f( l, l,-l)
        glEnd()


def lid(length, stat):
    
    global rotatelid

    # left side
    glPushMatrix()
    glTranslatef(-length, length, 0.0)  # Not included
    if stat == 0:
        glRotatef(rotatelid, 0.0, 0.0, 1.0)

    # draw face
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0, 0.0, length)
    glVertex3f(0, 0.0,-length)
    glVertex3f(length, 0.0,-length)
    glVertex3f(length, 0.0, length)
    glEnd()

    # draw edges
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(0.0, 0.0, length)
    glVertex3f(length, 0.0, length)
    glVertex3f(length, 0.0,-length)
    glVertex3f(0.0, 0.0,-length)
    glEnd()
    glPopMatrix()

    # right side
    glPushMatrix()
    glTranslatef(length, length, 0.0)  # Not included
    if stat == 0:
        glRotatef(-rotatelid, 0.0, 0.0, 1.0)

    # draw face
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0, 0.0, length)
    glVertex3f(0, 0.0,-length)
    glVertex3f(-length, 0.0,-length)
    glVertex3f(-length, 0.0, length)
    glEnd()

    # draw edges
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(0.0, 0.0, length)
    glVertex3f(-length, 0.0, length)
    glVertex3f(-length, 0.0,-length)
    glVertex3f(0.0, 0.0,-length)
    glEnd()
    glPopMatrix()


def orient():
    # Rotate when user changes rotateX and rotateY
    glRotatef(rotateX, 1.0, 0.0, 0.0)
    glRotatef(rotateY, 0.0, 1.0, 0.0)


def specialKeys(key, x, y):

    global rotateX
    global rotateY
    # Right arrow - increase rotation by 5 degree
    if key == GLUT_KEY_RIGHT:
        rotateY += 5
    elif key == GLUT_KEY_LEFT:
        rotateY -= 5
    if key == GLUT_KEY_UP:
        rotateX += 5
    elif key == GLUT_KEY_DOWN:
        rotateX -= 5

    # Request display update
    glutPostRedisplay()


def keyboardKeys(key, x, y):

    ch = key.decode("utf-8")
    print(type(key), key, type(ch), ch)
    global openstat
    global box
    if key.decode() == ' ':
        if openstat == 0 and boxposY == 0:
            openstat = 1
            box += 1
            glutTimerFunc(1, openbox, 0)
            print("space")
        elif openstat == 1 and rotatelid == 120 and box < 5:
            openstat = 0
            glutTimerFunc(1, dropbox, 0)
            print("down")


def openbox(value):
    
    global rotatelid
    global openstat
    if rotatelid < 120:
        rotatelid += 1
        drawbox(boxlength-0.1)
        glutPostRedisplay()
        glutTimerFunc(16, openbox, 0)
    else:
        openstat = 1
        drawbox(boxlength-0.1)
        glutPostRedisplay()


def dropbox(value):

    global openstat
    global boxposY
    global rotatelid
    global boxlength
    global box
    if boxposY < 2.5:
        boxposY += 0.015
        drawbox(boxlength-0.1)
        glutPostRedisplay()
        glutTimerFunc(16, dropbox, 0)
    else:
        if openstat:
            box += 1
        openstat, rotatelid, boxposY = 0, 0, 0
        if box < 5:
            boxlength -= 0.1
        glutPostRedisplay()


def display():
    # Clear screen and Z-buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset transformations
    glLoadIdentity()

    # Buffer drawing here
    orient()
    if box < 5:
        drawbox(boxlength)
        drawbox(boxlength-0.1, 1)
    else:
        drawbox(boxlength)
    # End drawing

    glFlush()
    glutSwapBuffers()



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
    glutKeyboardFunc(keyboardKeys)
    glutSpecialFunc(specialKeys)

    # Pass control to GLUT for events
    glutMainLoop()


main()
