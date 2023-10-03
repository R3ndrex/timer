from interface import start_timer,stop_timer,update_timer
import tkinter as tk
from tkinter import ttk
from notifications import notify

def main():
    duration = 30
    remaining_time = duration
    timer_running = False
    timer_id = [None]

    app = tk.Tk()
    app.title("Timer App")
    app.geometry("800x600")

    time_display = tk.Label(app, text="Time Left: 00:00:00", font=("Helvetica", 24))
    time_display.pack()

    canvas = tk.Canvas(app, width=200, height=200)
    canvas.pack()

    progress_bar = ttk.Progressbar(app, orient="horizontal", length=500, mode="determinate", maximum=duration)
    progress_bar.pack()

    start_button = tk.Button(app,cursor="hand2", text="Start Timer", command=start_timer)
    start_button.pack()

    stop_button = tk.Button(app,cursor="hand2", text="Stop Timer", command=stop_timer)
    stop_button.pack()

    custom_label = tk.Label(app, cursor="xterm",text="Custom Time (mm:ss):")
    custom_label.pack()

    app.mainloop()
if __name__=="__main__":
    main()
