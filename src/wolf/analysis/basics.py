import numpy as np
from pydub import AudioSegment


def show_frame_rate(audio_file: str) -> np.int32:
    ext = audio_file.split(".")[1]
    if ext == "mp3":
        song = AudioSegment.from_mp3(audio_file)
    elif ext == "wav":
        song = AudioSegment.from_wav(audio_file)
    else:
        song = AudioSegment.from_file(audio_file)
    info = np.int32(song.frame_rate)
    return info


'''
def unpack_coordinates(
    arr: np.ndarray,
) -> Union[Tuple[float, float, float], Tuple[np.ndarray, np.ndarray, np.ndarray]]:
    """
    Examines the dimension length of a coordinate array and resizes array dimensions
    to match downstream expected formats.

    Args:
        arr (np.ndarray): Array containing coordinate array

    Returns:
        Three dimension values of the input array.
    """
    if len(arr.shape) == 1:
        return arr[0], arr[1], arr[2]
    elif arr.shape[0] == 1:
        return arr[0, 0], arr[0, 1], arr[0, 2]
    else:
        return arr[:, 0], arr[:, 1], arr[:, 2]
'''
