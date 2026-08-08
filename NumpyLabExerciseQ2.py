# TODO:
# Create two arrays with same values but different dtypes
arr_int = np.array([1,2,3], dtype=np.int64)
arr_float = np.array([1,2,3], dtype=np.float64)
print(f"print array_int{arr_int} with data type {arr_int.dtype}")
print(f"print array float{arr_float} with data data type  {arr_float.dtype}")

# TODO:
# Compare memory usage
# HINT:
# - Use .nbytes
print(f"arr_int memory usage = {arr_int.nbytes}")
print(f"arr_float memory usage = {arr_float.nbytes}")
print(f"comparing memory usage {arr_int.nbytes == arr_float.nbytes}")

check('same_shape', arr_int.shape == arr_float.shape)
check('dtype_int', np.issubdtype(arr_int.dtype, np.integer))
check('dtype_float', np.issubdtype(arr_float.dtype, np.floating))
check('float_uses_more_bytes', arr_float.nbytes >= arr_int.nbytes)
