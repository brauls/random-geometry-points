"""Validation functions to check the types and values of geometry parameters.
"""

import math
from functools import reduce

def check_number_of_random_points(num_points):
    """Check the number of random points to create for a geometry.
    The number of points must be of type int and its value must be
    greater than zero and less than 100000.

    Args:
        num_points (any): The parameter whose type and value shall be checked

    Raises:
        TypeError: Signals that param is not of type int
        ValueError: Signals that param's value is either less/equal 0.0 or greater/equal 10000
    """
    if not isinstance(num_points, int):
        raise TypeError("Inproper type for number of points. Expected int.")
    elif num_points <= 0:
        raise ValueError("""Inproper value for number of points.
        Expected a value greater than zero""")
    elif num_points >= 100000:
        raise ValueError("""Inproper value for number of points.
        Expected a value less than 100000""")

def check_geometry_parameter(param):
    """Check the type of one geometry parameter to be float or int.

    Args:
        param (any): The parameter whose type and value shall be checked

    Raises:
        TypeError: Signals that param is neither of type int nor float
        ValueError: Signals that param's value is either Inf or NaN

    Returns:
        float: The checked parameter parsed to float
    """
    if isinstance(param, float):
        checked_param = param
    elif isinstance(param, int):
        checked_param = float(param)
    else:
        raise TypeError("Inproper parameter type. Expected float or int.")
    if math.isinf(checked_param) or math.isnan(checked_param):
        raise ValueError("Inproper parameter value. No inf or nan.")
    return checked_param

def check_radius(radius):
    """Check the type of the radius parameter to be float or int.
    Furthermore check that the radius value is greater than zero.

    Args:
        radius (any): The parameter whose type and value shall be checked

    Raises:
        TypeError: Signals that param is neither of type int nor float
        ValueError: Signals that param's value is Inf, NaN or less/equal 0.0

    Returns:
        float: The checked parameter parsed to float
    """
    param = check_geometry_parameter(radius)
    if param <= 0.0:
        raise ValueError("Inproper radius value. Expected a value greater than zero.")
    return param

def check_vector(vec):
    """Check the input vector elements' type and value.

    Args:
        vec (any): The 3D vector to be checked

    Raises:
        TypeError: Signals that the vector elements are neither of type int nor float
          or that the vector is not of type tuple
        ValueError: Signals that the value of at least one vector element is Inf, NaN
          or that the length of the vector is not 3

    Returns:
        tuple (float, float, float): The checked vector elements
    """
    if not isinstance(vec, tuple):
        raise TypeError("Inproper type for vector. Expected tuple.")
    elif len(vec) != 3:
        raise ValueError("Inproper vector length. Expected length 3.")
    for vec_elem in vec:
        check_geometry_parameter(vec_elem)
    return vec

def check_direction_vector(vec):
    """Check the input vector elements' type and value.

    Args:
        vec (any): The 3D vector to be checked

    Raises:
        TypeError: Signals that the vector elements are neither of type int nor float
        ValueError: Signals that the value of at least one vector element
          is Inf, NaN or the magnitude of the whole vector is less than 0.9

    Returns:
        tuple (float, float, float): The checked vector elements
    """
    check_vector(vec)
    update_magnitude = lambda acc, vec_elem: acc + vec_elem**2
    magnitude = math.sqrt(reduce(update_magnitude, vec, 0.0))
    if magnitude < 0.9:
        raise ValueError("""Inproper vector parameter.
          Expected the vector's magnitude to be at least 0.9.""")
    return vec

def check_quaternion(quat):
    """Check the input quaternion elements' type and value.

    Args:
        quat (any): The quaternion to be checked

    Raises:
        TypeError: Signals that the quaternion elements are neither of type int nor float
          or that the quaternion is not of type tuple
        ValueError: Signals that the value of at least one quaternion element is Inf, NaN
          or that the length of the quaternion is not 4

    Returns:
        tuple (float, float, float, float): The checked quaternion elements
    """
    if not isinstance(quat, tuple):
        raise TypeError("Inproper type for quaternion. Expected tuple.")
    elif len(quat) != 4:
        raise ValueError("Inproper quaternion length. Expected length 4.")
    for q_elem in quat:
        check_geometry_parameter(q_elem)
    return quat
