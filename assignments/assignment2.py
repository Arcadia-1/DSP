
from scipy import signal
import matplotlib.pyplot as plt


def prototype_filter():
    """ ASSIGNMENT 2

        Compute the prototype filter used in subband coding. The filter
        is a 512-point lowpass FIR h[n] with bandwidth pi/64 and stopband
        starting at pi/32

        You should use the remez routine (signal.remez()). See
        http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.remez.html
    """

    # Your code goes here
    fs = 44100
    numtaps = 512
    f_pass = fs / 2 * 1 / 128
    f_stop = fs / 2 * 1 / 32

    bands = [0, f_pass, f_stop, 0.5 * fs]
    desired = [2, 0]
    out = signal.remez(numtaps, bands, desired, fs=fs)

    return out
