import sounddevice as sd
import scipy.io.wavfile as wav
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class VoiceRecorder:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Recorder")
        
        self.is_recording = False
        self.fs = 44100  
        self.recording = None

        self.record_button = tk.Button(master, text="Record", command=self.start_recording)
        self.record_button.pack(pady=10)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_recording)
        self.stop_button.pack(pady=10)
        
        self.play_button = tk.Button(master, text="Play", command=self.play_recording)
        self.play_button.pack(pady=10)
        
        self.save_button = tk.Button(master, text="Save", command=self.save_recording)
        self.save_button.pack(pady=10)
        
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=10)
        
    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.recording = sd.rec(int(self.fs * 5), samplerate=self.fs, channels=2)
            sd.wait()
            messagebox.showinfo("Info", "Recording started")
        
    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            sd.stop()
            messagebox.showinfo("Info", "Recording stopped")
        
    def play_recording(self):
        if self.recording is not None:
            sd.play(self.recording, self.fs)
            sd.wait()
        else:
            messagebox.showinfo("Info", "No recording found")
    
    def save_recording(self):
        if self.recording is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
            if file_path:
                wav.write(file_path, self.fs, self.recording)
                messagebox.showinfo("Info", f"Recording saved to {file_path}")
        else:
            messagebox.showinfo("Info", "No recording found")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorder(master=root)
    root.mainloop()

