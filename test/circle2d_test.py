import sys
import os
import math
import pytest

PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_PATH + '/../')

from random_geometry_points.circle2d import Circle2D

def test_create_random_points():
    """Test the create_random_points method of Circle2D.

    Create a list of different circle definitions along with the desired point count.
    For each circle it is checked if the number of created points matches
    the expected number of points.
    Furthermore it is checked if the created points lie on the 2D circle, respectively.
    """
    circles = _get_valid_circle_definitions()
    for circle in circles:
        circle_points = circle[0].create_random_points(circle[1])
        _check_valid_circle_results(circle[0], circle[1], circle_points)

def test_create_random_point_gen():
    """Test the create_random_point_generator method of Circle2D.

    Create a list of different circle definitions along with the desired point count.
    For each circle it is checked if the number of created points matches
    the expected number of points.
    Furthermore it is checked if the created points lie on the 2D circle, respectively.
    """
    circles = _get_valid_circle_definitions()
    for circle in circles:
        circle_points = [point for point in circle[0].create_random_point_generator(circle[1])]
        _check_valid_circle_results(circle[0], circle[1], circle_points)

def test_create_random_points_exc():
    """Test the create_random_points and create_random_point_generator methods of Circle2D.

    Create a list of different invalid circle definitions.
    Check if for each circle definition the expected exception is raised.
    """
    def check_circle_creation(center_x, center_y, radius, expected_exception):
        """Check the circle parameters to raise the expected exception
        """
        with pytest.raises(expected_exception):
            Circle2D(center_x, center_y, radius)

    def check_point_count(circle, num_points, expected_exception):
        """Check the create_random_points method to raise an exception because of
        an invalid number of points to be created.
        """
        with pytest.raises(expected_exception):
            circle.create_random_points(num_points)

    def check_point_count_gen(circle, num_points, expected_exception):
        """Check the create_random_point_generator method to raise an exception because of
        an invalid number of points to be created.
        """
        with pytest.raises(expected_exception):
            circle.create_random_point_generator(num_points)

    circle_creation_errors = _get_invalid_circle_definitions()
    point_count_errors = _get_circles_with_invalid_point_count()
    for circle in circle_creation_errors:
        check_circle_creation(circle[0], circle[1], circle[2], circle[3])
    for circle in point_count_errors:
        check_point_count(circle[0], circle[1], circle[2])
        check_point_count_gen(circle[0], circle[1], circle[2])

def _get_valid_circle_definitions():
    """Create a list of valid 2D circle parameters.

    Create and return a static list of tuples each containing the parameters of
    a 2D circle along with the desired number of random points to be created.

    Returns:
        list (tuple (Circle2D, int) ): List with 2D circle parameters and desired point count
    """
    return [
        (Circle2D(3.0, 5.0, 10.0), 5),
        (Circle2D(3.0, 5.0, 1.0), 10),
        (Circle2D(-2.0, 4.0, 5.0), 20),
        (Circle2D(3.55, -44.2, 5422.5), 100),
        (Circle2D(200, 1070, 55), 5),
        (Circle2D(4.5, 10, 4), 5),
        (Circle2D(10000.78, 99453.44, 10455.6), 5),
        (Circle2D(-55466.4, -22331.5, 99002.5), 5),
        (Circle2D(0.005, -0.00064, 0.00085), 5),
        (Circle2D(0.005, -0.00064, 0.00085), 99999)
    ]

def _get_invalid_circle_definitions():
    """Create a list of invalid 2D circle parameters.

    Create and return a list of tuples each containing invalid parameters of
    a 2D circle along with the expected type of exception that should be thrown.

    An invalid parameter is a parameter with either an unexpected data type or value.

    Returns:
        list (tuple (any, any, any, Exception)): List with 2D circle parameters
          and the expected exception
    """
    return [
        ("4.5", 5.0, 10.0, TypeError),
        (4.5, "test", 10.0, TypeError),
        (7, 5.0, "4", TypeError),
        (4, 5.0, -9.5, ValueError),
        (3, 5.0, 0.0, ValueError),
        (3, 5.0, 0, ValueError),
        (float("nan"), 5.0, 2.0, ValueError),
        (3, float("nan"), 2.0, ValueError),
        (3, 5.0, float("nan"), ValueError),
        (float("inf"), 5.0, 2.0, ValueError),
        (3, float("inf"), 2.0, ValueError),
        (3, 5.0, float("inf"), ValueError),
        (float("-inf"), 5.0, 2.0, ValueError),
        (3, float("-inf"), 2.0, ValueError),
        (3, 5.0, float("-inf"), ValueError)
    ]

def _get_circles_with_invalid_point_count():
    """Create a list of 2D circle parameters and invalid point count values.

    Create and return a list of tuples each containing valid 2D circle parameters
    along with an invalid number of desired random points.

    An invalid number is either a value of wrong type or with an invalid value.

    Returns:
        list (tuple (Circle2D, any): List with 2D circle parameters
          and an invalid number of random points
    """
    return [
        (Circle2D(2.0, 5.0, 5), "3", TypeError),
        (Circle2D(2.0, 5.0, 5), "test", TypeError),
        (Circle2D(2.0, 5.0, 5), 4.5, TypeError),
        (Circle2D(2.0, 5.0, 5), -5, ValueError),
        (Circle2D(2.0, 5.0, 5), 0, ValueError),
        (Circle2D(2.0, 5.0, 5), 100000, ValueError),
        (Circle2D(2.0, 5.0, 5), float('nan'), TypeError),
        (Circle2D(2.0, 5.0, 5), float("inf"), TypeError),
        (Circle2D(2.0, 5.0, 5), float("-inf"), TypeError)
    ]

def _check_valid_circle_results(circle, num_points, circle_points):
    """Check the randomly generated points for a valid 2D circle definition.

    It is checked that num_points points are created and that each created point
    lies on the defined 2D circle.

    Args:
        circle (Circle2D): A valid 2D circle definition
        num_points (int): A valid number of random points to be created
        circle_points (list (tuple(float, float))): The randomly created points
          for the given circle and num_points
    """
    assert all([len(point) == 2 for point in circle_points])
    assert len(circle_points) == num_points
    center_x = circle.center_x
    center_y = circle.center_y
    radius = circle.radius
    dist_to_center = lambda point: math.sqrt((point[0]-center_x)**2 + (point[1]-center_y)**2)
    is_circle_point = lambda point: math.isclose(dist_to_center(point), radius)
    assert all(is_circle_point(point) for point in circle_points)
