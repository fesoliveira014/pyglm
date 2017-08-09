# Changelog

## v0.3

### New

- Vector
    - Added the following functions: faceForward, reflect and refract
        - These are found under geometric function in GLM, but since most geometric functions are already implemented as overloads, simply adding these functions here serves its purpose
- Common:
    - Added the following functions: step, smoothstep and fma

- Changed standard identation from tabs to spaces    
- Minor code refactor on some variable names and imports

## Known Issues

- No changes from previous version

## v0.2

### New

- Vector:
    - Right-hand operator overload added for arithmetic operations
- Matrix:
    - Right-hand operator overload added for arithmetic operations
- Transforms:
    - Added project, unproject and lookAt
    - Added frustum matrix generation
- Added Common functions:
    - fract, mod, modf, min, max, clamp and mix
- Misc:
    - Added changelog and todo documents

### Known Issues

- Matrix:
    - Right-handed multiplication and division are not implemented
    - Floor division not implemented

## v0.1

### New

- Vector: 2, 3 and 4 dimensions
    - Operator overload: arithmetic, self operators, math operators
    - Basic operations: dot, cross (__vec3__), distance, length and normalize
    - Relational operators: equal, less, greater and combinations
- Matrix: 2, 3 and 4 dimensions
    - Operator overload: arithmetic, self operators, math operators
    - Basic operations: inverse, determinant and transpose
- Transforms: translate, rotate and scale
    - Projections: perspective and orthographic
    - Docstrings for all functions
- Unit tests:
    - Vector unit tests