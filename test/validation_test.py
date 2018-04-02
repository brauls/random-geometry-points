import sys
import os
import math
import pytest

PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_PATH + '/../')

import random_geometry_points.validation as validation

def test_check_num_random_points():
    """Test the check_number_of_random_points function of the validation module.
    """
    expect_type_errors = [
        "test",
        3.5,
        3.0
    ]
    expect_value_errors = [
        0,
        -1,
        100000
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            validation.check_number_of_random_points(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            validation.check_number_of_random_points(param)

def test_check_geometry_parameter():
    """Test the check_geometry_parameter function of the validation module.
    """
    valid_params = [
        2.0,
        -2.5,
        3,
        0,
        350
    ]
    expect_type_errors = [
        "test",
        "3.4",
        "3",
        (1, 2),
        [1, 2]
    ]
    expect_value_errors = [
        float("nan"),
        float("inf"),
        float("-inf")
    ]
    for param in valid_params:
        assert isinstance(validation.check_geometry_parameter(param), float)
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            validation.check_geometry_parameter(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            validation.check_geometry_parameter(param)

def test_check_radius():
    """Test the check_radius function of the validation module.
    """
    valid_params = [
        2.0,
        3,
        350
    ]
    expect_type_errors = [
        "test",
        "3.4",
        "3",
        (1, 2),
        [1, 2]
    ]
    expect_value_errors = [
        float("nan"),
        float("inf"),
        float("-inf"),
        0,
        0.0,
        -2.5
    ]
    for param in valid_params:
        assert isinstance(validation.check_radius(param), float)
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            validation.check_radius(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            validation.check_radius(param)

def test_check_vector():
    """Test the check_vector function of the validation module.
    """
    valid_params = [
        (1, 2, 3),
        (0, 0, 0),
        (1.0, 0.5, 10988),
        (-4.5, 0, 7.54)
    ]
    expect_type_errors = [
        "test",
        3,
        4.5,
        [1, 2, 3],
        ("4", 5, 6)
    ]
    expect_value_errors = [
        (1, 2, 3, 4),
        (1, 2),
        (float("nan"), 2, 3),
        (float("inf"), 2, 3),
        (float("-inf"), 2, 3)
    ]
    for param in valid_params:
        result = validation.check_vector(param)
        assert isinstance(result, tuple) and len(result) == 3
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            validation.check_vector(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            validation.check_vector(param)

def test_check_direction_vector():
    """Test the check_direction_vector function of the validation module.
    """
    valid_params = [
        (1, 2, 3),
        (0.52, 0.52, 0.52),
        (-0.52, 0.52, 0.52),
        (-4.5, 0, 7.54),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
    ]
    expect_type_errors = [
        "test",
        3,
        4.5,
        [1, 2, 3],
        ("4", 5, 6)
    ]
    expect_value_errors = [
        (1, 2, 3, 4),
        (1, 2),
        (float("nan"), 2, 3),
        (float("inf"), 2, 3),
        (float("-inf"), 2, 3),
        (0.51, 0.51, 0.51),
        (-0.51, 0.51, 0.51)
    ]
    for param in valid_params:
        result = validation.check_direction_vector(param)
        assert isinstance(result, tuple) and len(result) == 3
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            validation.check_direction_vector(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            validation.check_direction_vector(param)

def test_check_quaternion():
    """Test the check_quaternion function of the validation module
    """
    valid_params = [
        (1, 2, 3, 4),
        (0, 0, 0, 0),
        (-1, -5, 0, 3.4),
        (1.0, 1.5, -7.4, 3)
    ]
    expect_type_errors = [
        "test",
        3,
        4.5,
        [1, 2, 3, 4],
        ("4", 5, 6, 2)
    ]
    expect_value_errors = [
        (1, 2, 3, 4, 5),
        (1, 2, 3),
        (float("nan"), 2, 3, 4),
        (float("inf"), 2, 3, 4),
        (float("-inf"), 2, 3, 4)
    ]
    for param in valid_params:
        result = validation.check_quaternion(param)
        assert isinstance(result, tuple) and len(result) == 4
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            validation.check_quaternion(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            validation.check_quaternion(param)
