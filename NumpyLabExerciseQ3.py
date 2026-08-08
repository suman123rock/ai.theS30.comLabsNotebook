# TODO:
# Create a 2D array and slice every alternate row
# HINT:
# - Use slicing, not fancy indexing
A = np.arange(20).reshape(5, 4)
print(f"print A with 2d{A}")
A_slice = A[ ::2, :]
print(f"print A_slice {A_slice}")

# TODO:
# Modify A_slice and observe A
A_slice[0, 0] = -999
print(f"After modifying A_slice observe  A {A}")
print(f"After modifying A_slice observe A_slice {A_slice}")
print(f"view_shares_memory of A and A_slice {np.shares_memory(A, A_slice)}")

# TODO:
# Use fancy indexing and verify it creates a copy
A_fancy = A[[0,2,4], :]
A_fancy[0, 0] = 123456
print(f"After modifying A_fancy observe  A_fancy {A_fancy}")
print(f"After modifying A_fancy observe A {A}")
print(f"view_shares_memory of A and A_fancy {np.shares_memory(A, A_fancy)}")

check('slice_shape', A_slice.ndim == 2)
check('view_updates_parent', A[0, 0] == -999)
check('view_shares_memory', np.shares_memory(A, A_slice))
check('copy_shape', A_fancy.ndim == 2)
check('fancy_index_copy_no_parent_change', A[0, 0] != 123456)
