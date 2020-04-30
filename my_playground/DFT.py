import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (12,4)

N = 64
n = np.arange(0, N, 1)
L = N / 16
delay = 0
y = 0.5 * np.sin(2 * np.pi / N * L * (n - delay))

plt.figure(1)
plt.subplot(2,2,1)
plt.stem(y)

Y2 = np.fft.fft(y)

plt.subplot(2,2,2)
plt.stem(np.abs(Y2),use_line_collection=True)

plt.subplot(2,2,3)
plt.stem(np.imag(Y2),use_line_collection=True)

plt.show()