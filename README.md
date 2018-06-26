[![Build Status](https://travis-ci.org/brauls/random-geometry-points.svg?branch=master)](https://travis-ci.org/brauls/random-geometry-points)
[![Coverage Status](https://coveralls.io/repos/github/brauls/random-geometry-points/badge.svg?branch=master)](https://coveralls.io/github/brauls/random-geometry-points?branch=master)
[![PyPI version](https://badge.fury.io/py/random-geometry-points.svg)](https://badge.fury.io/py/random-geometry-points)
[![PyPI pyversions](https://img.shields.io/badge/python-3.6-blue.svg)](https://badge.fury.io/py/random-geometry-points)

# random-geometry-points

This module provides classes to generate random points on geometry surfaces.
These points can then be used as test data, e.g. to simulate measurements of a measurement device.

## Installation

You can install this module using pip globally
```bash
pip install random-geometry-points
```
or using pipenv
```bash
cd <your project folder>
pipenv install random-geometry-points
```

## Basic Usage

Currently the geometry types <b>Plane</b>, <b>Sphere</b> and <b>2D Circle</b> are supported.
You can import the geometry classes by using the following import statements.

```python
from random_geometry_points.plane import Plane
from random_geometry_points.sphere import Sphere
from random_geometry_points.circle2d import Circle2D
```

Now you can create an arbitrary number of random points lying on a geometry surface.

```python
# create a plane object with n = (1, 0, 0), x0 = (0, 0, 0), d = 0 and radius = 10
normal_vec = (1.0, 0.0, 0.0)
ref_point = (0.0, 0.0, 0.0)
plane = Plane(normal_vec, 0.0, ref_point, 10.0)

# create and print 3 random points lying on the plane
random_plane_points = plane.create_random_points(3)
print(random_plane_points)
# example output: [(0.0, -2.058506783308933, -5.777518695971468), (0.0, 2.501766732323411, 6.740902158795952), (0.0, 7.846400008799242, 5.304670974614023)]
```

```python
# create a sphere object with x = 1.0, y = -4.5, z = 3.3 and radius = 11.35
sphere = Sphere(1.0, -4.5, 3.3, 11.35)

# create and print 3 random points lying on the sphere
random_sphere_points = sphere.create_random_points(3)
print(random_sphere_points)
# example output: [(4.442124959724451, -1.593759345598388, -7.1176792530940025), (-7.102728837759106, -6.022944977793705, -4.500572028791214), (-10.190814503489936, -4.676727604583875, 5.1859846505890115)]
```

```python
# create a circle object with x = 1.0, y = -4.5 and radius = 11.35
circle = Circle2D(1.0, -4.5, 11.35)

# create and print 3 random points lying on the circle
random_circle_points = circle.create_random_points(3)
print(random_circle_points)
# example output: [(4.057509245253113, -15.430422554283604), (2.2509595260473114, 6.780851043436018), (9.330996610075898, 3.2082420488010035)]
```

## Documentation

Please take a look at the [Wiki](https://github.com/brauls/random-geometry-points/wiki) for a more detailed description. There you get more detailed information on how you can use the geometry classes, the meaning of the geometry parameters and error handling.

## Deployment

### Update packages

```pipenv update --dev setuptools wheel twine```

### Update `setup.py`

Update the content of `setup.py`, especially the version information.

### Commit and tag

Commit and push the changes along with a new version tag. Travis will run the test cases automatically when pushing to the master branch.

### Build source archive and built distribution

```pipenv run python setup.py sdist bdist_wheel```

### Deploy to PyPi or TestPyPi to test things first

```pipenv run twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*```

```pipenv run twine upload --skip-existing dist/*```

## Useful links

* [Configuring pipenv for Visual Studio Code](https://olav.it/2017/03/04/pipenv-visual-studio-code/)
* [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
