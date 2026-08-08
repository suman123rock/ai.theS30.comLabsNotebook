# TODO:
# Create a 1D array with values 0 to 99 (no loops)
# HINT:
# - Use np.arange
arr_1d = ...
print(type(arr_1d))

arr_1d = np.arange(0, 100)
print(arr_1d)
print(arr_1d.shape)
print(arr_1d.ndim)
print(arr_1d.size)
print(arr_1d[0])
print(arr_1d[-1])

# TODO:
# Reshape arr_1d into a (10, 10) array
# HINT:
# - reshape does NOT copy data
arr_2d = arr_1d.reshape((10,10))
print(f"Print arr_2d{arr_2d}")
print(f"print shape of arr_2d is {arr_2d.shape}")
print(f"print ndim of arr_2d is {arr_2d.ndim}")
print(f"print size of arr_2d is {arr_2d.size}")
print(f"print retrieval element of {arr_2d[0][0]}")
print(f"print the retrieval element of {arr_2d[0][1]}")

# TODO:
# Create a 3D array of shape (4, 5, 3)
# HINT:
# - Total elements must match
arr_3d = np.arange(4*5*3).reshape(4, 5, 3)
print(f"Print arr_3d{arr_3d}")
print(f"print shape of arr_3d is {arr_3d.shape}")
print(f"print ndim of arr_3d is {arr_3d.ndim}")
print(f"print size of arr_3d is {arr_3d.size}")
print(f"print retrieval element of {arr_3d[0][0][0]}")
print(f"print the retrieval element of {arr_3d[0][1][0]}")

check('arr_1d_shape', isinstance(arr_1d, np.ndarray) and arr_1d.shape == (100,))
check('arr_2d_shape', isinstance(arr_2d, np.ndarray) and arr_2d.shape == (10, 10))
check('arr_3d_shape', isinstance(arr_3d, np.ndarray) and arr_3d.shape == (4, 5, 3))
check('arr_2d_is_view_like', np.shares_memory(arr_1d, arr_2d))
