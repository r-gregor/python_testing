import matplotlib.pyplot as plt
import numpy as np

'''
### PLOT-1
Fs = 4000
f = 5
sample = 4000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, y)
plt.xlabel('voltage(V)')
plt.ylabel('sample(n)')
plt.show()
'''

### PLOT-2
fs = 100 # sample rate 
f = 2 # the frequency of the signal

x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = [ np.sin(2*np.pi*f * (i/fs)) for i in np.arange(fs)]

# showing the exact location of the smaples
plt.stem(x,y, 'r', )
plt.plot(x,y)
plt.show()

