import sys
import os
import math
import pytest

PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_PATH + '/../')

from random_geometry_points.plane import Plane

def test_create_random_points():
    """Test the create_random_points method of Plane.

    Create a list of different plane definitions along with the desired point count.
    For each plane it is checked if the number of created points matches
    the expected number of points.
    Furthermore it is checked if the created points lie on the plane, respectively.
    """
    planes = _get_valid_plane_definitions()
    for plane in planes:
        plane_points = plane[0].create_random_points(plane[1])
        _check_valid_plane_results(plane[0], plane[1], plane_points)

def test_create_random_points_gen():
    """Test the create_random_point_generator method of Plane.

    Create a list of different plane definitions along with the desired point count.
    For each plane it is checked if the number of created points matches
    the expected number of points.
    Furthermore it is checked if the created points lie on the plane, respectively.
    """
    planes = _get_valid_plane_definitions()
    for plane in planes:
        plane_points = [point for point in plane[0].create_random_point_generator(plane[1])]
        _check_valid_plane_results(plane[0], plane[1], plane_points)

def test_create_random_points_exc():
    """Test the create_random_points and create_random_point_generator methods of Plane.

    Create a list of different invalid plane definitions.
    Check if for each plane definition the expected exception is raised.
    """
    def check_hessian_normal_form(normal_vec, d_origin, ref_point, radius, expected_exception):
        """Check the plane parameters to raise the expected exception
        """
        with pytest.raises(expected_exception):
            Plane(normal_vec, d_origin, ref_point, radius)

    def check_normal_form(normal_vec, position_vec, radius, expected_exception):
        """Check the plane parameters to raise the expected exception
        """
        with pytest.raises(expected_exception):
            Plane.from_normal_form(normal_vec, position_vec, radius)

    def check_point_count(plane, num_points, expected_exception):
        """Check the create_random_points method to raise an exception because of
        an invalid number of points to be created.
        """
        with pytest.raises(expected_exception):
            plane.create_random_points(num_points)

    def check_point_count_gen(plane, num_points, expected_exception):
        """Check the create_random_point_generator method to raise an exception because of
        an invalid number of points to be created.
        """
        with pytest.raises(expected_exception):
            plane.create_random_point_generator(num_points)

    invalid_normal_forms = _get_invalid_plane_definitions_normal_form()
    invalid_hessian_normal_forms = _get_invalid_plane_definitions_hessian_normal_form()
    point_count_errors = _get_planes_with_invalid_point_count()
    for plane in invalid_normal_forms:
        check_normal_form(plane[0], plane[1], plane[2], plane[3])
    for plane in invalid_hessian_normal_forms:
        check_hessian_normal_form(plane[0], plane[1], plane[2], plane[3], plane[4])
    for plane in point_count_errors:
        check_point_count(plane[0], plane[1], plane[2])
        check_point_count_gen(plane[0], plane[1], plane[2])

def _get_valid_plane_definitions():
    """Create a list of valid plane parameters.

    Create and return a static list of tuples each containing the parameters of
    a plane along with the desired number of random points to be created.

    Returns:
        list (tuple (Plane, int) ): List with plane parameters and desired point count
    """
    return [
        (Plane((0.9, 0, 0), 3.5, (3.5, 7.0, 8.0), 15.0), 5),
        (Plane((1.0, 0, 0), 3.5, (3.5, 7.0, 8.0), 90000.0), 5),
        (Plane((0, 1.0, 0), 3.5, (99855, 3.5, 89445), 15.0), 5),
        (Plane((2, 2, 0), math.sqrt(200), (10, 10, 8.0), 15.0), 99999),
        (Plane((1.0, 5, 8), 0, (0, 0, 0), 15.0), 5),
        (Plane((1, 0, 0), -7, (-7, 6, -7.45), 15.0), 5),
        (Plane((-1, 0, 0), -7, (7, 6, -7.45), 15.0), 5),
        (Plane.from_normal_form((0.9, 0, 0), (3, 2.4, 9), 15.0), 5),
        (Plane.from_normal_form((1, 0, 0), (3, 2.4, 9), 15.0), 5),
        (Plane.from_normal_form((0.55, 0.55, 0.55), (0, 0, 0), 4), 5),
        (Plane.from_normal_form((0.55, 0.55, 0.55), (0, 0, 0), 0.01), 5),
        (Plane.from_normal_form((99254, 88777.7, 26755), (0, 0, 0), 0.01), 5)
    ]

def _get_invalid_plane_definitions_hessian_normal_form():
    """Create a list of invalid plane parameters.

    Create and return a list of tuples each containing invalid parameters of
    a plane along with the expected type of exception that should be thrown.

    The order of parameters is: normal_vec, d_origin, ref_point, radius

    An invalid parameter is a parameter with either an unexpected data type or value.

    Returns:
        list (tuple (any, any, any, any, Exception)): List with plane parameters
          and the expected exception
    """
    return [
        (("4.5", 2, 4), 2.0, (1, 2, 3), 10.0, TypeError),
        ((4.5, "2", 4), 2.0, (1, 2, 3), 10.0, TypeError),
        ((4.5, 2, "4"), 2.0, (1, 2, 3), 10.0, TypeError),
        ((4.5, 2, 4), "2.0", (1, 2, 3), 10.0, TypeError),
        ((4.5, 2, 4), 2.0, ("1", 2, 3), 10.0, TypeError),
        ((4.5, 2, 4), 2.0, (1, "2", 3), 10.0, TypeError),
        ((4.5, 2, 4), 2.0, (1, 2, "3"), 10.0, TypeError),
        ((4.5, 2, 4), 2.0, (1, 2, 3), "10.0", TypeError),
        ((float("nan"), 2, 4), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, float("nan"), 4), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, float("nan")), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), float("nan"), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (float("nan"), 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, float("nan"), 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, 2, float("nan")), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, 2, 3), float("nan"), ValueError),
        ((float("inf"), 2, 4), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, float("inf"), 4), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, float("inf")), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), float("inf"), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (float("inf"), 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, float("inf"), 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, 2, float("inf")), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, 2, 3), float("inf"), ValueError),
        ((float("-inf"), 2, 4), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, float("-inf"), 4), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, float("-inf")), 2.0, (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), float("-inf"), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (float("-inf"), 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, float("-inf"), 3), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, 2, float("-inf")), 10.0, ValueError),
        ((4.5, 2, 4), 2.0, (1, 2, 3), float("-inf"), ValueError),
        ((0, 0, 0), 2.0, (1, 2, 3), 10.0, ValueError),
        ((0.0, 0.0, 0.0), 2.0, (1, 2, 3), 10.0, ValueError),
        ((0.89, 0, 0), 2.0, (2, 0, 0), 10.0, ValueError),
        ((1.0, 0, 0), 2.0, (2, 0, 0), 0, ValueError),
        ((1.0, 0, 0), 2.0, (2, 0, 0), 0.0, ValueError),
        ((1.0, 0, 0), 2.0, (2, 0, 0), -1.0, ValueError),
    ]

def _get_invalid_plane_definitions_normal_form():
    """Create a list of invalid plane parameters.

    Create and return a list of tuples each containing invalid parameters of
    a plane along with the expected type of exception that should be thrown.

    The order of parameters is: normal_vec, position_vec, radius

    An invalid parameter is a parameter with either an unexpected data type or value.

    Returns:
        list (tuple (any, any, any, Exception)): List with plane parameters
          and the expected exception
    """
    return [
        (("4.5", 2, 4), (1, 2, 3), 10.0, TypeError),
        ((4.5, "2", 4), (1, 2, 3), 10.0, TypeError),
        ((4.5, 2, "4"), (1, 2, 3), 10.0, TypeError),
        ((4.5, 2, 4), ("1", 2, 3), 10.0, TypeError),
        ((4.5, 2, 4), (1, "2", 3), 10.0, TypeError),
        ((4.5, 2, 4), (1, 2, "3"), 10.0, TypeError),
        ((4.5, 2, 4), (1, 2, 3), "10.0", TypeError),
        ((float("nan"), 2, 4), (1, 2, 3), 10.0, ValueError),
        ((4.5, float("nan"), 4), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, float("nan")), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), (float("nan"), 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), (1, float("nan"), 3), 10.0, ValueError),
        ((4.5, 2, 4), (1, 2, float("nan")), 10.0, ValueError),
        ((4.5, 2, 4), (1, 2, 3), float("nan"), ValueError),
        ((float("inf"), 2, 4), (1, 2, 3), 10.0, ValueError),
        ((4.5, float("inf"), 4), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, float("inf")), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), (float("inf"), 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), (1, float("inf"), 3), 10.0, ValueError),
        ((4.5, 2, 4), (1, 2, float("inf")), 10.0, ValueError),
        ((4.5, 2, 4), (1, 2, 3), float("inf"), ValueError),
        ((float("-inf"), 2, 4), (1, 2, 3), 10.0, ValueError),
        ((4.5, float("-inf"), 4), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, float("-inf")), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), (float("-inf"), 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), (1, float("-inf"), 3), 10.0, ValueError),
        ((4.5, 2, 4), (1, 2, float("-inf")), 10.0, ValueError),
        ((4.5, 2, 4), (1, 2, 3), float("-inf"), ValueError),
        ((0, 0, 0), (1, 2, 3), 10.0, ValueError),
        ((0.0, 0.0, 0.0), (1, 2, 3), 10.0, ValueError),
        ((0.51, 0.51, 0.51), (1, 2, 3), 10.0, ValueError),
        ((4.5, 2, 4), (1, 2, 3), 0, ValueError),
        ((4.5, 2, 4), (1, 2, 3), 0.0, ValueError),
        ((4.5, 2, 4), (1, 2, 3), -1.0, ValueError)
    ]

def _get_planes_with_invalid_point_count():
    """Create a list of plane parameters and invalid point count values.

    Create and return a list of tuples each containing valid plane parameters
    along with an invalid number of desired random points.

    An invalid number is either a value of wrong type or with an invalid value.

    Returns:
        list (tuple (Plane, any): List with plane parameters
          and an invalid number of random points
    """
    return [
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), "3", TypeError),
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), "test", TypeError),
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), 4.5, TypeError),
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), -5, ValueError),
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), 0, ValueError),
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), 100000, ValueError),
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), float("nan"), TypeError),
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), float("inf"), TypeError),
        (Plane((1.0, 0, 0), 5.0, (5.0, 5, 6), 5), float("-inf"), TypeError)
    ]

def _check_valid_plane_results(plane, num_points, plane_points):
    """Check the randomly generated points for a valid plane definition.

    It is checked that num_points points are created and that each created point
    lies on the defined plane.

    Args:
        plane (Plane): A valid plane definition
        num_points (int): A valid number of random points to be created
        plane_points (list (tuple (float, float, float))): The randomly created points
          for the given plane and num_points
    """
    assert all([len(point) == 3 for point in plane_points])
    assert len(plane_points) == num_points
    (n_x, n_y, n_z) = plane.normal_vec
    d_origin = plane.d_origin
    dist_to_plane = lambda p: p[0]*n_x + p[1]*n_y + p[2]*n_z - d_origin
    is_plane_point = lambda p: math.isclose(dist_to_plane(p), 0.0, abs_tol=0.000001)
    assert all(is_plane_point(point) for point in plane_points)
