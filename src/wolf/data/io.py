import numpy as np
import librosa as lb

y, sr = lb.load("~//..//samples//piano_oneshot.mp3")
print(lb.get_duration(y=y, sr=sr))
