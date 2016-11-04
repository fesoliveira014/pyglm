import math
from glvector, glmatrix import *
from gltransform import *

def fract(x):
	return x - math.floor(x)

def mod(x, y):
	return x - y * floor(x / y)

def modf(x):
	if isinstance(x, float):
		frac = math.modf(x)
	elif isinstance(x, vec2):
		frac = vec2(modf(x.x), modf(x.y))
	elif isinstance(x, vec3):
		frac = vec3(modf(x.x), modf(x.y), modf(x.z))
	elif isinstance(x, vec4):
		frac = vec4(modf(x.x), modf(x.y), modf(x.z), modf(x.w))
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

