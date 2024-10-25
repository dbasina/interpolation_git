from scipy import interpolate
from scipy.interpolate import CubicSpline,make_interp_spline
import matplotlib.pyplot as plot
import numpy as np
import math

#create original function
x_orig = np.linspace(0,10, 1000)
y_orig = np.sin(x_orig**2)

#generate (x,y) scatter data
x_known = np.linspace(0,10, num = 10)
y_known = np.sin(x_known**2)

x_new = np.linspace(0,10, num = 50)
#linear-interpolation
y_linear = np.interp(x_new, x_known, y_known)

#Cublic spline generation
spline = CubicSpline(x_known, y_known)

y_cubic = spline(x_new)

#B-spline generation
# define Bspline
bspline = make_interp_spline(x_known, y_known, k = 5)
y_bspline = bspline(x_new)

plot.plot(x_known,y_known,linestyle = '',marker = 'o', color = 'blue', label = 'known data')
plot.plot(x_new,y_linear,marker = '', color = 'red', label = 'linear-interpolant')
plot.plot(x_new, y_cubic, color = 'green', label = 'cubic-interpolant')
plot.plot(x_new, y_bspline, color = 'orange', label = 'bSpline-interpolant')

plot.plot(x_orig,y_orig, color = 'black', label = 'sin(x^2)', alpha = 0.3)
plot.xlabel("x")
plot.ylabel("y = sin(x**2)")
plot.legend()
plot.title('Linear vs Cubic vs 5th order B-spline')

#Generate figure
fig = plot.gcf()
plot.draw()
fig.savefig("InterpolationJuxtaposed.png", dpi = 400)

#show
plot.show()