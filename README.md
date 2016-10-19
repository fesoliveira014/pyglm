# pyglm
pyglm is a Python 3 implementation of the OpenGL math library [glm](http://glm.g-truc.net). The objective of this module is to give native support to some of the best features of glm, such as vectors and matrices for computer graphics, as well as other relevant functions and structures. 

## Features

- Vectors of 2, 3 and 4 dimensions.
- Square matrices of 2, 3 and 4 dimensions.
- Basic transforms: translate, rotate and scale.
- Basic vector and matrix functionalites: 
    + dot product for vectors
    + cross product for 3d vectors
    + \*operator overload for arithmethic operations over matrices and vectors
- \*\*Test units 
- GLSL syntax 

>\* The operator overload follows glm convention, such that a product between vectors: let a, b be two 2d vectors, `a * b = (a.x * b.x, a.y * b.y)`

>\*\* Test units are only implemented for vectors so far.

## Planned Features

- Test units for matrices
- Other transforms and operations, such as project, unproject and lookat
- Geometric functions, such as faceForward, reflect and refract
- Math functions such as mix, clamp, step, min/max
- Noise functions, such as Perlin Noise, Simplex Noise, fractal noise, etc
- Color space conversions
- Quaternions
- Other matrix dimensions (?)
- Test units for each new set of features

## Dependencies

There are no explicit dependencies on the module apart from Python 3. This might change in the future, but I will try to keep third-party dependencies to a minimum, if they become necessary.

## Usage

To use the modules, just import the module into your project and use it.

```python
>>> from glvector import *
>>> from glmatrix import *
>>>
>>> u = vec2(1,2)
>>> v = vec2(3,4)
>>>
>>> distance(u,v)
2.8284271247461903
>>>
>>> A = mat2.fromVec2(u,v)
>>> A
mat2(1, 2, 3, 4)
>>>
>>> A * u
vec2(5,11)

```

## License

MIT License

Copyright (c) 2016 Felipe Santos Oliveira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
