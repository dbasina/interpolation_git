import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

# Known data points
x = np.linspace(0,10,num = 10)
y = np.sin(x**2)

# Create the B-spline using make_interp_spline (cubic B-spline)
spline = make_interp_spline(x, y, bc_type='clamped')

# Extract the underlying BSpline object
bspline_obj = spline.tck  # tck is the tuple (knots, coefficients, degree)

# Get the knot vector, coefficients (control points), and degree
knots, coeffs, degree = bspline_obj

# Number of basis functions (control points)
n_basis = len(knots) - degree - 1

# Generate new x-values for plotting
x_new = np.linspace(min(x), max(x), 100)

# Plot the basis functions
plt.figure(figsize=(10, 6))
for i in range(n_basis):
    # Get the i-th basis function
    basis = BSpline.basis_element(knots[i:i + degree + 2], extrapolate=False)
    
    # Plot the basis function
    plt.plot(x_new, basis(x_new), label=f'Basis {i + 1}')

# Plot the original B-spline
plt.plot(x_new, spline(x_new), 'k--', label='B-spline', linewidth=2)
plt.plot(x,y,linestyle = '', marker = 'o', color = 'blue', label = 'known data y = sin(x**2)')

# Add labels and legend
plt.legend()
plt.title('Basis Functions generating B-spline')
plt.xlabel('x')
plt.ylabel('y')

#Generate figure
fig = plt.gcf()
plt.draw()
fig.savefig("basisFunctions.png", dpi = 400)

plt.show()
