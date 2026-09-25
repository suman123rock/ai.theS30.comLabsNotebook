# TODO:
# Create random array of size 1000
X = np.random.randn(1000)

# TODO:
# Extract values greater than mean
# HINT:
# - Mean first
# - Boolean mask
x_mean = X.sum() / X.size
X_gt_mean =  X > x_mean

# TODO:
# Replace negative values with 0 (no loops)
negative_mask = X < 0
X_clipped = X[negative_mask]
X_clipped = 0

check('x_shape', X.shape == (1000,))
check('mask_nonempty', X_gt_mean.size > 0)
check('gt_mean_condition', np.all(X_gt_mean > x_mean))
check('clip_non_negative', np.all(X_clipped >= 0))
