import numpy as np


def hanning_window(N):
    """Hanning window
    w[n] =  c/2 * (1 - \cos ((2 \pi n)/(N - 1)))
    """

    n = np.arange(N)
    w = 1 - np.cos(2 * np.pi * n / (N - 1))

    target = 511
    c = np.sqrt(target / np.sum(w ** 2))

    return c * w


def get_dB(x):
    dB = 20 * np.log10(x)
    dB[np.where(x == 0)[0]] = -100
    return dB


def scaled_fft_db(x):
    """ ASSIGNMENT 1:
        a) Compute a 512-point Hann window and use it to weigh the input data.
        
        
        b) Compute the DFT of the weighed input, take the magnitude in dBs and
        normalize so that the maximum value is 96dB.
        
        
        c) Return the first 257 values of the normalized spectrum

        Arguments:
        x: 512-point input buffer.

        Returns:
        first 257 points of the normalized spectrum, in dBs
    """

    N = len(x)

    # Window the input signal by a Hanning window
    w = hanning_window(N)
    y = np.multiply(x, w)

    # FFT, then normalize, then take the first 257 values
    Y = abs(np.fft.fft(y) / N)
    Y = Y[0 : (N // 2 + 1)]

    # Convert the magnitude to dBs, then rescale so that the maximum value is 96 dB
    Y = get_dB(Y)
    output = Y - max(Y) + 96

    return output
