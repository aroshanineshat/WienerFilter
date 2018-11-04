import numpy as np
import scipy as sp
import scipy.signal
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift
import SgnlGen


def program_(Filename):
    #t, d = SgnlGen.GenerateSignal(1e0, 10e1, 1, 1)
    #rate, data =  SgnlGen.ReadWav("audio-only.wav")
    #d = SgnlGen.GenerateWhiteNoise(10, 2)
    f, t, d = SgnlGen.ReadWav("audio-only.wav")
    n = SgnlGen.GenerateWhiteNoise(d.size, 2)
    x = (d+n)
    scipy.io.wavfile.write("audio-plusNoise.wav", f, x)

    Row = np.zeros((1, d.size))
    Phixd = np.zeros((1, d.size))
    Rxx = np.zeros((d.size, d.size))

    for i in np.arange (0, d.size, 1):
        Row[0, i] = np.correlate(x, np.roll(x, -i))
        Phixd[0,i] = np.correlate (np.roll(x, i), d)
        #Row[0,i] = np.correlate (x, shift(x, -i, cval=0))
        #Phixd[0,i] = np.correlate (shift(x, i, cval=0), d)
    for i in np.arange (0, d.size, 1):
        Rxx[i, :] = np.roll(Row, i)
        for index, j in enumerate(np.arange(1, i+1, 1)):
            Rxx[i, index] = Row[0, i + 1 - j]

    if (0):
        plt.imshow(Rxx, interpolation='nearest')
        plt.colorbar()
        plt.show()
    Wo = -1 * np.linalg.solve(Rxx, Phixd.T)
    e = x - d
    y = np.convolve( x, Wo.T[0,:], mode='same')
    #We = np.multiply(Wo.T, x)
    return t, x , y
    if (0):
        plt.close()
        plt.clf()
        plt.plot(t, x)
        #plt.plot(t, We[0,:])
        plt.plot(t, y)
        flename = "Pictures/Figure" + str(Filename) + ".png"
        plt.savefig(flename, filetype="png")
        #plt.show()


if __name__ == "__main__":
    i = 0
    total_number = 1.0
    t, x, y = program_(i)
    Output = y / total_number
    while i < total_number:
        plt.close()
        plt.clf()
        plt.ylim(top=1.3, bottom=-1.3)
        plt.plot(t, x)
        # plt.plot(t, We[0,:])
        plt.plot(t, Output)
        flename = "P2/Figure" + str(i) + ".png"
        plt.savefig(flename, filetype="png")
        print (str((i / total_number) * 100 ) + "%")
        i = i +1
        t, x, y = program_(i)
        Output = Output +  y / total_number
