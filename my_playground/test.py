import numpy as np

N = 512
n = np.arange(N)
w = 1 - np.cos(2 * np.pi * n / (N - 1))

target=511
result = np.dot(w,w)
print(np.sum(result))

c=np.sqrt(target/np.sum(w**2))
w=c*w
print(np.sum(w**2))
