import numpy as np
from scipy import ndimage

import matplotlib.mlab as mlab
import librosa
import pandas as pd
def fingerprint(file,file_path):
    data,sr=librosa.load(file_path)
    specgram, freqs, times = mlab.specgram(data, NFFT=4096, Fs=sr, noverlap=int(4096 / 2))
    specgram[specgram == 0]=1e-6
    extent = 0, np.amax(times), freqs[0], freqs[-1] #data coord of bounding box
    Z = 10.0 * np.log10(specgram)
    Z = np.flipud(Z)
    peaks_array = spectrogram_to_peaks(specgram, freqs, times)
    peaks_where = np.where(peaks_array)
    
    return peaks_where

#90% cutoff threshold to remove noise
def find_ninety_C_k(spec_gram):
    spec_gram = spec_gram[spec_gram != 0] #remove 0's
    specgram_flattened = spec_gram.flatten() #returns copy of orig
    specgram_sorted = np.sort(np.log(np.abs(specgram_flattened)))
    specgram_length = len(specgram_sorted)

    ninety_index = int(0.9 * specgram_length)
    ninety_C_k = specgram_sorted[ninety_index]
    return ninety_C_k


def spectrogram_to_peaks(specgram, freqs, times):
    fp = ndimage.generate_binary_structure(2,1)
    fp = ndimage.iterate_structure(fp, 20)
    background_threshold = find_ninety_C_k(specgram)
    peaks = ((specgram == ndimage.maximum_filter(specgram, footprint = fp) ) & (specgram > background_threshold))
    return peaks

