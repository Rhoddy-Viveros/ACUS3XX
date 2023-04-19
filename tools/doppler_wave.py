import numpy as np
from tools.doppler import Doppler
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

class Wave:
    def __init__(self, x: float, y: float):
        self.r: float = 0
        self.x = x
        self.y = y
        self.wave = plt.Circle((self.x, self.y), self.r,
                               facecolor='blue', edgecolor='k')

    def update(self, r: float):
        self.r = r
        self.wave = plt.Circle((self.x, self.y), r,
                               facecolor='none', edgecolor='k')


def generateAudio(frequencies: np.ndarray, sample_rate=44100):
    t = np.linspace(0., 1., sample_rate)
    amplitude = np.iinfo(np.int16).max
    data = np.array([])
    for freq in frequencies:
        data = np.append(data, amplitude*np.sin(2.*np.pi*freq*t))
    write("doppler_effect.wav", sample_rate, data.astype(np.int16))
