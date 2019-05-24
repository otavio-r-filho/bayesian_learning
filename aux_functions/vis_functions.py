import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.fftpack import fft, fftfreq

def plot_random(X, Y, xcol, title_col, nplots = 9, ncols = 3, sample_rate = 360):
    '''
    Function to random plot signals
    '''
    rnd_samples = np.random.choice(X.columns, nplots)
    
    fig, axes = plt.subplots(nrows=np.int32(np.ceil(nplots/ncols)),
                             ncols = ncols,
                             figsize = (ncols * 5, np.int32(np.ceil(nplots/ncols) * 4)))
    axes = axes.flatten()

    for idx, ax in zip(rnd_samples, axes):
        yvals = X.loc[:, idx]
        xvals = np.arange(yvals.shape[0]) * (1/sample_rate)
        ax.plot(xvals, yvals)
#         ax.legend().remove()
#         X.plot(x = xcol, y = idx, kind = "line", ax = ax, legend = False)
        ax.set_title("".join([str(idx),": ", Y.loc[idx, title_col]]))
        ax.set_xlabel("time(s)")

    plt.subplots_adjust(hspace=0.5)
    
    return fig

def plot_fanalysis(X, Y, xcol, title_col, nplots = 1, sample_rate = 360):
    '''
    Function to plot the signal, FFT and spectrogram in the same line
    '''
    rnd_samples = np.random.choice(X.columns, nplots)
    
    fig, axes = plt.subplots(nrows=nplots,
                             ncols = 3,
                             figsize = (15, nplots * 4))
    
    for idx, ax in zip(rnd_samples, axes):
        raw_signal = X.loc[:, idx]
        signal_fft = fft(raw_signal, n = 187)
        signal_freq = fftfreq(signal_fft.shape[-1])
        signal_time = np.arange(raw_signal.shape[0]) * (1/sample_rate)
        
        ax[0].plot(signal_time, raw_signal)
        ax[0].set_title("".join([str(idx),": ", Y.loc[idx, title_col], " Wave"]))
        ax[0].set_xlabel("time(s)")
        
        ax[1].plot(signal_freq, signal_fft.real, signal_freq, signal_fft.imag)
        ax[1].set_title("".join([Y.loc[idx, title_col], " Wave FFT"]))
        ax[1].set_xlabel("norm. freq.")
        
        ax[2].specgram(raw_signal, Fs = sample_rate)
        ax[2].set_title("".join([Y.loc[idx, title_col], " Wave Spectrogram"]))
        ax[2].set_xlabel("time(s)")
    
    plt.subplots_adjust(hspace=0.5)
    return fig