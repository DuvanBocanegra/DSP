import numpy as num
import matplotlib.pyplot as matlab

x = num.arange(-10,10,0.1)
y = ((3*x)+2)
matlab.plot(x,y)
matlab.xlabel('x')
matlab.ylabel('y')
matlab.title('20230304 Exercise 002')
matlab.show()

