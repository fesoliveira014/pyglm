import math
from glvector import *
from glmatrix import *
from gltransform import *


def fract(x):
    return x - math.floor(x)

def mod(x, y):
    return x - y * math.floor(x / y)

def modf(x):
    if isinstance(x, float):
        frac = math.modf(x)
    elif isinstance(x, vec2):
        frac = vec2(math.modf(x.x), math.modf(x.y))
    elif isinstance(x, vec3):
        frac = vec3(math.modf(x.x), math.modf(x.y), math.modf(x.z))
    elif isinstance(x, vec4):
        frac = vec4(math.modf(x.x), math.modf(x.y), math.modf(x.z), math.modf(x.w))
    else:
        raise TypeError("Parameter must be either a float or a vector of floats.")
        
    return x - frac, frac

def min(x, y):
    return x if x < y else y

def max(x, y):
    return x if x > y else y

def clamp(x, minVal, maxVal):
    return min(max(x, minVal), maxVal)

def mix(x, y, a):
    if isinstance(a, bool):
        return y if a else x
    else:
        return x + a * y

def step(edge, x):
    return mix(1, 0, x < edge)

def smoothstep(edge0, edge1, x):
    if type(edge0) == type(x) and type(edge1) == type(x):
        tmp = clamp((x - edge0) / (edge1 - edge0), 0, 1)
        return tmp * tmp * (type(x)())

def fma(a, b, c):
    return a * b  + c



