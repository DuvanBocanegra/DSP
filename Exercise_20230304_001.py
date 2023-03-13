import numpy as num
import matplotlib.pyplot as matlab

x = num.arange(-10,10,0.1)
y = num.sin(3*x)
matlab.plot(x,y)
matlab.xlabel('x')
matlab.ylabel('y')
matlab.title('Seno')
matlab.show()