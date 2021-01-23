import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(0, np.math.pi*2, 0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()