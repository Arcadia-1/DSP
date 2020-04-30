import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def plot_response(fs, w, h, title):
    "Utility function to plot response functions"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(0.5 * fs * w / np.pi, 20 * np.log10(np.abs(h)))
    # ax.set_ylim(-40, 5)
    # ax.set_xlim(0, 0.5 * fs)
    ax.grid(True)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Gain (dB)")
    ax.set_title(title)
    plt.show()


fs = 44100
numtaps = 512
f_pass = fs / 2 * 1 / 128
f_stop = fs / 2 * 1 / 32

bands = [0, f_pass, f_stop, 0.5 * fs]
desired = [2, 0]
out = signal.remez(numtaps, bands, desired, fs=fs)

# w, h = signal.freqz(out, [1], worN=2000)
# plot_response(fs, w, h, "Low-pass Filter")


f = 0
g = 0
L=10
x=np.arange(L)
y=np.arange(L)
for n in range(0, L - 1):
    y[n] = x[n] + f
    g = -f
    f = -x[n] + 0.5 * y[n] + g
plt.plot(f)
plt.show()