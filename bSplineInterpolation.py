from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plot
import numpy as np
import math
#create original function
x_orig = np.linspace(0,10, 1000)
y_orig = np.sin(x_orig**2)

#generate (x,y) scatter data
x_known = np.linspace(0,10, num = 10)
y_known = np.sin(x_known**2)

# define Bspline
bspline = make_interp_spline(x_known, y_known, k = 3)

x_new = np.linspace(0,10, num = 50)
y_new = bspline(x_new)
plot.plot(x_known,y_known,linestyle = '', marker = 'o', color = 'blue', label = 'known data')
plot.plot(x_new, y_new, linestyle = '', marker = 'x', color = 'orange', label = 'interpolant points')
plot.plot(x_new, y_new, marker = 'x', color = 'orange', label = 'bSpline-interpolant')
plot.plot(x_orig,y_orig, color = 'red', label = 'sin(x^2)', alpha = 0.3)

plot.xlabel("x")
plot.ylabel("y = sin(x**2)")
plot.legend()
plot.title('B-Spline Interpolation')

#Generate figure
fig = plot.gcf()
plot.draw()
fig.savefig("bSplineInterpolation.png", dpi = 400)

plot.show()