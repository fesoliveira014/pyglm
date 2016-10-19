from glvector import *
from glmatrix import *
from math import cos, sin, tan

def translate(m, v):
    '''
    Builds a translation 4 * 4 matrix created from a vector of 3 components.
    
    @param m Input matrix multiplied by this translation matrix.
    @param v Coordinates of a translation vector.
    '''

    res = mat4.fromMat4(m)
    res[3] = m[0] * v[0] + m[1] * v[1] + m[2] * v[2] + m[3]
    return res
    

def rotate(m, angle, v):
    '''
    Builds a rotation 4 * 4 matrix created from an axis vector and an angle. 
    
    @param m Input matrix multiplied by this rotation matrix.
    @param angle Rotation angle expressed in radians.
    @param axis Rotation axis, recommended to be normalized.
    '''

    a = angle
    c = cos(a)
    s = sin(a)

    axis = normalize(v)
    temp = (axis * (1 - c))

    Rotate = mat4()
    Rotate[0][0] = c + temp[0] * axis[0]
    Rotate[0][1] = 0 + temp[0] * axis[1] + s * axis[2]
    Rotate[0][2] = 0 + temp[0] * axis[2] - s * axis[1]
    Rotate[1][0] = 0 + temp[1] * axis[0] - s * axis[2]
    Rotate[1][1] = c + temp[1] * axis[1]
    Rotate[1][2] = 0 + temp[1] * axis[2] + s * axis[0]
    Rotate[2][0] = 0 + temp[2] * axis[0] + s * axis[1]
    Rotate[2][1] = 0 + temp[2] * axis[1] - s * axis[0]
    Rotate[2][2] = c + temp[2] * axis[2]

    Result = mat4()
    Result[0] = m[0] * Rotate[0][0] + m[1] * Rotate[0][1] + m[2] * Rotate[0][2]
    Result[1] = m[0] * Rotate[1][0] + m[1] * Rotate[1][1] + m[2] * Rotate[1][2]
    Result[2] = m[0] * Rotate[2][0] + m[1] * Rotate[2][1] + m[2] * Rotate[2][2]
    Result[3] = m[3]

    return Result

def scale(m, v):
    '''
    Builds a scale 4 * 4 matrix created from 3 scalars. 
    
    @param m Input matrix multiplied by this scale matrix.
    @param v Ratio of scaling for each axis.
    '''
    res = mat4()
    res[0] = m[0] * v[0]
    res[1] = m[1] * v[1]
    res[2] = m[2] * v[2]
    res[3] = m[3]

    return res

def ortho(left, right, bottom, top, zNear=None, zFar=None):
    '''
    Creates a matrix for an orthographic parallel viewing volume.
    
    @param left 
    @param right 
    @param bottom 
    @param top 
    @param zNear 
    @param zFar 
    '''

    Result = mat4.identity()
    Result[0][0] = 2 / (right - left)
    Result[1][1] = 2 / (top - bottom)

    if not (zNear == None and zFar == None):
        Result[2][2] = - 2 / (zFar - zNear)
    else:
        Result[2][2] = - 1

    Result[3][0] = - (right + left) / (right - left)
    Result[3][1] = - (top + bottom) / (top - bottom)

    if not (zNear == None and zFar == None):
        Result[3][2] = - (zFar + zNear) / (zFar - zNear)

    return Result

def perspective(fovy, aspect, zNear, zFar):
    '''
    Creates a matrix for a symetric perspective-view frustum based on the default handedness.
    
    @param fovy Specifies the field of view angle in the y direction. Expressed in radians.
    @param aspect Specifies the aspect ratio that determines the field of view in the x direction. The aspect ratio is the ratio of x (width) to y (height).
    @param near Specifies the distance from the viewer to the near clipping plane (always positive).
    @param far Specifies the distance from the viewer to the far clipping plane (always positive).
    '''

    if not abs(aspect - 2.220446049250313e-16) > 0:
        raise FloatingPointError("The aspect must be bigger than 0.")

    tanHalfFovy = tan(fovy / 2)

    Result = mat4()
    Result[0][0] = 1 / (aspect * tanHalfFovy)
    Result[1][1] = 1 / (tanHalfFovy)
    Result[2][2] = - (zFar + zNear) / (zFar - zNear)
    Result[2][3] = - 1
    Result[3][2] = - (2 * zFar * zNear) / (zFar - zNear)
    return Result;

def project(obj, model, proj, viewport):
    '''
    Map the specified object coordinates (obj.x, obj.y, obj.z) into window coordinates.
    
    @param obj Specify the object coordinates.
    @param model Specifies the current modelview matrix
    @param proj Specifies the current projection matrix
    @param viewport Specifies the current viewport
    @return Return the computed window coordinates.
    '''

def unproject(win, model, proj, viewport):
    '''
    Map the specified window coordinates (win.x, win.y, win.z) into object coordinates.
    
    @param win Specify the window coordinates to be mapped.
    @param model Specifies the modelview matrix
    @param proj Specifies the projection matrix
    @param viewport Specifies the viewport
    '''

def lookAt(eye, center, up):
    '''
    Build a look at view matrix based on the default handedness.
    
    @param eye Position of the camera
    @param center Position where the camera is looking at
    @param up Normalized up vector, how the camera is oriented. Typically (0, 0, 1)
    '''