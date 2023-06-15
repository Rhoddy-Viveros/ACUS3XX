from matplotlib import pyplot as plt
import matplotlib.patches as patches
from scipy.io.wavfile import write as wavwrite
import numpy as np

def plot_freq_res(twotube, label, glo, hpf):
	plt.xlabel('Hz')
	plt.ylabel('dB')
	plt.title(label)
	amp0, freq=glo.H0(freq_high=5000, Band_num=256)
	amp1, freq=twotube.H0(freq_high=5000, Band_num=256)
	amp2, freq=hpf.H0(freq_high=5000, Band_num=256)
	plt.plot(freq, (amp0+amp1+amp2))

def add_draw_patch(ax1, twotube):
	ax1.add_patch( patches.Rectangle((0, -0.5* twotube.A1), twotube.L1, twotube.A1, hatch='/', fill=False))
	ax1.add_patch( patches.Rectangle((twotube.L1, -0.5* twotube.A2), twotube.L2, twotube.A2, hatch='/', fill=False))
	ax1.set_xlim([0, 20])
	ax1.set_ylim([-5, 5])

def plot_waveform(twotube, label, glo, hpf):
	# you can get longer input source to set bigger repeat_num 
	yg_repeat=glo.make_N_repeat(repeat_num=5) # input source of two tube model
	y2tm=twotube.process(yg_repeat)
	yout=hpf.iir1(y2tm)
	plt.xlabel('mSec')
	plt.ylabel('level')
	plt.title('Waveform')
	plt.plot( (np.arange(len(yout)) * 1000.0 / glo.sr) , yout)
	return yout

def save_wav( yout, wav_path, sampling_rate=48000):
	wavwrite( wav_path, sampling_rate, ( yout * 2 ** 15).astype(np.int16))
	print ('save ', wav_path) 