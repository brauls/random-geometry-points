"""A small set of simple vector manipulation/calculation functions.
"""

import math
from functools import reduce
from random_geometry_points.validation import check_vector, check_geometry_parameter, \
  check_direction_vector, check_quaternion

def calc_magnitude(vec):
    """Calculate the magnitude of a 3D vector.

    Args:
        vec (tuple (float, float, float)): The 3D vector whose magnitude shall be calculated

    Returns:
        float: The magnitude of the 3D vector
    """
    checked_vec = check_vector(vec)
    return math.sqrt(checked_vec[0]**2 + checked_vec[1]**2 + checked_vec[2]**2)

def calc_dot_product(vec1, vec2):
    """Calculate the dot product of two 3D vectors.

    Args:
        vec1 (tuple (float, float, float)): The first 3D vector
        vec2 (tuple (float, float, float)): The second 3D vector

    Returns:
        float: The dot product of the two 3D vectors
    """
    checked_vec1 = check_vector(vec1)
    checked_vec2 = check_vector(vec2)
    return (checked_vec1[0]*checked_vec2[0] + checked_vec1[1]*checked_vec2[1]
            + checked_vec1[2]*checked_vec2[2])

def calc_cross_product(vec1, vec2):
    """Calculate the cross product of two 3D vectors.

    Args:
        vec1 (tuple (float, float, float)): The first 3D vector
        vec2 (tuple (float, float, float)): The second 3D vector

    Returns:
        tuple (float, float, float): The cross product of the two 3D vectors
    """
    checked_vec1 = check_vector(vec1)
    checked_vec2 = check_vector(vec2)
    return (checked_vec1[1]*checked_vec2[2] - checked_vec1[2]*checked_vec2[1],
            checked_vec1[2]*checked_vec2[0] - checked_vec1[0]*checked_vec2[2],
            checked_vec1[0]*checked_vec2[1] - checked_vec1[1]*checked_vec2[0])

def normalize_vector(vec):
    """Normalize the input vector.

    Args:
        vec (tuple (float, float float)): The 3D vector to be normalized

    Returns:
        tuple (float, float, float): The normalized vector
    """
    magnitude = calc_magnitude(vec)
    if math.isclose(magnitude, 0.0, abs_tol=0.000001):
        raise ValueError("Inproper vector. Expected a magnitude greater than 0.")
    normalize = lambda v: v / magnitude
    return tuple([normalize(vec_elem) for vec_elem in vec])

def calc_perpendicular_vector(vec):
    """Calculate an arbitrary perpendicular vector.

    Args:
        vec (tuple (float, float float)): The 3D vector for which an arbitrary
          perpendicular vector shall be calculated

    Returns:
        tuple (float, float, float): The perpendicular vector
    """
    checked_vec = check_vector(vec)
    magnitude = calc_magnitude(checked_vec)
    if math.isclose(magnitude, 0.0, abs_tol=0.000001):
        raise ValueError("""Invalid vector. Expected a vector with
          a magnitude greater than zero""")
    if math.fabs(checked_vec[0]) < math.fabs(checked_vec[1]) and \
      math.fabs(checked_vec[0]) < math.fabs(checked_vec[2]):
        return calc_cross_product((1.0, 0.0, 0.0), checked_vec)
    elif math.fabs(checked_vec[1]) < math.fabs(checked_vec[2]):
        return calc_cross_product((0.0, 1.0, 0.0), checked_vec)
    return calc_cross_product((0.0, 0.0, 1.0), checked_vec)

def get_as_rotation_quaternion(axis, angle):
    """Convert an axis and an angle into a rotation quaternion.

    Args:
        axis (tuple (float, float, float)): A vector representing a rotation axis
        angle (float): The rotation angle (radiant) for a right-handed rotation

    Returns:
        tuple (float, float, float, float): The rotation quaternion defined as
          q = (w, qx, qy, qz)
    """
    checked_axis = normalize_vector(check_direction_vector(axis))
    checked_angle = check_geometry_parameter(angle)
    omega = 0.5 * checked_angle
    return (math.cos(omega),) + tuple([math.sin(omega) * vec_elem for vec_elem in checked_axis])

def rotate_vector(vec, axis, angle):
    """Rotate a vector around an axis by an angle (radiant).

    Args:
        vec (tuple (float, float, float)): The vector that shall be rotated
        axis (tuple (float, float, float)): The rotation axis
        angle (float): The rotation angle (radiant) for a right-handed rotation

    Returns:
        tuple (float, float, float): The rotated vector
    """
    (vec_x, vec_y, vec_z) = check_vector(vec)
    (quat_w, quat_x, quat_y, quat_z) = get_as_rotation_quaternion(axis, angle)
    # rotation of a vector p via a quaternion q is defined as: q * p * (q*)
    qpq = reduce(multiply_quaternions, [
        (0.0, vec_x, vec_y, vec_z),
        (quat_w, -quat_x, -quat_y, -quat_z)
    ], (quat_w, quat_x, quat_y, quat_z))
    return (qpq[1], qpq[2], qpq[3])

def scale_vector(vec, scale):
    """Multiply each vector element with the scale factor.

    Args:
        vec (tuple (float, float, float)): The vector that shall be scaled
        scale (float): The scale factor

    Returns:
        tuple (float, float, float): The scaled vector
    """
    checked_vec = check_vector(vec)
    checked_scale = check_geometry_parameter(scale)
    return tuple([checked_scale * vec_elem for vec_elem in checked_vec])

def sum_vectors(vec1, vec2):
    """Calculate the sum of two vectors.

    Args:
        vec1 (tuple (float, float, float)): The first 3D vector
        vec2 (tuple (float, float, float)): The second 3D vector

    Returns:
        tuple (float, float, float): The sum of both vectors
    """
    checked_vec1 = check_vector(vec1)
    checked_vec2 = check_vector(vec2)
    return (checked_vec1[0]+checked_vec2[0], checked_vec1[1]+checked_vec2[1],
            checked_vec1[2]+checked_vec2[2])

def multiply_quaternions(quat1, quat2):
    """Multiply two quaternions.

    Args:
        quat1 (tuple (float, float, float, float)): The first quaternion
        quat2 (tuple (float, float, float, float)): The second quaternion

    Returns:
        tuple (float, float, float, float): The new quaternion created by doing q1 * q2
    """
    (qw1, qx1, qy1, qz1) = check_quaternion(quat1)
    (qw2, qx2, qy2, qz2) = check_quaternion(quat2)
    qw3 = qw1 * qw2 - calc_dot_product((qx1, qy1, qz1), (qx2, qy2, qz2))
    qxyz3 = reduce(sum_vectors, [
        calc_cross_product((qx1, qy1, qz1), (qx2, qy2, qz2)),
        scale_vector((qx2, qy2, qz2), qw1),
        scale_vector((qx1, qy1, qz1), qw2)
    ], (0, 0, 0))
    return (qw3,) + qxyz3
