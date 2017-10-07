import math
import glmatrix

class vec2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getitem__(self, key):
        if type(key) is int:
            if key is 0:
                return self.x
            elif key is 1:
                return self.y
            else:
                raise IndexError("Index out of bounds.")    
        else:
            raise TypeError("Invalid type.")

    def __setitem__(self, key, val):
        if type(key) is int:
            if key is 0:
                self.x = val
            elif key is 1:
                self.y = val
            else:
                raise IndexError("Index out of bounds.")    
        else:
            raise TypeError("Invalid type.")

    def __iter__(self):
        return iter([self.x, self.y])

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            y = self.y + other
            return vec2(x, y)
        elif isinstance(other, vec2):
            x = self.x + other.x
            y = self.y + other.y
            return vec2(x, y)
        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __iadd__(self, other):
        self = self + other
        return self

    def __radd__(self, other):
        self = self + other
        return self
        
    def __sub__(self, other):
        return self.__add__(-other)

    def __isub__(self, other):
        self = self - other
        return self

    def __rsub__(self, other):
        self = self - other
        return self

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = self.x * other
            y = self.y * other
            return vec2(x, y)
        elif isinstance(other, vec2):
            x = self.x * other.x
            y = self.y * other.y
            return vec2(x, y)
        elif isinstance(other, glmatrix.mat2):
            a = other[0][0] * self[0] + other[1][0] * self[1]
            b = other[0][1] * self[0] + other[1][1] * self[1]
            return vec2(a,b)

        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __imul__(self, other):
        self = self * other
        return self

    def __rmul__(self, other):
        self = self * other
        return self

    def __truediv__(self, other):   
        if isinstance(other, int) or isinstance(other, float):
            x = self.x / other
            y = self.y / other
            return vec2(x, y)

        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))    

    def __itruediv__(self, other):
        self = self / other
        return self

    def __rtruediv__(self, other):
        self = self / other
        return self

    def __floordiv__(self, other):
        if isinstance(other, int):
            x = self.x // other
            y = self.y // other
            return vec2(x, y)

        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __ifloordiv__(self, other):
        self = self // other
        return self

    def __rfloordiv__(self, other):
        self = self // other
        return self

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __lt__(self, other):
        return (self.x < other.x or (self.x == other .x and self.y < other.y))

    def __gt__(self, other):
        return (self.x > other.x or (self.x == other .x and self.y > other.y))

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __pos__(self):
        x = +self.x
        y = +self.y
        return vec2(x, y)

    def __neg__(self):
        x = -self.x
        y = -self.y
        return vec2(x, y)

    def __abs__(self):
        x = abs(self.x)
        y = abs(self.y)
        return vec2(x, y)

    def __round__(self, n=0):
        x = round(self.x, n)
        y = round(self.y, n)
        return vec2(x, y)

    def __floor__(self):
        x = math.floor(self.x)
        y = math.floor(self.y)
        return vec2(x, y)

    def __ceil__(self):
        x = math.ceil(self.x)
        y = math.ceil(self.y)
        return vec2(x, y)

    def __trunc__(self):
        x = math.trunc(self.x)
        y = math.trunc(self.y)
        return vec2(x, y)

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    def __repr__(self):
        return "vec2(" + str(self.x) + "," + str(self.y)    + ")"

    def __len__(self):
        return 2

    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    @property
    def unit(self):
        return self / self.length

    @classmethod
    def fromVec2(cls, vec):
        return cls(vec.x, vec.y)

    @classmethod
    def fromVec3(cls, vec):
        return cls(vec.x, vec.y)        
    
    @classmethod
    def fromVec4(cls, vec):
        return cls(vec.x, vec.y)



class vec3(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, key):
        if type(key) is int:
            if key is 0:
                return self.x
            elif key is 1:
                return self.y
            elif key is 2:
                return self.z
            else:
                raise IndexError("Index out of bounds.")    
        else:
            raise TypeError("Invalid type.")

    def __setitem__(self, key, val):
        if type(key) is int:
            if key is 0:
                self.x = val
            elif key is 1:
                self.y = val
            elif key is 2:
                self.z = val
            else:
                raise IndexError("Index out of bounds.")    
        else:
            raise TypeError("Invalid type.")

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            y = self.y + other
            z = self.z + other
            return vec3(x, y, z)
        elif isinstance(other, vec3):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return vec3(x, y, z)
        elif isinstance(other, glmatrix.mat3):
            a = other[0][0] * self[0] + other[1][0] * self[1] + other[2][0] * self[2]
            b = other[0][1] * self[0] + other[1][1] * self[1] + other[2][1] * self[2]
            c = other[0][2] * self[0] + other[1][2] * self[1] + other[2][2] * self[2]
        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __iadd__(self, other):
        self = self + other
        return self

    def __radd__(self, other):
        self = self + other
        return self
        
    def __sub__(self, other):
        return self.__add__(-other)

    def __isub__(self, other):
        self = self - other
        return self

    def __rsub__(self, other):
        self = self - other
        return self

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = self.x * other
            y = self.y * other
            z = self.z * other
            return vec3(x, y, z)
        elif isinstance(other, vec3):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            return vec3(x, y, z)
        elif isinstance(other, glmatrix.mat3):
            a = other[0][0] * self[0] + other[1][0] * self[1] + other[2][0] * self[2]
            b = other[0][1] * self[0] + other[1][1] * self[1] + other[2][1] * self[2]
            c = other[0][2] * self[0] + other[1][2] * self[1] + other[2][2] * self[2]
            return vec3(a,b,c)

        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __imul__(self, other):
        self = self * other
        return self

    def __rmul__(self, other):
        self = self * other
        return self

    def __truediv__(self, other):   
        if isinstance(other, int) or isinstance(other, float):
            x = self.x / other
            y = self.y / other
            z = self.z / other
            return vec3(x, y, z)

        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __itruediv__(self, other):
        self = self / other
        return self

    def __rtruediv__(self, other):
        self = self / other
        return self

    def __floordiv__(self, other):
        if isinstance(other, int):
            x = self.x // other
            y = self.y // other
            z = self.z // other
            return vec3(x, y, z)

        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __ifloordiv__(self, other):
        self = self // other
        return self

    def __rfloordiv__(self, other):
        self = self // other
        return self

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __lt__(self, other):
        return (self.x < other.x or (self.x == other .x and self.y < other.y) or (self.x == other.x and self.y == other.y and self.z < other.z))

    def __gt__(self, other):
        return (self.x > other.x or (self.x == other .x and self.y > other.y) or (self.x == other.x and self.y == other.y and self.z > other.z))

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __pos__(self):
        x = +self.x
        y = +self.y
        z = +self.z
        return vec3(x, y, z)

    def __neg__(self):
        x = -self.x
        y = -self.y
        z = -self.z
        return vec3(x, y, z)

    def __abs__(self):
        x = abs(self.x)
        y = abs(self.y)
        z = abs(self.z)
        return vec3(x, y, z)

    def __round__(self, n=0):
        x = round(self.x, n)
        y = round(self.y, n)
        z = round(self.z, n)
        return vec3(x, y, z)

    def __floor__(self):
        x = math.floor(self.x)
        y = math.floor(self.y)
        z = math.floor(self.z)
        return vec3(x, y, z)

    def __ceil__(self):
        x = math.ceil(self.x)
        y = math.ceil(self.y)
        z = math.ceil(self.z)
        return vec3(x, y, z)

    def __trunc__(self):
        x = math.trunc(self.x)
        y = math.trunc(self.y)
        z = math.trunc(self.z)
        return vec3(x, y, z)

    def __str__(self):
        return "(" + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ")"

    def __repr__(self):
        return "vec3(" + str(self.x) + "," + str(self.y)    + "," + str(self.z) + ")"

    def __len__(self):
        return 3

    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    @property
    def unit(self):
        return self / self.length

    @classmethod
    def fromVec2(cls, vec, z=0):
        return cls(vec.x, vec.y, z)

    @classmethod
    def fromVec3(cls, vec):
        return cls(vec.x, vec.y, vec.z)

    @classmethod
    def fromVec4(cls, vec):
        return cls(vec.x, vec.y, vec.z)




class vec4(object):
    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __getitem__(self, key):
        if type(key) is int:
            if key is 0:
                return self.x
            elif key is 1:
                return self.y
            elif key is 2:
                return self.z
            elif key is 3:
                return self.w
            else:
                raise IndexError("Index out of bounds.")    
        else:
            raise TypeError("Invalid type.")

    def __setitem__(self, key, val):
        if type(key) is int:
            if key is 0:
                self.x = val
            elif key is 1:
                self.y = val
            elif key is 2:
                self.z = val
            elif key is 3:
                self.w = val
            else:
                raise IndexError("Index out of bounds.")    
        else:
            raise TypeError("Invalid type.")

    def __iter__(self):
        return iter([self.x, self.y, self.z, self.w])

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            y = self.y + other
            z = self.z + other
            w = self.w + other
            return vec4(x, y, z, w)
        elif isinstance(other, vec4):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            w = self.w + other.w
            return vec4(x, y, z, w)
        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __iadd__(self, other):
        self = self + other
        return self

    def __radd__(self, other):
        self = self + other
        return self
        
    def __sub__(self, other):
        return self.__add__(-other)

    def __isub__(self, other):
        self = self - other
        return self

    def __rsub__(self, other):
        self = self - other
        return self

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            x = self.x * other
            y = self.y * other
            z = self.z * other
            w = self.w * other
            return vec4(x, y, z, w)
        elif isinstance(other, vec4):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            w = self.w * other.w
            return vec4(x, y, z, w)
        elif isinstance(other, glmatrix.mat4):
            a = other[0][0] * self[0] + other[1][0] * self[1] + other[2][0] * self[2] + other[3][0] * self[3]
            b = other[0][1] * self[0] + other[1][1] * self[1] + other[2][1] * self[2] + other[3][1] * self[3]
            c = other[0][2] * self[0] + other[1][2] * self[1] + other[2][2] * self[2] + other[3][2] * self[3]
            d = other[0][3] * self[0] + other[1][3] * self[1] + other[2][3] * self[2] + other[3][3] * self[3]
            return vec4(a, b, c, d)
        
        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __imul__(self, other):
        self = self * other
        return self

    def __rmul__(self, other):
        self = self * other
        return self

    def __truediv__(self, other):   
        if isinstance(other, int) or isinstance(other, float):
            x = self.x / other
            y = self.y / other
            z = self.z / other
            w = self.w / other
            return vec4(x, y, z, w)

        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __itruediv__(self, other):
        self = self / other
        return self

    def __rtruediv__(self, other):
        self = self / other
        return self

    def __floordiv__(self, other):   
        if isinstance(other, int):
            x = self.x // other
            y = self.y // other
            z = self.z // other
            w = self.w // other
            return vec4(x, y, z, w)

        raise TypeError("Unknown type for right hand argument: {}".format(type(other)))

    def __ifloordiv__(self, other):
        self = self / other
        return self

    def __rfloordiv__(self, other):
        self = self / other
        return self

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w)

    def __lt__(self, other):
        return (self.x < other.x or (self.x == other .x and self.y < other.y) or (self.x == other.x and self.y == other.y and self.z < other.z) or (self.w == other.w and self.y == other.y and self.z == other.z and self.w < other.w))

    def __gt__(self, other):
        return (self.x > other.x or (self.x == other .x and self.y > other.y) or (self.x == other.x and self.y == other.y and self.z > other.z) or (self.w == other.w and self.y == other.y and self.z == other.z and self.w > other.w))

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __pos__(self):
        x = +self.x
        y = +self.y
        z = +self.z
        w = +self.w
        return vec4(x, y, z, w)

    def __neg__(self):
        x = -self.x
        y = -self.y
        z = -self.z
        w = -self.w
        return vec4(x, y, z, w)

    def __abs__(self):
        x = abs(self.x)
        y = abs(self.y)
        z = abs(self.z)
        w = abs(self.w)
        return vec4(x, y, z, w)

    def __round__(self, n=0):
        x = round(self.x, n)
        y = round(self.y, n)
        z = round(self.z, n)
        w = round(self.w, n)
        return vec4(x, y, z, w)

    def __floor__(self):
        x = math.floor(self.x)
        y = math.floor(self.y)
        z = math.floor(self.z)
        w = math.floor(self.w)
        return vec4(x, y, z, w)

    def __ceil__(self):
        x = math.ceil(self.x)
        y = math.ceil(self.y)
        z = math.ceil(self.z)
        w = math.ceil(self.w)
        return vec4(x, y, z, w)

    def __trunc__(self):
        x = math.trunc(self.x)
        y = math.trunc(self.y)
        z = math.trunc(self.z)
        w = math.trunc(self.w)
        return vec4(x, y, z, w)

    def __str__(self):
        return "(" + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + "," + str(self.z) + ")"

    def __repr__(self):
        return "vec4(" + str(self.x) + "," + str(self.y)    + "," + str(self.z) + "," + str(self.w) + ")"

    def __len__(self):
        return 4

    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)

    @property
    def unit(self):
        return self / self.length

    @classmethod
    def fromVec2(cls, vec, z=0, w=0):
        return cls(vec.x, vec.y, z, w)

    @classmethod
    def fromVec3(cls, vec, w=0):
        return cls(vec.x, vec.y, vec.z, w)

    @classmethod
    def fromVec4(cls, vec):
        return cls(vec.x, vec.y, vec.z, vec.w)


def dot(u, v):
    try:
        if isinstance(u, type(v)) or isinstance(v, type(u)) :
            if isinstance(u, vec2):
                return u.x * v.x + u.y * v.y

            elif isinstance(u, vec3):
                return u.x * v.x + u.y * v.y + u.z * v.z

            elif isinstance(u, vec4):
                return u.x * v.x + u.y * v.y + u.z * v.z + u.w * v.w
        else:
            raise TypeError("Parameters must be vecs of the same type.")
    except TypeError as err:
        print("Type Error: " + err)

def cross(u, v):
    try:
        if isinstance(u, type(v)) or isinstance(v, type(u))  and isinstance(u, vec3):
            x = u.y * v.z - u.z * v.y
            y = u.z * v.x - u.x * v.z
            z = u.x * v.y - u.y * v.x
            return vec3(x, y, z)
        else:
            raise TypeError("Parameters must be 3D vecs.")
    except TypeError as err:
        print("Type Error: " + err)


def distance(u, v):
    try:
        if isinstance(u, type(v)) or isinstance(v, type(u)) :
            if isinstance(u, vec2) or isinstance(u, vec3) or isinstance(u, vec4):
                res = v - u
                return res.length
        else:
            raise TypeError("Parameters must be vecs of the same type.")
    except TypeError as err:
        print("Type Error: " + err)

def length(u):
    try:
        if isinstance(u, vec2) or isinstance(u, vec3) or isinstance(u, vec4):
            return u.length
        else:
            raise TypeError("Parameter must be a vector.")
    except TypeError as err:
        print("Type Error: " + err)

def normalize(u):
    try:
        if isinstance(u, vec2) or isinstance(u, vec3) or isinstance(u, vec4):
            return u.unit
        else:
            raise TypeError("Parameter must be a vector.")
    except TypeError as err:
        print("Type Error: " + err)

###################################################
## Geometric operations
###################################################

def faceforward(N, I, Nref):
    return N if dot(Nref, I) < 0.0 else -N

def reflect(I, N):
    return I - N * dot(N, I) * 2.0

def refract(I, N, eta):
    dotValue = dot(N, I)
    k = 1 - eta * eta * (1 - dotValue ** 2)
    return (eta * I - (eta * dotValue + math.sqrt(k)) * N) * (1.0 if k >= 0.0 else 0.0)

###################################################
