import numpy as np
# TASK 1
if __name__ == "__main__":
    i_love_BTS = ['Намджун', 'Чонгук', 'Чингачгук',
                  'Гойко Митич', 'Джин', 'Юнги']
    from_left_to_right = np.array(i_love_BTS)
    floats = np.arange(2, 3, 0.1)
    hell = np.ones((6, 6))*6


# TASK 2
def matrix_multiplication(arr1, arr2):
    return arr1.dot(arr2)

# TASK 3
# далее считаем, что тоже имелось в виду скалярное произведение
def multiplication_check(arr_list):
    try:
        np.linalg.multi_dot(arr_list)
        return True
    except ValueError:
        return False

# TASK 4
def multiply_matrices(arr_list):
    return np.linalg.multi_dot(arr_list)


# TASK 5
def compute_2d_distance(point1, point2):
    return np.linalg.norm(point1 - point2)


# TASK 6
def compute_multidimensional_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

# TASK 7
def compute_pair_distances(matrix):
    return np.linalg.norm(matrix[:, None, :] - matrix[None, :, :], axis=-1)

