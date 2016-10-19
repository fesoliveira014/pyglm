import unittest
from glvector import *
import math

class TestVec2(unittest.TestCase):
	def test_getter_setter(self):
		u = vec2()
		u[0] = 1
		self.assertEqual(u[0], 1)

	def test_add(self):
		u = vec2(1,2)
		v = vec2(-4,5)
		self.assertEqual(u+v, vec2(-3,7))

	def test_iadd(self):
		u = vec2(1,2)
		u += u
		self.assertEqual(u, vec2(2,4))		

	def test_mul_scalar(self):
		u = vec2(2,3)
		self.assertEqual(u*2, vec2(4,6))

	def test_mul_vec3(self):
		u = vec2(2,3)
		v = vec2(3,4)
		self.assertEqual(u*v, vec2(6,12))

	def test_mul_mat3(self):
		u = vec2(2,3)
		A = mat2(1,2,3,4)
		self.assertEqual(u*A, vec2(11,16))

	def test_truediv(self):
		u = vec2(2,3)
		self.assertEqual(u/2, vec2(1, 1.5))

	def test_eq(self):
		u = vec2(2,3)
		v = vec2(1+1, 6/2)
		w = vec2(3,2)
		self.assertEqual(u==v, True)
		self.assertEqual(u==w, False)

	def test_cmp(self):
		u = vec2(1,2)
		v = vec2(1,3)
		w = vec2(2,3)
		self.assertEqual(u > v, False)
		self.assertEqual(u > w, False)
		self.assertEqual(v > w, False)
		self.assertEqual(u < v, True)
		self.assertEqual(u < w, True)
		self.assertEqual(v < w, True)

	def test_lenght(self):
		u = vec2(1,2)
		self.assertEqual(u.length, math.sqrt(5))

	def test_unit(self):
		u = vec2(1,2)
		self.assertEqual(u.unit, u / math.sqrt(5))

	def test_dot(self):
		u = vec2(1,2)
		v = vec2(3,2)
		self.assertEqual(dot(u,v), 7)

	def test_distance(self):
		u = vec2(1,3)
		v = vec2(3,2)
		w = u - v
		self.assertEqual(distance(u,v), w.length)

class TestVec3(unittest.TestCase):
	def test_getter_setter(self):
		u = vec3()
		u[0] = 1
		self.assertEqual(u[0], 1)

	def test_add(self):
		u = vec3(1,2,5)
		v = vec3(-4,5,0)
		self.assertEqual(u+v, vec3(-3,7,5))

	def test_iadd(self):
		u = vec3(1,2,-5)
		u += u
		self.assertEqual(u, vec3(2,4,-10))		

	def test_mul_scalar(self):
		u = vec3(2,3,-5)
		self.assertEqual(u*2, vec3(4,6,-10))

	def test_mul_vec2(self):
		u = vec3(2,3,-5)
		v = vec3(3,4,6)
		self.assertEqual(u*v, vec3(6,12,-30))

	def test_mul_mat3(self):
		u = vec3(2,3,-1)
		A = mat3(1,2,3,4,5,6,7,8,9)
		self.assertEqual(u*A, vec3(7,11,15))

	def test_truediv(self):
		u = vec3(2,3,6)
		self.assertEqual(u/2, vec3(1, 1.5,3))

	def test_eq(self):
		u = vec3(2,3,6)
		v = vec3(1+1, 6/2, 1.5*4)
		w = vec3(3,2,6)
		self.assertEqual(u==v, True)
		self.assertEqual(u==w, False)

	def test_cmp(self):
		u = vec3(1,2,-5)
		v = vec3(1,2,-1)
		w = vec3(2,-3,2)
		self.assertEqual(u > v, False)
		self.assertEqual(u > w, False)
		self.assertEqual(v > w, False)
		self.assertEqual(u < v, True)
		self.assertEqual(u < w, True)
		self.assertEqual(v < w, True)

	def test_lenght(self):
		u = vec3(1,2,3)
		self.assertEqual(u.length, math.sqrt(14))

	def test_unit(self):
		u = vec3(1,2,3)
		self.assertEqual(u.unit, u / math.sqrt(14))

	def test_dot(self):
		u = vec3(1,2,3)
		v = vec3(3,2,1)
		self.assertEqual(dot(u,v), 10)

	def test_distance(self):
		u = vec3(1,2,3)
		v = vec3(3,2,1)
		w = u - v
		self.assertEqual(distance(u,v), w.length)

	def test_cross(self):
		u = vec3(1,2,3)
		v = vec3(3,2,1)
		self.assertEqual(cross(u,v), vec3(-4,8,-4))


class TestVec4(unittest.TestCase):
	def test_getter_setter(self):
		u = vec4()
		u[0] = 1
		self.assertEqual(u[0], 1)

	def test_add(self):
		u = vec4(1,2,5,7)
		v = vec4(-4,5,0,-3)
		self.assertEqual(u+v, vec4(-3,7,5,4))

	def test_iadd(self):
		u = vec4(1,2,-5,7)
		u += u
		self.assertEqual(u, vec4(2,4,-10,14))		

	def test_mul_scalar(self):
		u = vec4(2,3,-5,7)
		self.assertEqual(u*2, vec4(4,6,-10,14))

	def test_mul_vec4(self):
		u = vec4(2,3,-5,9)
		v = vec4(3,4,6,2)
		self.assertEqual(u*v, vec4(6,12,-30,18))

	def test_mul_mat4(self):
		u = vec4(2,3,-1, 5)
		A = mat4(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
		self.assertEqual(u*A, vec4(73, 82, 91, 100))

	def test_truediv(self):
		u = vec4(2,3,6,8)
		self.assertEqual(u/2, vec4(1, 1.5,3,4))

	def test_eq(self):
		u = vec4(2,3,6,8)
		v = vec4(1+1, 6/2, 1.5*4, 2**3)
		w = vec4(3,2,6,8)
		self.assertEqual(u==v, True)
		self.assertEqual(u==w, False)

	def test_cmp(self):
		u = vec4(1,2,-5,7)
		v = vec4(1,2,-1,3)
		w = vec4(2,-3,2,4)
		self.assertEqual(u > v, False)
		self.assertEqual(u > w, False)
		self.assertEqual(v > w, False)
		self.assertEqual(u < v, True)
		self.assertEqual(u < w, True)
		self.assertEqual(v < w, True)

	def test_lenght(self):
		u = vec4(1,2,3,4)
		self.assertEqual(u.length, math.sqrt(30))

	def test_unit(self):
		u = vec4(1,2,3,4)
		self.assertEqual(u.unit, u / math.sqrt(30))

	def test_dot(self):
		u = vec4(1,2,3,5)
		v = vec4(3,2,1,6)
		self.assertEqual(dot(u,v), 40)

	def test_distance(self):
		u = vec4(1,2,3,4)
		v = vec4(3,2,1,5)
		w = u - v
		self.assertEqual(distance(u,v), w.length)

if __name__ == '__main__':
    unittest.main()
