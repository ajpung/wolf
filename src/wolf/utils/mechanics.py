import numpy as np
import audiosegment

from pydub.playback import play
from typing import Tuple


def load_track(audio_file: str) -> audiosegment:
    """
    Loads an .mp3 or .wav file via pydub

    Args:
        audio_file: path to the audio file

    Returns:
        track: The equivalent audiosegment
    """
    # Read in initial audio track
    track = audiosegment.from_file(audio_file)
    return track


def split_track(track: audiosegment) -> Tuple:
    """
    Splits an audiosegment into two channels, each channel is a Numpy array

    Args:
        track: The loaded audiosegment

    Returns:
        l_channel: the left channel in Numpy array format
        r_channel: the right channel in Numpy array format
    """
    # Convert track to Numpy arrays
    splits = track.to_numpy_array()

    # Define left/right channels
    l_channel = splits[:, 0]
    r_channel = splits[:, 1]

    return l_channel, r_channel


def arrays_to_track(
    l_channel: np.ndarray, r_channel: np.ndarray, framerate: int = 44100
) -> audiosegment:
    """
    Ingests two arrays (one left channel, one right channel), and recombines them into an audiosegment.

    Args:
        l_channel: The left channel in Numpy array format
        r_channel: The right channel in Numpy array format

    Returns:
        newtrack: The audiosegment created from both channels
    """
    # Re-stack numpy arrays
    newtrack = np.vstack((l_channel, r_channel)).T

    # Convert back to the new track
    newtrack = audiosegment.from_numpy_array(newtrack, framerate=framerate)

    return newtrack


def characterize_track(audio_file: audiosegment) -> Tuple:
    """
    Characterizes an audio track.

    Args:
        audio_file: path to the audio file

    Returns:
        track: The equivalent audiosegment
    """
    # Extract duration
    duration = audio_file.duration_seconds

    # Extract sample rate
    samprate = audio_file.frame_rate

    # Extract frame width
    sampwdth = audio_file.frame_width

    # Identify total samples and time axis
    Lchan, Rchan = split_track(audio_file)
    n_samples = len(Lchan)
    time_axis = np.linspace(0, duration, num=n_samples)

    return duration, samprate, sampwdth, time_axis
