import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Create a frame for better layout management
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Display label
        self.label = tk.Label(self.frame, text="00:00:00", font=("Helvetica", 72), fg="blue")
        self.label.pack()

        # Button styling
        button_style = {
            'width': 10,
            'height': 3,
            'font': ('Helvetica', 24),
            'bg': 'lightgray'
        }

        # Start button
        self.start_button = tk.Button(self.frame, text="Start", command=self.start, **button_style)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Stop button
        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop, **button_style)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        # Reset button
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, **button_style)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.label.config(text=self.format_time(self.elapsed_time))
            self.root.after(100, self.update)

    def format_time(self, seconds):
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

# Create the main window
root = tk.Tk()
root.title("Stopwatch")  # Set a title for the window
root.geometry("600x400")  # Set a specific window size

# Create an instance of the Stopwatch
stopwatch = Stopwatch(root)

# Start the Tkinter main loop
root.mainloop()
