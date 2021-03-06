import EEGFuncs

# Required settings #

# Data source. Options:
# 'muse' for data from Muse headsets.
# 'muse-lsl' for data from Muse headsets recorded with Lab Streaming Layer.
# 'openbci' for OpenBCI Cyton data recorded with the OpenBCI GUI;
# 'openbci-ganglion' for OpenBCI Ganglion data recorded with the OpenBCI GUI;
# 'openbci-openvibe' for Cyton data recorded with OpenViBE's csv writer
# 'openbci-ganglion-openvibe' for Ganglion data recorded with OpenViBE's csv writer

source = 'muse'#'openbci'

# Path to EEG data file
path = 'C:/Users/nkala/Desktop/Final_Data/' #'data/'

# EEG data file name
filename = 'Nivii_Calm_filtered_data2.csv'

# Session title (used in some plots and such)
session_title = "Muse Data"

# Channel
channel = 1

# Initialize
EEG = EEGFuncs.EEGFuncs(path, filename, source, session_title)

# Here we can set some additional properties
# The 'plot' property determines whether plots are displayed or saved.
# Possible values are 'show' and 'save'
EEG.plot = 'show'

# Load the EEG data
EEG.load_data()

EEG.load_channel(channel)

print("Processing channel "+ str(EEG.channel))

# Removes OpenBCI DC offset
EEG.remove_dc_offset()

# Notches 60hz noise (if you're in Europe, switch to 50Hz)
EEG.notch_mains_interference()

# Make signal plot
EEG.signalplot()

# Calculates spectrum data and stores as EEGFuncs attribute(s) for reuse
EEG.get_spectrum_data()

# Returns bandpassed data
# (uses scipy.signal butterworth filter)
start_Hz = 12 #1
stop_Hz = 38 #50
EEG.data = EEG.bandpass(start_Hz,stop_Hz)

# Make Spectrogram
EEG.spectrogram()

# Line graph of amplitude over time for a given frequency range.
# Arguments are start frequency, end frequency, and label
#EEG.plot_band_power(12, 28,"Beta")
EEG.plot_band_power(8,12,"Alpha")

# Power spectrum plot
EEG.plot_spectrum_avg_fft()

# Plot coherence fft (not tested recently...)
# s1 = bandpass(seginfo["data"][:,1-1], config['band'])
# s2 = bandpass(seginfo["data"][:,8-1], config['band'])
# plot_coherence_fft(s1,s2,"1","8")

EEG.showplots()
