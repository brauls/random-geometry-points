import sys
import os
import math
import pytest

PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_PATH + '/../src/')

from random_geometry_points.circle2d import Circle2D

def test_create_random_points():
    """Test the create_random_points method of Circle2D.

    Create a set of different circles definitions along with the desired point count.
    For each circle it is checked wether the number of created points matches
    the expected number of points.
    Furthermore it is checked if the created points lie on the 2D circle, respectively.
    """

    def check_circle_results(circle, num_points):
        """Check the randomly generated points for a given circle and point count.
        """
        actual_points = circle.create_random_points(num_points)
        assert all([len(point) == 2 for point in actual_points])
        assert len(actual_points) == num_points
        center_x = circle.center_x
        center_y = circle.center_y
        radius = circle.radius
        dist_to_center = lambda point: math.sqrt((point[0]-center_x)**2 + (point[1]-center_y)**2)
        is_circle_point = lambda point: math.isclose(dist_to_center(point), radius)
        assert all(is_circle_point(point) for point in actual_points)

    circles = [
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

    for circle in circles:
        check_circle_results(circle[0], circle[1])

def test_create_random_points_exc():
    """Test the create_random_points method of Circle2D.

    Create a set of different invalid circles definitions.
    Check if for each circle definition the expected exception is raised.
    """

    def check_circle_creation(center_x, center_y, radius, expected_exception):
        """Check the circle parameters to raise the expected exception
        """
        with pytest.raises(expected_exception):
            Circle2D(center_x, center_y, radius)

    def check_point_count(circle, num_points, expected_exception):
        """Check the number of desired points to raise the expected exception.
        """
        with pytest.raises(expected_exception):
            circle.create_random_points(num_points)

    circle_creation_errors = [
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

    point_count_errors = [
        (Circle2D(2.0, 5.0, 5), "3", TypeError),
        (Circle2D(2.0, 5.0, 5), "test", TypeError),
        (Circle2D(2.0, 5.0, 5), 4.5, TypeError),
        (Circle2D(2.0, 5.0, 5), -5, ValueError),
        (Circle2D(2.0, 5.0, 5), 0, ValueError),
        (Circle2D(2.0, 5.0, 5), 100000, ValueError)
    ]

    for circle in circle_creation_errors:
        check_circle_creation(circle[0], circle[1], circle[2], circle[3])

    for circle in point_count_errors:
        check_point_count(circle[0], circle[1], circle[2])
