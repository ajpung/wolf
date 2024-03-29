import tkinter as tk
from tkinter import filedialog
import audiosegment
import pygame
import pydub
from wolf.utils import mechanics


class AudioPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")

        # Create buttons for opening, playing, pausing, and resuming audio files
        self.open_button = tk.Button(
            root, text="Open Audio File", command=self.open_audio
        )
        self.play_button = tk.Button(
            root, text="Play", state=tk.DISABLED, command=self.play_audio
        )
        self.highpass_button = tk.Button(
            root,
            text="High-pass filter",
            state=tk.DISABLED,
            command=self.apply_highpass,
        )

        # self.pause_button = tk.Button(
        #    root, text="Pause", state=tk.DISABLED, command=self.pause_audio
        # )
        # self.resume_button = tk.Button(
        #    root, text="Resume", state=tk.DISABLED, command=self.resume_audio
        # )
        # self.show_button = tk.Button(
        #    root, text="Show wave", state=tk.DISABLED, command=self.show_audio
        # )

        self.open_button.pack(pady=10)
        self.play_button.pack(pady=10)
        self.highpass_button.pack(pady=10)
        # self.pause_button.pack()
        # self.resume_button.pack()
        # self.show_button.pack()

        # Initialize pygame
        pygame.mixer.init()

        # Register a callback to stop audio when the window is closed
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Initialize playback state
        self.paused = False

    def open_audio(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3 *.wav")]
        )
        if file_path:
            self.audio_file = mechanics.load_track(file_path)
            self.play_button.config(state=tk.NORMAL)

    def apply_highpass(self):
        d, r, w = mechanics.characterize_track(self.audio_file)
        hp_track = mechanics.high_pass(self.audio_file, r)
        self.play_button.config(state=tk.NORMAL)
        self.audio_file = hp_track

    def play_audio(self):
        d, r, w, t = mechanics.characterize_track(self.audio_file)
        print(type(self.audio_file))
        pydub.playback.play(self.audio_file)

    #    self.play_button.config(state=tk.DISABLED)
    #    self.pause_button.config(state=tk.NORMAL)

    # def pause_audio(self):
    #    pygame.mixer.music.pause()
    #    self.pause_button.config(state=tk.DISABLED)
    #    self.resume_button.config(state=tk.NORMAL)
    #    self.paused = True

    # def resume_audio(self):
    #    pygame.mixer.music.unpause()
    #    self.resume_button.config(state=tk.DISABLED)
    #    self.pause_button.config(state=tk.NORMAL)
    #    self.paused = False

    # def show_audio(self):
    #    info = basics.show_frame_rate(self.audio_file)
    #    print(info)

    def on_closing(self):
        # Check if audio is currently playing
        if pygame.mixer.music.get_busy():
            # Stop audio playback before closing the application
            pygame.mixer.music.stop()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayerApp(root)
    root.mainloop()
