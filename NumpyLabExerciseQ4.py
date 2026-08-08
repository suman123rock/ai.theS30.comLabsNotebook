# TODO:
# Create random array of size 1000
rng = np.random.default_rng(0)
print(f"print rng is {rng}")
X = rng.standard_normal(1000)
print(f"Random integer generator for array of size 1000  from low = 0 and high = 100 is {X}")
print(f"Check the type of X {type(X)}")

# TODO:
# Extract values greater than mean
# HINT:
# - Mean first
# - Boolean mask
x_mean = X.sum()/X.size
print(f"Calculating X_mean is {x_mean}")
X_gt_mean = X > x_mean
print(f"Print type of  greater than mean is {(type(X_gt_mean))}")
values_gt_mean = X[X_gt_mean]
print(f"Extract values greater than mean is {values_gt_mean}")

# TODO:
# Replace negative values with 0 (no loops)
negative_mask = X < 0
print(f"print negative mask is {negative_mask}")
print(f"print the type of negative_mask is {type(negative_mask)}")
X_clipped = X.copy()
X_clipped[negative_mask] = 0
print(f"print X_clipped is {X_clipped}")

check('x_shape', X.shape == (1000,))
check('mask_nonempty', X_gt_mean.size > 0)
check('gt_mean_condition', np.all(X_gt_mean > x_mean))
check('clip_non_negative', np.all(X_clipped >= 0))
