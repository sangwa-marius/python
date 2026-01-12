import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(0,50,100)
x = np.cos(z)
y = np.sin(z)

y1 = np.cos(z+1)
x1 = np.cos(z+1)

fig = plt.figure()
ax = fig.add_subplot(111,projection ="3d")
ax.plot(x,y,z,color="green", label ="line 1" )
ax.plot(x1,y1,z,color="blue", label ="line 2" )
ax.legend()


plt.show()
