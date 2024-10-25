from scipy import interpolate
import matplotlib.pyplot as plot
import numpy as np
import math

#create original function
x_orig = np.linspace(0,10, 1000)
y_orig = np.sin(x_orig**2)

#generate (x,y) scatter data
x_known = np.linspace(0,10, num = 10)
y_known = np.sin(x_known**2)

x_interp = np.linspace(0,10, num = 50)
y_interp = np.interp(x_interp, x_known, y_known)

plot.plot(x_known,y_known,linestyle = '', marker = 'o', color = 'blue', label = 'known data')
plot.plot(x_interp, y_interp, linestyle = '', marker = 'x', color = 'orange', label = 'interpolant points')
plot.plot(x_interp,y_interp,marker = '', color = 'orange', label = 'linear-interpolant')
plot.plot(x_orig,y_orig, color = 'red', label = 'sin(x^2)', alpha = 0.3)
plot.xlabel("x")
plot.ylabel("y = sin(x**2)")
plot.legend()
plot.title('Linear Interpolation')

#Generate figure
fig = plot.gcf()
plot.draw()
fig.savefig("linearInterpolation.png", dpi = 400)

#show
plot.show()