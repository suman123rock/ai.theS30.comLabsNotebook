# TODO:
# Create A (1000, 50) and b (50,)
# whenever +ve and -ve values and bell shaped values distributions are required, go for standard normal 1D creation then reshape to different 2D or 3D as per requirements
rng = np.random.default_rng(0)
a = rng.standard_normal(50_000)
A = a.reshape(1000, 50)
b = rng.standard_normal(50)
print(f"Shape printing of A is {A.shape}")
print(f"print b shape is {b.shape}")

# TODO:
# Add b to each row of A
# HINT:
# - No reshape required
A_plus_b = A + b
#print(f"checking A[0] + b is {A[0] + b}")
#print(f"checking A_plus_b addition is {A_plus_b[0]} ")
print(f"checking A[0]+b == A_plus_b[0] is {A[0] + b == A_plus_b[0]} ")

# TODO:
# Normalize each row of A
# HINT:
# - Axis matters
# - Keep dimensions in mind
row_norms = np.linalg.norm(A, axis = 1, keepdims = True)
print(f"print shape of row_norms is {row_norms.shape}")
A_norm = A / row_norms
print(f"print shape of A_norm is {A_norm.shape}")

check('A_shape', isinstance(locals().get('A', None), np.ndarray) and locals().get('A').shape == (1000, 50))
check('b_shape', isinstance(locals().get('b', None), np.ndarray) and locals().get('b').shape == (50,))
check('broadcast_shape', isinstance(locals().get('A_plus_b', None), np.ndarray) and locals().get('A_plus_b').shape == (1000, 50))
check('row_norm_shape', isinstance(locals().get('row_norms', None), np.ndarray) and locals().get('row_norms').shape in [(1000, 1), (1000,)])
check('A_norm_exists', isinstance(locals().get('A_norm', None), np.ndarray) and locals().get('A_norm').shape == (1000, 50))
check('rows_unit_norm', isinstance(locals().get('A_norm', None), np.ndarray) and np.allclose(np.linalg.norm(locals().get('A_norm'), axis=1), 1.0, atol=1e-5))
