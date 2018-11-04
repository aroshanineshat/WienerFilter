import numpy as np
import scipy as sp
import scipy.io.wavfile


def ReadWav(Filename):
    f, d = sp.io.wavfile.read(Filename)
    seconds = d.size / f
    t = np.linspace(0, seconds, d.size)
    return f, t, d

def GenerateSignal(F0, Fs, A, timeInsec):
    t = np.linspace(0, timeInsec, Fs * timeInsec)
    y = A * sp.sin(2*sp.pi * F0 * t)
    return t, y


def GenerateWhiteNoise(NumSamples, A):
    mean = 0
    std = 1
    return A * np.random.normal(mean, std, size=NumSamples)
