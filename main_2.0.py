# 2-й Способ
import tkinter as tk
import pyttsx4

class AudioBookGUI:
    def __init__(self, root, book_text):
        self.root = root
        self.book_text = book_text
        self.engine = pyttsx4.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty("volume", 1.0)
        self.paused = False
        self.slider_pos = 0
        self.total_length = len(self.book_text)
        self.current_pos = 0
        self.text_label = tk.Label(root, text="Press Play to start reading")
        self.text_label.pack()
        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack()
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack()
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack()
        self.slider = tk.Scale(root, from_=0, to=self.total_length, orient=tk.HORIZONTAL, command=self.on_slider_move)
        self.slider.pack()

    def play(self):
        if self.paused:
            self.engine.resume()
            self.paused = False
        else:
            self.engine.say(self.book_text[self.current_pos:])
            self.engine.runAndWait()

    def pause(self):
        self.engine.pause()
        self.paused = True

    def stop(self):
        self.engine.stop()
        self.paused = False
        self.current_pos = 0
        self.slider.set()

    def on_slider_move(self, pos):
        self.current_pos = int(pos)
        self.slider.set(self.current_pos)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    book_text = "Этот тескт может быть очень длиным поэтому исполущуем слайдер"
    root = tk.Tk()
    root.title("Audio Book")
    app = AudioBookGUI(root, book_text)
    app.run()