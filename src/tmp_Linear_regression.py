import numpy as np

# -------------------------
# Measured data (raw, temperature_c)
# -------------------------
data = [
    (768, 24.9),
    (757, 24.3),
    (748, 23.8),
    (745, 23.6),
    (743, 23.5),
    (739, 23.3),
    (738, 23.2),
    (734, 23.0),
    (732, 22.9),
    (730, 22.8),
    (729, 22.7),
    (682, 20.1),
]

# -------------------------
# Convert to arrays
# -------------------------
x = np.array([d[0] for d in data], dtype=float)
y = np.array([d[1] for d in data], dtype=float)

# -------------------------
# Least squares method (Linear regression)
# y = a*x + b
# -------------------------
A = np.vstack([x, np.ones(len(x))]).T
a, b = np.linalg.lstsq(A, y, rcond=None)[0]

# -------------------------
# Display results
# -------------------------
print("=== Linear Regression Result ===")
print(f"y = {a:.6f} * x + {b:.6f}")

# -------------------------
# Accuracy check (Residuals)
# -------------------------
y_pred = a * x + b
error = y - y_pred

print("\n=== Error ===")
print(f"MAE: {np.mean(np.abs(error)):.4f}")
print(f"Max Error: {np.max(np.abs(error)):.4f}")
