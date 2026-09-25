# TODO:
# Intentionally trigger a broadcasting error
# Then fix it

error_raised = False
try:
    a = np.ones((3, 4))
    b = np.ones((5,))
    _ = a + b
except ValueError:
    error_raised = True

# TODO: fix with compatible shapes
a = np.ones((3, 4))
b = np.ones(    (4,))
fixed = a + b

check('broadcast_error_raised', bool(locals().get('error_raised', False)))
check('fixed_shape', isinstance(locals().get('fixed', None), np.ndarray) and locals().get('fixed').shape == (3, 4))
