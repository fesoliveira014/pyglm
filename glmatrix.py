import math
from glvector import *

class mat2(object):
    def __init__(self, a=0, b=0, c=0, d=0):
        self.cols = [vec2(a,b), vec2(c,d)]
        
    def __getitem__(self, key):
        if type(key) is int:
            return self.cols[key]
        else:
            raise TypeError("Invalid type.")

    def __setitem__(self, key, val):
        if type(key) is int:
            self.cols[key] = val
        else:
            raise TypeError("Invalid type.")

    def __iter__(self):
        return iter(self.cols)

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] + other
            b = self[0][1] + other
            c = self[1][0] + other
            d = self[1][1] + other
            return mat2(a,b,c,d)
        elif type(other) is mat2:
            a = self[0][0] + other[0][0]
            b = self[0][1] + other[0][1]
            c = self[1][0] + other[1][0]
            d = self[1][1] + other[1][1]
            print("a = {0}, b = {1}, c = {2}, d={3}".format(a,b,c,d))
            return mat2(a,b,c,d)
        else:
            raise TypeError("Invalid type.")

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] - other
            b = self[0][1] - other
            c = self[1][0] - other
            d = self[1][1] - other
            return mat2(a,b,c,d)
        elif type(other) is mat2:
            a = self[0][0] - other[0][0]
            b = self[0][1] - other[0][1]
            c = self[1][0] - other[1][0]
            d = self[1][1] - other[1][1]
            return mat2(a,b,c,d)
        else:
            raise TypeError("Invalid type.")        

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] * other
            b = self[0][1] * other
            c = self[1][0] * other
            d = self[1][1] * other
            return mat2(a,b,c,d)
        elif type(other) is mat2:
            a = self[0][0] * other[0][0] + self[0][1] * other[1][0]
            b = self[0][0] * other[0][1] + self[0][1] * other[1][1]
            c = self[1][0] * other[0][0] + self[1][1] * other[1][0]
            d = self[1][0] * other[0][1] + self[1][1] * other[1][1]
            return mat2(a,b,c,d)
        elif type(other) is vec2:
            a = self[0][0] * other[0] + self[0][1] * other[1]
            b = self[1][0] * other[0] + self[1][1] * other[1]
            return vec2(a,b)
        else:
            raise TypeError("Invalid type.")

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] / other
            b = self[0][1] / other
            c = self[1][0] / other
            d = self[1][1] / other
            return mat2(a,b,c,d)
        elif type(other) is mat2:
            return self * mat2._inverse(other)
        else:
            raise TypeError("Invalid type.")

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __imul__(self, other):
        self = self * other
        return self

    def __itruediv__(self, other):
        self = self / other
        return self

    def __eq__(self, other):
        return (self[0] == other[0] and self[1] == other[1])

    def __ne__(self, other):
        return not self == other

    def __pos__(self):
        a = +self[0][0]
        b = +self[0][1]
        c = +self[1][0]
        d = +self[1][1]
        return mat2(a,b,c,d)

    def __neg__(self):
        a = -self[0][0]
        b = -self[0][1]
        c = -self[1][0]
        d = -self[1][1]
        return mat2(a,b,c,d)

    def __abs__(self):
        a = abs(self[0][0])
        b = abs(self[0][1])
        c = abs(self[1][0])
        d = abs(self[1][1])
        return mat2(a,b,c,d)

    def __round__(self, n=0):
        a = round(self[0][0], n)
        b = round(self[0][1], n)
        c = round(self[1][0], n)
        d = round(self[1][1], n)
        return mat2(a,b,c,d)

    def __floor__(self):
        a = math.floor(self[0][0])
        b = math.floor(self[0][1])
        c = math.floor(self[1][0])
        d = math.floor(self[1][1])
        return mat2(a,b,c,d)

    def __ceil__(self):
        a = math.ceil(self[0][0])
        b = math.ceil(self[0][1])
        c = math.ceil(self[1][0])
        d = math.ceil(self[1][1])
        return mat2(a,b,c,d)

    def __trunc__(self):
        a = math.trunc(self[0][0])
        b = math.trunc(self[0][1])
        c = math.trunc(self[1][0])
        d = math.trunc(self[1][1])
        return mat2(a,b,c,d)

    def __str__(self):
        return "([" + str(self[0][0]) + ', ' + str(self[0][1]) + "]," + \
                "[" + str(self[1][0]) + ', ' + str(self[1][1]) + "]"

    def __repr__(self):
        return "mat2(" + str(self[0][0]) + ', ' + str(self[0][1]) + ', ' + \
                         str(self[1][0]) + ', ' + str(self[1][1]) + ")"

    @classmethod
    def fromVec2(cls, vec1, vec2):
        a = vec1[0]
        b = vec1[1]
        c = vec2[0]
        d = vec2[1]
        return cls(a,b,c,d)
    
    @classmethod
    def _inverse(cls, matrix):
        if type(matrix) is not mat2:
            raise TypeError("Parameter must be of type " + str(mat2))

        determinant = mat2._determinant(matrix)
        if determinant is not 0:
            oneOverDeterminant = 1 / determinant
            a = + matrix[1][1] * oneOverDeterminant
            b = - matrix[0][1] * oneOverDeterminant
            c = - matrix[1][0] * oneOverDeterminant
            d = + matrix[0][0] * oneOverDeterminant
            return cls(a,b,c,d)
        else:
            raise ArithmeticError("Can't invert a matrix which determinant is zero.")

    @classmethod
    def _transpose(cls, matrix):
        if type(matrix) is not mat2:
            raise TypeError("Parameter must be of type " + str(mat2))

        a = matrix[0][0]
        b = matrix[1][0]
        c = matrix[0][1]
        d = matrix[1][1]
        return cls(a,b,c,d)

    @staticmethod
    def _determinant(matrix):
        if type(matrix) is not mat2:
            raise TypeError("Parameter must be of type " + str(mat2))

        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]



class mat3(object):
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0, i=0):
        self.cols = [vec3(a,b,c), vec3(d,e,f), vec3(g,h,i)]
        
    def __getitem__(self, key):
        if type(key) is int:
            return self.cols[key]
        else:
            raise TypeError("Invalid type.")

    def __setitem__(self, key, val):
        if type(key) is int:
            self.cols[key] = val
        else:
            raise TypeError("Invalid type.")

    def __iter__(self):
        return iter(self.cols)

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] + other
            b = self[0][1] + other
            c = self[0][2] + other
            d = self[1][0] + other
            e = self[1][1] + other
            f = self[1][2] + other
            g = self[2][0] + other
            h = self[2][1] + other
            i = self[2][2] + other
            return mat3(a,b,c,d,e,f,g,h,i)
        elif type(other) is mat3:
            a = self[0][0] + other[0][0]
            b = self[0][1] + other[0][1]
            c = self[0][2] + other[0][2]
            d = self[1][0] + other[1][0]
            e = self[1][1] + other[1][1]
            f = self[1][2] + other[1][2]
            g = self[2][0] + other[2][0]
            h = self[2][1] + other[2][1]
            i = self[2][2] + other[2][2]
            return mat3(a,b,c,d,e,f,g,h,i)
        else:
            raise TypeError("Invalid type.")

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] - other
            b = self[0][1] - other
            c = self[0][2] - other
            d = self[1][0] - other
            e = self[1][1] - other
            f = self[1][2] - other
            g = self[2][0] - other
            h = self[2][1] - other
            i = self[2][2] - other
            return mat3(a,b,c,d,e,f,g,h,i)
        elif type(other) is mat3:
            a = self[0][0] - other[0][0]
            b = self[0][1] - other[0][1]
            c = self[0][2] - other[0][2]
            d = self[1][0] - other[1][0]
            e = self[1][1] - other[1][1]
            f = self[1][2] - other[1][2]
            g = self[2][0] - other[2][0]
            h = self[2][1] - other[2][1]
            i = self[2][2] - other[2][2]
            return mat3(a,b,c,d,e,f,g,h,i)
        else:
            raise TypeError("Invalid type.")        

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] * other
            b = self[0][1] * other
            c = self[0][2] * other
            d = self[1][0] * other
            e = self[1][1] * other
            f = self[1][2] * other
            g = self[2][0] * other
            h = self[2][1] * other
            i = self[2][2] * other
            return mat3(a,b,c,d,e,f,g,h,i)
        elif type(other) is mat3:
            a = self[0][0] * other[0][0] + self[0][1] * other[1][0] + self[0][2] * other[2][0]
            b = self[0][0] * other[0][1] + self[0][1] * other[1][1] + self[0][2] * other[2][1]
            c = self[0][0] * other[0][2] + self[0][1] * other[1][2] + self[0][2] * other[2][2]
            d = self[1][0] * other[0][0] + self[1][1] * other[1][0] + self[1][2] * other[2][0]
            e = self[1][0] * other[0][1] + self[1][1] * other[1][1] + self[1][2] * other[2][1]
            f = self[1][0] * other[0][2] + self[1][1] * other[1][2] + self[1][2] * other[2][2]
            g = self[2][0] * other[0][0] + self[2][1] * other[1][0] + self[2][2] * other[2][0]
            h = self[2][0] * other[0][1] + self[2][1] * other[1][1] + self[2][2] * other[2][1]
            i = self[2][0] * other[0][2] + self[2][1] * other[1][2] + self[2][2] * other[2][2]
            return mat3(a,b,c,d,e,f,g,h,i)
        elif type(other) is vec3:
            a = self[0][0] * other[0] + self[0][1] * other[1] + self[0][2] * other[2]
            b = self[1][0] * other[0] + self[1][1] * other[1] + self[1][2] * other[2]
            c = self[2][0] * other[0] + self[2][1] * other[1] + self[2][2] * other[2]
            return vec3(a,b,c)
        else:
            raise TypeError("Invalid type.")

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] / other
            b = self[0][1] / other
            c = self[0][2] / other
            d = self[1][0] / other
            e = self[1][1] / other
            f = self[1][2] / other
            g = self[2][0] / other
            h = self[2][1] / other
            i = self[2][2] / other
            return mat3(a,b,c,d,e,f,g,h,i)
        elif type(other) is mat3:
            return round(self * mat3._inverse(other))
        else:
            raise TypeError("Invalid type.")

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __imul__(self, other):
        self = self * other
        return self

    def __itruediv__(self, other):
        self = self / other
        return self

    def __eq__(self, other):
        return (self[0] == other[0] and self[1] == other[1] and self[2] == other[2])

    def __ne__(self, other):
        return not self == other

    def __pos__(self):
        a = +self[0][0]
        b = +self[0][1]
        c = +self[0][2]
        d = +self[1][0]
        e = +self[1][1]
        f = +self[1][2]
        g = +self[2][0]
        h = +self[2][1]
        i = +self[2][2]
        return mat3(a,b,c,d,e,f,g,h,i)

    def __neg__(self):
        a = -self[0][0]
        b = -self[0][1]
        c = -self[0][2]
        d = -self[1][0]
        e = -self[1][1]
        f = -self[1][2]
        g = -self[2][0]
        h = -self[2][1]
        i = -self[2][2]
        return mat3(a,b,c,d,e,f,g,h,i)

    def __abs__(self):
        a = abs(self[0][0])
        b = abs(self[0][1])
        c = abs(self[0][2])
        d = abs(self[1][0])
        e = abs(self[1][1])
        f = abs(self[1][2])
        g = abs(self[2][0])
        h = abs(self[2][1])
        i = abs(self[2][2])
        return mat3(a,b,c,d,e,f,g,h,i)

    def __round__(self, n=0):
        a = round(self[0][0], n)
        b = round(self[0][1], n)
        c = round(self[0][2], n)
        d = round(self[1][0], n)
        e = round(self[1][1], n)
        f = round(self[1][2], n)
        g = round(self[2][0], n)
        h = round(self[2][1], n)
        i = round(self[2][2], n)
        return mat3(a,b,c,d,e,f,g,h,i)

    def __floor__(self):
        a = math.floor(self[0][0])
        b = math.floor(self[0][1])
        c = math.floor(self[0][2])
        d = math.floor(self[1][0])
        e = math.floor(self[1][1])
        f = math.floor(self[1][2])
        g = math.floor(self[2][0])
        h = math.floor(self[2][1])
        i = math.floor(self[2][2])
        return mat3(a,b,c,d,e,f,g,h,i)

    def __ceil__(self):
        a = math.ceil(self[0][0])
        b = math.ceil(self[0][1])
        c = math.ceil(self[0][2])
        d = math.ceil(self[1][0])
        e = math.ceil(self[1][1])
        f = math.ceil(self[1][2])
        g = math.ceil(self[2][0])
        h = math.ceil(self[2][1])
        i = math.ceil(self[2][2])
        return mat3(a,b,c,d,e,f,g,h,i)

    def __trunc__(self):
        a = math.trunc(self[0][0])
        b = math.trunc(self[0][1])
        c = math.trunc(self[0][2])
        d = math.trunc(self[1][0])
        e = math.trunc(self[1][1])
        f = math.trunc(self[1][2])
        g = math.trunc(self[2][0])
        h = math.trunc(self[2][1])
        i = math.trunc(self[2][2])
        return mat3(a,b,c,d,e,f,g,h,i)

    @classmethod
    def fromVec3(cls, u, v, w):
        a = u[0]
        b = u[1]
        c = u[2]
        d = v[0]
        e = v[1]
        f = v[2]
        g = w[0]
        h = w[1]
        i = w[2]
        return cls(a,b,c,d,e,f,g,h,i)

    @classmethod
    def fromMat2(cls, m):
        a = m[0][0]
        b = m[0][1]
        c = 0
        d = [1][0]
        e = [1][1]
        f = 0
        g = 0
        i = 0
        h = 1
        return cls(a,b,c,d,e,f,g,h,i)

    @classmethod
    def fromMat3(cls, m):
        a = m[0][0]
        b = m[0][1]
        c = m[0][2]
        d = m[1][0]
        e = m[1][1]
        f = m[1][2]
        g = m[2][0]
        h = m[2][1]
        i = m[2][2]
        return cls(a,b,c,d,e,f,g,h,i)

    def __str__(self):
        return "([" + str(self[0]) + ', ' + str(self[1]) + ', ' + str(self[2]) + "])"

    def __repr__(self):
        return "mat3(" + str(self[0]) + ', ' + str(self[1]) + ', ' + str(self[2]) + ")"

    @classmethod
    def zero(cls):
        return cls();

    @classmethod
    def identity(cls):
        return cls(a=1, e=1, i=1)

    
    @classmethod
    def _inverse(cls, matrix):
        if type(matrix) is not mat3:
            raise TypeError("Parameter must be of type " + str(mat3))

        determinant = mat3._determinant(matrix)

        if determinant is not 0:
            oneOverDeterminant = 1 / determinant

            a = + (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) * oneOverDeterminant;
            d = - (matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2]) * oneOverDeterminant;
            g = + (matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]) * oneOverDeterminant;
            b = - (matrix[0][1] * matrix[2][2] - matrix[2][1] * matrix[0][2]) * oneOverDeterminant;
            e = + (matrix[0][0] * matrix[2][2] - matrix[2][0] * matrix[0][2]) * oneOverDeterminant;
            h = - (matrix[0][0] * matrix[2][1] - matrix[2][0] * matrix[0][1]) * oneOverDeterminant;
            c = + (matrix[0][1] * matrix[1][2] - matrix[1][1] * matrix[0][2]) * oneOverDeterminant;
            f = - (matrix[0][0] * matrix[1][2] - matrix[1][0] * matrix[0][2]) * oneOverDeterminant;
            i = + (matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]) * oneOverDeterminant;

            return cls(a,b,c,d,e,f,g,h,i)
        else:
            raise ArithmeticError("Can't invert a matrix which determinant is zero.")

    @classmethod
    def _transpose(cls, matrix):
        if type(matrix) is not mat3:
            raise TypeError("Parameter must be of type " + str(mat3))

        a = matrix[0][0]
        d = matrix[0][1]
        g = matrix[0][2]
        b = matrix[1][0]
        e = matrix[1][1]
        h = matrix[1][2]
        c = matrix[2][0]
        f = matrix[2][1]
        i = matrix[2][2]
        return cls(a,b,c,d,e,f,g,h,i)

    @staticmethod
    def _determinant(matrix):
        if type(matrix) is not mat3:
            raise TypeError("Parameter must be of type " + str(mat3))

        return (matrix[0][0] * matrix[1][1] * matrix[2][2] + 
                matrix[0][1] * matrix[1][2] * matrix[2][0] +
                matrix[0][2] * matrix[1][0] * matrix[2][1] - 
                matrix[0][2] * matrix[1][1] * matrix[2][0] -
                matrix[0][1] * matrix[1][0] * matrix[2][2] -
                matrix[0][0] * matrix[1][2] * matrix[2][1])




class mat4(object):
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0, i=0, j=0, k=0, l=0, m=0, n=0, o=0, p=0):
        self.cols = [vec4(a,b,c,d), vec4(e,f,g,h), vec4(i,j,k,l), vec4(m,n,o,p)]
        
    def __getitem__(self, key):
        if type(key) is int:
            return self.cols[key]
        else:
            raise TypeError("Invalid type.")

    def __setitem__(self, key, val):
        if type(key) is int:
            self.cols[key] = val
        else:
            raise TypeError("Invalid type.")

    def __iter__(self):
        return iter(self.cols)

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] + other
            b = self[0][1] + other
            c = self[0][2] + other
            d = self[0][3] + other
            e = self[1][0] + other
            f = self[1][1] + other
            g = self[1][2] + other
            h = self[1][3] + other
            i = self[2][0] + other
            j = self[2][1] + other
            k = self[2][2] + other
            l = self[2][3] + other
            m = self[3][0] + other
            n = self[3][1] + other
            o = self[3][2] + other
            p = self[3][3] + other
            return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
        elif type(other) is mat4:
            a = self[0][0] + other[0][0]
            b = self[0][1] + other[0][1]
            c = self[0][2] + other[0][2]
            d = self[0][3] + other[1][0]
            e = self[1][0] + other[1][1]
            f = self[1][1] + other[1][2]
            g = self[1][2] + other[2][0]
            h = self[1][3] + other[2][1]
            i = self[2][0] + other[2][2]
            j = self[2][1] + other[2][1]
            k = self[2][2] + other[2][2]
            l = self[2][3] + other[2][3]
            m = self[3][0] + other[3][0]
            n = self[3][1] + other[3][1]
            o = self[3][2] + other[3][2]
            p = self[3][3] + other[3][3]
            return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
        else:
            raise TypeError("Invalid type.")

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] - other
            b = self[0][1] - other
            c = self[0][2] - other
            d = self[0][3] - other
            e = self[1][0] - other
            f = self[1][1] - other
            g = self[1][2] - other
            h = self[1][3] - other
            i = self[2][0] - other
            j = self[2][1] - other
            k = self[2][2] - other
            l = self[2][3] - other
            m = self[3][0] - other
            n = self[3][1] - other
            o = self[3][2] - other
            p = self[3][3] - other
            return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
        elif type(other) is mat4:
            a = self[0][0] - other[0][0]
            b = self[0][1] - other[0][1]
            c = self[0][2] - other[0][2]
            d = self[0][3] - other[1][0]
            e = self[1][0] - other[1][1]
            f = self[1][1] - other[1][2]
            g = self[1][2] - other[2][0]
            h = self[1][3] - other[2][1]
            i = self[2][0] - other[2][2]
            j = self[2][1] - other[2][1]
            k = self[2][2] - other[2][2]
            l = self[2][3] - other[2][3]
            m = self[3][0] - other[3][0]
            n = self[3][1] - other[3][1]
            o = self[3][2] - other[3][2]
            p = self[3][3] - other[3][3]
            return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
        else:
            raise TypeError("Invalid type.")        

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] * other
            b = self[0][1] * other
            c = self[0][2] * other
            d = self[0][3] * other
            e = self[1][0] * other
            f = self[1][1] * other
            g = self[1][2] * other
            h = self[1][3] * other
            i = self[2][0] * other
            j = self[2][1] * other
            k = self[2][2] * other
            l = self[2][3] * other
            m = self[3][0] * other
            n = self[3][1] * other
            o = self[3][2] * other
            p = self[3][3] * other
            return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
        elif type(other) is mat4:
            a = self[0][0] * other[0][0] + self[0][1] * other[1][0] + self[0][2] * other[2][0] + self[0][3] * other[3][0]
            b = self[0][0] * other[0][1] + self[0][1] * other[1][1] + self[0][2] * other[2][1] + self[0][3] * other[3][1]
            c = self[0][0] * other[0][2] + self[0][1] * other[1][2] + self[0][2] * other[2][2] + self[0][3] * other[3][2]
            d = self[0][0] * other[0][3] + self[0][1] * other[1][3] + self[0][2] * other[2][3] + self[0][3] * other[3][3]
            e = self[1][0] * other[0][0] + self[1][1] * other[1][0] + self[1][2] * other[2][0] + self[1][3] * other[3][0]
            f = self[1][0] * other[0][1] + self[1][1] * other[1][1] + self[1][2] * other[2][1] + self[1][3] * other[3][1]
            g = self[1][0] * other[0][2] + self[1][1] * other[1][2] + self[1][2] * other[2][2] + self[1][3] * other[3][2]
            h = self[1][0] * other[0][3] + self[1][1] * other[1][3] + self[1][2] * other[2][3] + self[1][3] * other[3][3]
            i = self[2][0] * other[0][0] + self[2][1] * other[1][0] + self[2][2] * other[2][0] + self[2][3] * other[3][0]
            j = self[2][0] * other[0][1] + self[2][1] * other[1][1] + self[2][2] * other[2][1] + self[2][3] * other[3][1]
            k = self[2][0] * other[0][2] + self[2][1] * other[1][2] + self[2][2] * other[2][2] + self[2][3] * other[3][2]
            l = self[2][0] * other[0][3] + self[2][1] * other[1][3] + self[2][2] * other[2][3] + self[2][3] * other[3][3]
            m = self[3][0] * other[0][0] + self[3][1] * other[1][0] + self[3][2] * other[2][0] + self[3][3] * other[3][0]
            n = self[3][0] * other[0][1] + self[3][1] * other[1][1] + self[3][2] * other[2][1] + self[3][3] * other[3][1]
            o = self[3][0] * other[0][2] + self[3][1] * other[1][2] + self[3][2] * other[2][2] + self[3][3] * other[3][2]
            p = self[3][0] * other[0][3] + self[3][1] * other[1][3] + self[3][2] * other[2][3] + self[3][3] * other[3][3]
            return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
        elif type(other) is vec4:
            a = self[0][0] * other[0] + self[0][1] * other[1] + self[0][2] * other[2] + self[0][3] * other[3]
            b = self[1][0] * other[0] + self[1][1] * other[1] + self[1][2] * other[2] + self[1][3] * other[3]
            c = self[2][0] * other[0] + self[2][1] * other[1] + self[2][2] * other[2] + self[2][3] * other[3]
            d = self[3][0] * other[0] + self[3][1] * other[1] + self[3][2] * other[2] + self[3][3] * other[3]
            return vec3(a,b,c)
        else:
            raise TypeError("Invalid type.")

    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            a = self[0][0] / other
            b = self[0][1] / other
            c = self[0][2] / other
            d = self[0][3] / other
            e = self[1][0] / other
            f = self[1][1] / other
            g = self[1][2] / other
            h = self[1][3] / other
            i = self[2][0] / other
            j = self[2][1] / other
            k = self[2][2] / other
            l = self[2][3] / other
            m = self[3][0] / other
            n = self[3][1] / other
            o = self[3][2] / other
            p = self[3][3] / other
            return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
        elif type(other) is mat4:
            return self * mat4._inverse(other)
        else:
            raise TypeError("Invalid type.")

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __imul__(self, other):
        self = self * other
        return self

    def __itruediv__(self, other):
        self = self / other
        return self

    def __eq__(self, other):
        return (self[0] == other[0] and self[1] == other[1] and self[2] == other[2])

    def __ne__(self, other):
        return not self == other

    def __pos__(self):
        a = +self[0][0]
        b = +self[0][1]
        c = +self[0][2]
        d = +self[0][3]
        e = +self[1][0]
        f = +self[1][1]
        g = +self[1][2]
        h = +self[1][3]
        i = +self[2][0]
        j = +self[2][1]
        k = +self[2][2]
        l = +self[2][3]
        m = +self[3][0]
        n = +self[3][1]
        o = +self[3][2]
        p = +self[3][3]
        return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    def __neg__(self):
        a = -self[0][0]
        b = -self[0][1]
        c = -self[0][2]
        d = -self[0][3]
        e = -self[1][0]
        f = -self[1][1]
        g = -self[1][2]
        h = -self[1][3]
        i = -self[2][0]
        j = -self[2][1]
        k = -self[2][2]
        l = -self[2][3]
        m = -self[3][0]
        n = -self[3][1]
        o = -self[3][2]
        p = -self[3][3]
        return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    def __abs__(self):
        a = abs(self[0][0])
        b = abs(self[0][1])
        c = abs(self[0][2])
        d = abs(self[0][3])
        e = abs(self[1][0])
        f = abs(self[1][1])
        g = abs(self[1][2])
        h = abs(self[1][3])
        i = abs(self[2][0])
        j = abs(self[2][1])
        k = abs(self[2][2])
        l = abs(self[2][3])
        m = abs(self[3][0])
        n = abs(self[3][1])
        o = abs(self[3][2])
        p = abs(self[3][3])
        return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    def __round__(self, n=0):
        a = abs(self[0][0], n)
        b = abs(self[0][1], n)
        c = abs(self[0][2], n)
        d = abs(self[0][3], n)
        e = abs(self[1][0], n)
        f = abs(self[1][1], n)
        g = abs(self[1][2], n)
        h = abs(self[1][3], n)
        i = abs(self[2][0], n)
        j = abs(self[2][1], n)
        k = abs(self[2][2], n)
        l = abs(self[2][3], n)
        m = abs(self[3][0], n)
        n = abs(self[3][1], n)
        o = abs(self[3][2], n)
        p = abs(self[3][3], n)
        return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    def __floor__(self):
        a = math.floor(self[0][0])
        b = math.floor(self[0][1])
        c = math.floor(self[0][2])
        d = math.floor(self[0][3])
        e = math.floor(self[1][0])
        f = math.floor(self[1][1])
        g = math.floor(self[1][2])
        h = math.floor(self[1][3])
        i = math.floor(self[2][0])
        j = math.floor(self[2][1])
        k = math.floor(self[2][2])
        l = math.floor(self[2][3])
        m = math.floor(self[3][0])
        n = math.floor(self[3][1])
        o = math.floor(self[3][2])
        p = math.floor(self[3][3])
        return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    def __ceil__(self):
        a = math.ceil(self[0][0])
        b = math.ceil(self[0][1])
        c = math.ceil(self[0][2])
        d = math.ceil(self[0][3])
        e = math.ceil(self[1][0])
        f = math.ceil(self[1][1])
        g = math.ceil(self[1][2])
        h = math.ceil(self[1][3])
        i = math.ceil(self[2][0])
        j = math.ceil(self[2][1])
        k = math.ceil(self[2][2])
        l = math.ceil(self[2][3])
        m = math.ceil(self[3][0])
        n = math.ceil(self[3][1])
        o = math.ceil(self[3][2])
        p = math.ceil(self[3][3])
        return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    def __trunc__(self):
        a = math.trunc(self[0][0])
        b = math.trunc(self[0][1])
        c = math.trunc(self[0][2])
        d = math.trunc(self[0][3])
        e = math.trunc(self[1][0])
        f = math.trunc(self[1][1])
        g = math.trunc(self[1][2])
        h = math.trunc(self[1][3])
        i = math.trunc(self[2][0])
        j = math.trunc(self[2][1])
        k = math.trunc(self[2][2])
        l = math.trunc(self[2][3])
        m = math.trunc(self[3][0])
        n = math.trunc(self[3][1])
        o = math.trunc(self[3][2])
        p = math.trunc(self[3][3])
        return mat4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    @classmethod
    def fromVec4(cls, u, v, w, z):
        a = u[0]
        b = u[1]
        c = u[2]
        d = u[3]
        e = v[0]
        f = v[1]
        g = v[2]
        h = v[3]
        i = w[0]
        j = w[1]
        k = w[2]
        l = w[3]
        m = z[0]
        n = z[1]
        o = z[2]
        p = z[3]
        return cls(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    @classmethod
    def fromMat4(cls, matrix):
        a = m[0][0]
        b = m[0][1]
        c = m[0][2]
        d = m[0][3]
        e = m[1][0]
        f = m[1][1]
        g = m[1][2]
        h = m[1][3]
        i = m[2][0]
        j = m[2][1]
        k = m[2][2]
        l = m[2][3]
        m = m[3][0]
        n = m[3][1]
        o = m[3][2]
        p = m[3][3]
        return cls(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)




    def __str__(self):
        return "([" + str(self[0][0]) + ', ' + str(self[0][1]) + ', ' + str(self[0][2]) + ', ' + str(self[0][3]) + "]," + \
                "[" + str(self[1][0]) + ', ' + str(self[1][1]) + ', ' + str(self[1][2]) + ', ' + str(self[1][3]) + "]," + \
                "[" + str(self[2][0]) + ', ' + str(self[2][1]) + ', ' + str(self[2][2]) + ', ' + str(self[2][3]) + "]," + \
                "[" + str(self[3][0]) + ', ' + str(self[3][1]) + ', ' + str(self[3][2]) + ', ' + str(self[3][3]) + "]"

    def __repr__(self):
        return "mat4(" + str(self[0][0]) + ', ' + str(self[0][1]) + ', ' + str(self[0][2]) + ', ' + str(self[0][3]) + ', ' + \
                         str(self[1][0]) + ', ' + str(self[1][1]) + ', ' + str(self[1][2]) + ', ' + str(self[1][3]) + ', ' + \
                         str(self[2][0]) + ', ' + str(self[2][1]) + ', ' + str(self[2][2]) + ', ' + str(self[2][3]) + ', ' + \
                         str(self[3][0]) + ', ' + str(self[3][1]) + ', ' + str(self[3][2]) + ', ' + str(self[3][3]) + ")"

    @classmethod
    def zero(cls):
        return cls();

    @classmethod
    def identity(cls):
        return cls(a=1, f=1, k=1, p=1)

    @classmethod
    def _inverse(cls, matrix):
        coef00 = matrix[2][2] * matrix[3][3] - matrix[3][2] * matrix[2][3]
        coef02 = matrix[1][2] * matrix[3][3] - matrix[3][2] * matrix[1][3]
        coef03 = matrix[1][2] * matrix[2][3] - matrix[2][2] * matrix[1][3]

        coef04 = matrix[2][1] * matrix[3][3] - matrix[3][1] * matrix[2][3]
        coef06 = matrix[1][1] * matrix[3][3] - matrix[3][1] * matrix[1][3]
        coef07 = matrix[1][1] * matrix[2][3] - matrix[2][1] * matrix[1][3]

        coef08 = matrix[2][1] * matrix[3][2] - matrix[3][1] * matrix[2][2]
        coef10 = matrix[1][1] * matrix[3][2] - matrix[3][1] * matrix[1][2]
        coef11 = matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]

        coef12 = matrix[2][0] * matrix[3][3] - matrix[3][0] * matrix[2][3]
        coef14 = matrix[1][0] * matrix[3][3] - matrix[3][0] * matrix[1][3]
        coef15 = matrix[1][0] * matrix[2][3] - matrix[2][0] * matrix[1][3]

        coef16 = matrix[2][0] * matrix[3][2] - matrix[3][0] * matrix[2][2]
        coef18 = matrix[1][0] * matrix[3][2] - matrix[3][0] * matrix[1][2]
        coef19 = matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2]

        coef20 = matrix[2][0] * matrix[3][1] - matrix[3][0] * matrix[2][1]
        coef22 = matrix[1][0] * matrix[3][1] - matrix[3][0] * matrix[1][1]
        coef23 = matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]

        fac0 = vec4(coef00, coef00, coef02, coef03)
        fac1 = vec4(coef04, coef04, coef06, coef07)
        fac2 = vec4(coef08, coef08, coef10, coef11)
        fac3 = vec4(coef12, coef12, coef14, coef15)
        fac4 = vec4(coef16, coef16, coef18, coef19)
        fac5 = vec4(coef20, coef20, coef22, coef23)

        v0 = vec4(matrix[1][0], matrix[0][0], matrix[0][0], matrix[0][0])
        v1 = vec4(matrix[1][1], matrix[0][1], matrix[0][1], matrix[0][1])
        v2 = vec4(matrix[1][2], matrix[0][2], matrix[0][2], matrix[0][2])
        v3 = vec4(matrix[1][3], matrix[0][3], matrix[0][3], matrix[0][3])

        inv0 = vec4.fromVec4(v1 * fac0 - v2 * fac1 + v3 * fac2)

        inv1 = vec4.fromVec4(v0 * fac0 - v2 * fac3 + v3 * fac4)
        inv2 = vec4.fromVec4(v0 * fac1 - v1 * fac3 + v3 * fac5)
        inv3 = vec4.fromVec4(v0 * fac2 - v1 * fac4 + v2 * fac5)

        signA = vec4(+1, -1, +1, -1)
        signB = vec4(-1, +1, -1, +1)
        inverse = mat4.fromVec4(inv0 * signA, inv1 * signB, inv2 * signA, inv3 * signB)

        row0 = vec4(inverse[0][0], inverse[1][0], inverse[2][0], inverse[3][0])

        d0 = vec4.fromVec4(matrix[0] * row0)
        d1 = (d0.x + d0.y) + (d0.z + d0.w)

        if d1 != 0:
            oneOverDeterminant = 1 / d1
            return inverse * oneOverDeterminant
        else:
            raise ArithmeticError("Can't invert a matrix which determinant is zero.")

    @classmethod
    def _transpose(cls, matrix):
        if type(matrix) is not mat4:
            raise TypeError("Parameter must be of type " + str(mat4))

        a = matrix[0][0]
        b = matrix[1][0]
        c = matrix[2][0]
        d = matrix[3][0]
        e = matrix[0][1]
        f = matrix[1][1]
        g = matrix[2][1]
        h = matrix[3][1]
        i = matrix[0][2]
        j = matrix[1][2]
        k = matrix[2][2]
        l = matrix[3][2]
        m = matrix[0][3]
        n = matrix[1][3]
        o = matrix[2][3]
        p = matrix[3][3]
        return cls(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

    @staticmethod
    def _determinant(matrix):
        if type(matrix) is not mat4:
            raise TypeError("Parameter must be of type " + str(mat4))

        subFactor00 = matrix[2][2] * matrix[3][3] - matrix[3][2] * matrix[2][3]
        subFactor01 = matrix[2][1] * matrix[3][3] - matrix[3][1] * matrix[2][3]
        subFactor02 = matrix[2][1] * matrix[3][2] - matrix[3][1] * matrix[2][2]
        subFactor03 = matrix[2][0] * matrix[3][3] - matrix[3][0] * matrix[2][3]
        subFactor04 = matrix[2][0] * matrix[3][2] - matrix[3][0] * matrix[2][2]
        subFactor05 = matrix[2][0] * matrix[3][1] - matrix[3][0] * matrix[2][1]

        detCof = vec4(
            + (matrix[1][1] * subFactor00 - matrix[1][2] * subFactor01 + matrix[1][3] * subFactor02),
            - (matrix[1][0] * subFactor00 - matrix[1][2] * subFactor03 + matrix[1][3] * subFactor04),
            + (matrix[1][0] * subFactor01 - matrix[1][1] * subFactor03 + matrix[1][3] * subFactor05),
            - (matrix[1][0] * subFactor02 - matrix[1][1] * subFactor04 + matrix[1][2] * subFactor05))

        return matrix[0][0] * detCof[0] + matrix[0][1] * detCof[1] + \
               matrix[0][2] * detCof[2] + matrix[0][3] * detCof[3]




def inverse(matrix):
    if   type(matrix) is mat2: return mat2._inverse(matrix)
    elif type(matrix) is mat3: return mat3._inverse(matrix)
    elif type(matrix) is mat4: return mat4._inverse(matrix)
    else: raise TypeError("Argument must be a matrix.")

def transpose(matrix):
    if   type(matrix) is mat2: return mat2._transpose(matrix)
    elif type(matrix) is mat3: return mat3._transpose(matrix)
    elif type(matrix) is mat4: return mat4._transpose(matrix)
    else: raise TypeError("Argument must be a matrix.")

def determinant(matrix):
    if   type(matrix) is mat2: return mat2._determinant(matrix)
    elif type(matrix) is mat3: return mat3._determinant(matrix)
    elif type(matrix) is mat4: return mat4._determinant(matrix)
    else: raise TypeError("Argument must be a matrix.")


