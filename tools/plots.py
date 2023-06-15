import matplotlib.pyplot as plt
import numpy as np
import torch
import librosa



def plot_spectrogram(specgram,hop_length,fs, title=None, ylabel="freq_bin"):
    
    fig, axs = plt.subplots(1, 1,figsize=(9,6))
    axs.set_title(title or "Spectrogram (db)")
    axs.set_ylabel(ylabel)
    axs.set_xlabel("time")
    frames = np.linspace(0,specgram.shape[1],8)
    hz = np.linspace(0,fs//2,8)
    hzpos = np.linspace(0,specgram.shape[0],8)
    time = np.around(frames*hop_length/fs,0)
    im = axs.imshow(librosa.power_to_db(specgram), origin="lower", aspect="auto")
    axs.set_xticks(frames)
    axs.set_xticklabels(time)
    axs.set_yticks(hzpos)
    axs.set_yticklabels(hz)
    fig.colorbar(im, ax=axs)
    plt.show(block=False)

def plot_pitch(waveform, sr, pitch):
    figure, axis = plt.subplots(1, 1,figsize=(7,5))
    axis.set_title("Pitch Feature")
    axis.grid(True)

    end_time = waveform.shape[1] / sr
    time_axis = torch.linspace(0, end_time, waveform.shape[1])
    axis.plot(time_axis, waveform[0], linewidth=1, color="gray", alpha=0.3)

    axis2 = axis.twinx()
    time_axis = torch.linspace(0, end_time, pitch.shape[1])
    axis2.plot(time_axis, pitch[0], linewidth=2, label="Pitch", color="green")

    axis2.legend(loc=0)
    plt.show(block=False)