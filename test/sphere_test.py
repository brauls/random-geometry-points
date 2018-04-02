import sys
import os
import math
import pytest

PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_PATH + '/../')

from random_geometry_points.sphere import Sphere

def test_create_random_points():
    """Test the create_random_points method of Sphere.

    Create a list of different sphere definitions along with the desired point count.
    For each sphere it is checked if the number of created points matches
    the expected number of points.
    Furthermore it is checked if the created points lie on the sphere, respectively.
    """
    spheres = _get_valid_sphere_definitions()
    for sphere in spheres:
        sphere_points = sphere[0].create_random_points(sphere[1])
        _check_valid_sphere_results(sphere[0], sphere[1], sphere_points)

def test_create_random_point_gen():
    """Test the create_random_point_generator method of Sphere.

    Create a list of different sphere definitions along with the desired point count.
    For each sphere it is checked if the number of created points matches
    the expected number of points.
    Furthermore it is checked if the created points lie on the sphere, respectively.
    """
    spheres = _get_valid_sphere_definitions()
    for sphere in spheres:
        sphere_points = [point for point in sphere[0].create_random_point_generator(sphere[1])]
        _check_valid_sphere_results(sphere[0], sphere[1], sphere_points)

def test_create_random_points_exc():
    """Test the create_random_points and create_random_point_generator methods of Sphere.

    Create a list of different invalid sphere definitions.
    Check if for each sphere definition the expected exception is raised.
    """
    def check_sphere_creation(center_x, center_y, center_z, radius, expected_exception):
        """Check the sphere parameters to raise the expected exception
        """
        with pytest.raises(expected_exception):
            Sphere(center_x, center_y, center_z, radius)

    def check_point_count(sphere, num_points, expected_exception):
        """Check the create_random_points method to raise an exception because of
        an invalid number of points to be created.
        """
        with pytest.raises(expected_exception):
            sphere.create_random_points(num_points)

    def check_point_count_gen(sphere, num_points, expected_exception):
        """Check the create_random_point_generator method to raise an exception because of
        an invalid number of points to be created.
        """
        with pytest.raises(expected_exception):
            sphere.create_random_point_generator(num_points)

    sphere_creation_errors = _get_invalid_sphere_definitions()
    point_count_errors = _get_spheres_with_invalid_point_count()
    for sphere in sphere_creation_errors:
        check_sphere_creation(sphere[0], sphere[1], sphere[2], sphere[3], sphere[4])
    for sphere in point_count_errors:
        check_point_count(sphere[0], sphere[1], sphere[2])
        check_point_count_gen(sphere[0], sphere[1], sphere[2])

def _get_valid_sphere_definitions():
    """Create a list of valid sphere parameters.

    Create and return a static list of tuples each containing the parameters of
    a sphere along with the desired number of random points to be created.

    Returns:
        list (tuple (Sphere, int) ): List with sphere parameters and desired point count
    """
    return [
        (Sphere(3.0, 5.0, 7.0, 10.0), 5),
        (Sphere(3.0, 5.0, 7.0, 1.0), 10),
        (Sphere(-2.0, 4.0, 10.0, 5.0), 20),
        (Sphere(3.55, -44.2, 14.35, 5422.5), 100),
        (Sphere(200, 1070, 34, 55), 5),
        (Sphere(4.5, 10, -6.5, 4), 5),
        (Sphere(10000.78, 99453.44, 99738.56, 10455.6), 5),
        (Sphere(-55466.4, -22331.5, -45763.54, 99002.5), 5),
        (Sphere(0.005, -0.00064, 0.00074, 0.00085), 5),
        (Sphere(0.005, -0.00064, -0.00074, 0.00085), 99999)
    ]

def _get_invalid_sphere_definitions():
    """Create a list of invalid sphere parameters.

    Create and return a list of tuples each containing invalid parameters of
    a sphere along with the expected type of exception that should be thrown.

    An invalid parameter is a parameter with either an unexpected data type or value.

    Returns:
        list (tuple (any, any, any, any, Exception)): List with sphere parameters
          and the expected exception
    """
    return [
        ("4.5", 5.0, 7.0, 10.0, TypeError),
        (4.5, "test", 7.0, 10.0, TypeError),
        (4.5, 5.0, "7", 10.0, TypeError),
        (7, 5.0, 7.0, "4", TypeError),
        (4, 5.0, 7.5, -9.5, ValueError),
        (3, 5.0, 8, 0.0, ValueError),
        (3, 5.0, 8, 0, ValueError),
        (float("nan"), 5.0, 7.0, 2.0, ValueError),
        (3, float("nan"), 7.0, 2.0, ValueError),
        (3, 5.0, float("nan"), 2.0, ValueError),
        (3, 5.0, 7.0, float("nan"), ValueError),
        (float("inf"), 5.0, 7.0, 2.0, ValueError),
        (3, float("inf"), 7.0, 2.0, ValueError),
        (3, 5.0, float("inf"), 2.0, ValueError),
        (3, 5.0, 7.0, float("inf"), ValueError),
        (float("-inf"), 5.0, 7.0, 2.0, ValueError),
        (3, float("-inf"), 7.0, 2.0, ValueError),
        (3, 5.0, float("-inf"), 2.0, ValueError),
        (3, 5.0, 7.0, float("-inf"), ValueError)
    ]

def _get_spheres_with_invalid_point_count():
    """Create a list of sphere parameters and invalid point count values.

    Create and return a list of tuples each containing valid sphere parameters
    along with an invalid number of desired random points.

    An invalid number is either a value of wrong type or with an invalid value.

    Returns:
        list (tuple (Sphere, any): List with sphere parameters
          and an invalid number of random points
    """
    return [
        (Sphere(2.0, 5.0, 7.0, 5), "3", TypeError),
        (Sphere(2.0, 5.0, 7.0, 5), "test", TypeError),
        (Sphere(2.0, 5.0, 7.0, 5), 4.5, TypeError),
        (Sphere(2.0, 5.0, 7.0, 5), -5, ValueError),
        (Sphere(2.0, 5.0, 7.0, 5), 0, ValueError),
        (Sphere(2.0, 5.0, 7.0, 5), 100000, ValueError),
        (Sphere(2.0, 5.0, 7.0, 5), float("nan"), TypeError),
        (Sphere(2.0, 5.0, 7.0, 5), float("inf"), TypeError),
        (Sphere(2.0, 5.0, 7.0, 5), float("-inf"), TypeError)
    ]

def _check_valid_sphere_results(sphere, num_points, sphere_points):
    """Check the randomly generated points for a valid sphere definition.

    It is checked that num_points points are created and that each created point
    lies on the defined sphere.

    Args:
        sphere (Sphere): A valid sphere definition
        num_points (int): A valid number of random points to be created
        sphere_points (list (tuple (float, float, float))): The randomly created points
          for the given sphere and num_points
    """
    assert all([len(point) == 3 for point in sphere_points])
    assert len(sphere_points) == num_points
    center_x = sphere.center_x
    center_y = sphere.center_y
    center_z = sphere.center_z
    radius = sphere.radius
    dist_to_center = lambda p: math.sqrt((p[0]-center_x)**2+(p[1]-center_y)**2+(p[2]-center_z)**2)
    is_sphere_point = lambda p: math.isclose(dist_to_center(p), radius)
    assert all(is_sphere_point(point) for point in sphere_points)
