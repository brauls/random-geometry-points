import sys
import os
import math
import pytest

PROJ_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_PATH + '/../')

import random_geometry_points.vector_math as vector_math

def test_calc_magnitude():
    """Test the calc_magnitude function of the vector_math module.
    """
    expect_type_errors = [
        ("1", 2, 3),
        "test",
        5.4
    ]
    expect_value_errors = [
        (1, 2),
        (1, 2, 3, 4)
    ]
    expected_magnitudes = [
        ((1, 1, 1), math.sqrt(3)),
        ((0, 0, 0), 0),
        ((1.5, 2.3, -5.4), math.sqrt(36.7))
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.calc_magnitude(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.calc_magnitude(param)
    for param in expected_magnitudes:
        assert math.isclose(vector_math.calc_magnitude(param[0]), param[1], abs_tol=0.000001)

def test_calc_dot_product():
    """Test the calc_dot_product function of the vector_math module.
    """
    expect_type_errors = [
        (("1", 4, 5), (1, 2, 3)),
        ((1, 3, 5.5), ("test", 5, 4)),
        (4, (1, 2, 3)),
        ((1, 0, 0), "test")
    ]
    expect_value_errors = [
        ((1, 2), (1, 2, 3)),
        ((1, 2, 3), (1, 2, 3, 4))
    ]
    expected_dot_products = [
        ((1, 0, 0), (3, 4, 6), 3)
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.calc_dot_product(param[0], param[1])
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.calc_dot_product(param[0], param[1])
    for param in expected_dot_products:
        assert math.isclose(vector_math.calc_dot_product(param[0], param[1]),
                            param[2], abs_tol=0.000001)

def test_calc_cross_product():
    """Test the calc_cross_product function of the vector_math module.
    """
    expect_type_errors = [
        (("1", 4, 5), (1, 2, 3)),
        ((1, 3, 5.5), ("test", 5, 4)),
        (4, (1, 2, 3)),
        ((1, 0, 0), "test")
    ]
    expect_value_errors = [
        ((1, 2), (1, 2, 3)),
        ((1, 2, 3), (1, 2, 3, 4))
    ]
    expected_cross_products = [
        ((1.0, 0, 0), (0, 1, 0), (0, 0, 1)),
        ((3.5, 1, -4), (3, -5, 2), (-18, -19, -20.5)),
        ((0, 0, 1), (0, 3, 4), (-3, 0, 0))
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.calc_dot_product(param[0], param[1])
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.calc_dot_product(param[0], param[1])
    for param in expected_cross_products:
        actual_cross_product = vector_math.calc_cross_product(param[0], param[1])
        for elem_actual, elem_expected in zip(actual_cross_product, param[2]):
            assert math.isclose(elem_actual, elem_expected, abs_tol=0.000001)

def test_normalize_vector():
    """Test the normalize_vector function of the vector_math module.
    """
    expect_type_errors = [
        ("4", 4, 5),
        4,
        "test"
    ]
    expect_value_errors = [
        (1, 2),
        (1, 2, 3, 4),
        (0, 0, 0),
        (0.0, 0.0, 0.0)
    ]
    expected_normalized_vectors = [
        ((4, 0, 0), (1, 0, 0)),
        ((-4, 0, 0), (-1, 0, 0)),
        ((3, 2, 1), (0.80178372573, 0.53452248382, 0.26726124191)),
        ((-5, 3, 10), (-0.43193421279, 0.25916052767, 0.86386842558)),
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.normalize_vector(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.normalize_vector(param)
    for param in expected_normalized_vectors:
        actual_normal_vector = vector_math.normalize_vector(param[0])
        for elem_actual, elem_expected in zip(actual_normal_vector, param[1]):
            assert math.isclose(elem_actual, elem_expected, abs_tol=0.000001)

def test_calc_perpendicular_vector():
    """Test the calc_perpendicular_vector function of the vector_math module.
    """
    expect_type_errors = [
        ("1", 2, 3),
        "test",
        4
    ]
    expect_value_errors = [
        (1, 2),
        (1, 2, 3, 4),
        (0, 0, 0),
        (0.0, 0.0, 0.0)
    ]
    expected_perpendicular_vectors = [
        ((1, 0, 0), (0, 1, 0)),
        ((0, 1, 0), (-1, 0, 0)),
        ((0, 0, 1), (1, 0, 0)),
        ((3.5, 7.0, 2), (-7, 3.5, 0)),
        ((-5, -1, 0), (1, -5, 0)),
        ((1.5, 6, -4), (0, 4, 6))
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.calc_perpendicular_vector(param)
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.calc_perpendicular_vector(param)
    for param in expected_perpendicular_vectors:
        actual_perpendicular_vector = vector_math.calc_perpendicular_vector(param[0])
        for elem_actual, elem_expected in zip(actual_perpendicular_vector, param[1]):
            assert math.isclose(elem_actual, elem_expected, abs_tol=0.000001)

def test_get_as_rotation_quaternion():
    """Test the get_as_rotation_quaternion function of the vector_math module.
    """
    expect_type_errors = [
        ("test", 2.1),
        ((1.0, 5, "test"), 2.1),
        ((1, 2, 3), "test")
    ]
    expect_value_errors = [
        ((1, 2), 2.1),
        ((1, 2, 3, 4), 2.1),
        ((1, 2, 3), float("inf")),
        ((1, 2, 3), float("nan")),
        ((0, 0, 0), 2.1),
        ((0.0, 0.0, 0.0), 2.1)
    ]
    expected_rotation_quaternions = [
        ((1, 0, 0), 0.5, (math.cos(0.25), math.sin(0.25), 0, 0)),
        ((0, 2.5, 0), -2.5, (math.cos(-1.25), 0, math.sin(-1.25), 0)),
        ((-2, 2, 5), 10, (math.cos(5), math.sin(5) * -2 / math.sqrt(33),
                          math.sin(5) * 2 / math.sqrt(33), math.sin(5) * 5 / math.sqrt(33)))
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.get_as_rotation_quaternion(param[0], param[1])
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.get_as_rotation_quaternion(param[0], param[1])
    for param in expected_rotation_quaternions:
        actual_rotation_quaternion = vector_math.get_as_rotation_quaternion(param[0], param[1])
        for elem_actual, elem_expected in zip(actual_rotation_quaternion, param[2]):
            assert math.isclose(elem_actual, elem_expected, abs_tol=0.000001)

def test_rotate_vector():
    """Test the rotate_vector function of vector_math module.
    """
    expect_type_errors = [
        ("test", (1, 2, 3), 5),
        ((1, 2, 3), "test", 5),
        ((1, 2, 3), (1, 0, 0), "test"),
        (("test", 2, 3), (1, 0, 0), 5),
        ((1, 2, 3), ("test", 0, 0), 5)
    ]
    expect_value_errors = [
        ((1, 2), (1, 0, 0), 5),
        ((1, 2, 3, 4), (1, 0, 0), 5),
        ((1, 2, 3), (1, 0), 5),
        ((1, 2, 3), (1, 0, 0, 0), 5),
        ((1, 2, 3), (1, 0, 0), float("inf")),
        ((1, 2, 3), (1, 0, 0), float("nan")),
        ((float("inf"), 2, 3), (1, 0, 0), 5),
        ((float("nan"), 2, 3), (1, 0, 0), 5),
        ((1, 2, 3), (float("inf"), 0, 0), 5),
        ((1, 2, 3), (float("nan"), 0, 0), 5),
        ((1, 2, 3), (0, 0, 0), 5),
        ((1, 2, 3), (0.0, 0.0, 0.0), 5)
    ]
    expected_rotated_vector = [
        ((1, 2, 3), (1, 0, 0), math.pi, (1, -2, -3)),
        ((1, 2, 3.5), (1, 0, 0), 0.0, (1, 2, 3.5)),
        ((-1, 3, 3), (0, 1, 0), -math.pi, (1, 3, -3))
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.rotate_vector(param[0], param[1], param[2])
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.rotate_vector(param[0], param[1], param[2])
    for param in expected_rotated_vector:
        actual_rotated_vector = vector_math.rotate_vector(param[0], param[1], param[2])
        for elem_actual, elem_expected in zip(actual_rotated_vector, param[3]):
            assert math.isclose(elem_actual, elem_expected, abs_tol=0.000001)

def test_scale_vector():
    """Test the scale_vector function of vector_math module.
    """
    expect_type_errors = [
        ("test", 5),
        ((1, 2, "test"), 5),
        ((1, 2, 3), "test")
    ]
    expect_value_errors = [
        ((1, 2), 5),
        ((1, 2, 3, 4), 5),
        ((1, 2, 3), float("inf")),
        ((1, 2, 3), float("nan")),
        ((float("inf"), 2, 3), 5),
        ((float("nan"), 2, 3), 5)
    ]
    expected_scaled_vectors = [
        ((1, 2, 3), 5, (5, 10, 15)),
        ((-2.5, 1.4, 0), -2.5, (6.25, -3.5, 0)),
        ((0, 0, 0), 10, (0, 0, 0))
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.scale_vector(param[0], param[1])
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.scale_vector(param[0], param[1])
    for param in expected_scaled_vectors:
        actual_scaled_vector = vector_math.scale_vector(param[0], param[1])
        for elem_actual, elem_expected in zip(actual_scaled_vector, param[2]):
            assert math.isclose(elem_actual, elem_expected, abs_tol=0.000001)

def test_sum_vectors():
    """Test the sum_vectors function of vector_math module.
    """
    expect_type_errors = [
        ("test", (1, 2, 3)),
        ((1, 2, 3), "test"),
        (("test", 2, 3), (1, 2, 3)),
        ((1, 2, 3), ("test", 2, 3))
    ]
    expect_value_errors = [
        ((1, 2), (1, 2, 3)),
        ((1, 2, 3, 4), (1, 2, 3)),
        ((1, 2, 3), (1, 2)),
        ((1, 2, 3), (1, 2, 3, 4))
    ]
    expected_sum_vectors = [
        ((1, 2, 3), (1, 2, 3), (2, 4, 6)),
        ((-1, -5.5, 2), (3, 4, 2), (2, -1.5, 4)),
        ((0, 0, 0), (1, 2, 1), (1, 2, 1)),
        ((-1, 0, 0), (0, 0, 0), (-1, 0, 0)),
        ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.sum_vectors(param[0], param[1])
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.sum_vectors(param[0], param[1])
    for param in expected_sum_vectors:
        actual_sum_vector = vector_math.sum_vectors(param[0], param[1])
        for elem_actual, elem_expected in zip(actual_sum_vector, param[2]):
            assert math.isclose(elem_actual, elem_expected, abs_tol=0.000001)

def test_multiply_quaternions():
    """Test the multiply_quaternions function of vector_math module.
    """
    expect_type_errors = [
        ("test", (1, 2, 3, 4)),
        ((1, 2, 3, 4), "test"),
        (("test", 2, 3, 4), (1, 2, 3, 4)),
        ((1, 2, 3, 4), ("test", 2, 3, 4))
    ]
    expect_value_errors = [
        ((1, 2, 3), (1, 2, 3, 4)),
        ((1, 2, 3, 4, 5), (1, 2, 3, 4)),
        ((1, 2, 3, 4), (1, 2, 3)),
        ((1, 2, 3, 4), (1, 2, 3, 4, 5)),
        ((float("inf"), 2, 3, 4), (1, 2, 3, 4)),
        ((float("nan"), 2, 3, 4), (1, 2, 3, 4)),
        ((1, 2, 3, 4), (float("inf"), 2, 3, 4)),
        ((1, 2, 3, 4), (float("nan"), 2, 3, 4))
    ]
    expected_quaternions = [
        ((1, 2, 3, 4), (1, 2, 3, 4), (-28, 4, 6, 8)),
        ((-1.5, 1, 4, 2), (4.5, 1.2, 3, 2), (-23.95, 4.7, 13.9, 4.2)),
        ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))
    ]
    for param in expect_type_errors:
        with pytest.raises(TypeError):
            vector_math.multiply_quaternions(param[0], param[1])
    for param in expect_value_errors:
        with pytest.raises(ValueError):
            vector_math.multiply_quaternions(param[0], param[1])
    for param in expected_quaternions:
        actual_quaternion = vector_math.multiply_quaternions(param[0], param[1])
        for elem_actual, elem_expected in zip(actual_quaternion, param[2]):
            print(actual_quaternion)
            assert math.isclose(elem_actual, elem_expected, abs_tol=0.000001)
