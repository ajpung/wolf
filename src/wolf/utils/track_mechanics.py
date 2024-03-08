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
