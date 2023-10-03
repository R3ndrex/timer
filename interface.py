import tkinter as tk
from tkinter import ttk
from notifications import notify

duration = 300
remaining_time = duration
timer_running = False
timer_id = [None]  # Use a list to store the timer's after() ID

def update_timer():
    global remaining_time, timer_running
    if remaining_time >= 0 and timer_running:
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_display.config(text=f"Time Left: {hours:02d}:{minutes:02d}:{seconds:02d}")
        progress_bar.step(1)
        remaining_time -= 1
        if remaining_time < 0:
            notify()
            progress_bar.stop()
        else:
            timer_id[0] = app.after(1000, update_timer)

def start_timer():
    global timer_running, remaining_time
    timer_running = True
    remaining_time = duration  # Reset remaining_time to duration
    progress_bar["value"] = 0  # Reset progress bar
    if timer_id[0]:
        app.after_cancel(timer_id[0])  # Cancel any pending timer updates
    timer_id[0] = app.after(0, update_timer)  # Start the timer immediately
    # Note: Use 0 milliseconds to ensure it starts without delay

def stop_timer():
    global timer_running
    timer_running = False
    if timer_id[0]:
        app.after_cancel(timer_id[0])

def start_custom_timer():
    global duration
    custom_time_str = custom_time_entry.get()
    custom_hours,custom_minutes, custom_seconds = map(int, custom_time_str.split(":"))
    duration = custom_hours * 3600 +custom_minutes * 60 + custom_seconds
    start_timer()


app = tk.Tk()
app.title("Timer App")
app.geometry("800x600")

time_display = tk.Label(app, text="Time Left: 00:00:00", font=("Helvetica", 24))
time_display.pack()

canvas = tk.Canvas(app, width=200, height=200)
canvas.pack()

progress_bar = ttk.Progressbar(app, orient="horizontal", length=500, mode="determinate", maximum=duration)
progress_bar.pack()

start_button = tk.Button(app, cursor="hand2", font=("Helvetica", 12),text="Start Timer", command=start_timer,width=50, height=2)
start_button.pack()

stop_button = tk.Button(app, cursor="hand2",font=("Helvetica", 12),text="Stop Timer", command=stop_timer,width=50, height=2)
stop_button.pack()

custom_label = tk.Label(app, text="Custom Time (hh:mm:ss):")
custom_label.pack()

custom_time_entry = tk.Entry(app)
custom_time_entry.pack()

custom_start_button = tk.Button(app, cursor="hand2",font=("Helvetica", 12), text="Start Custom Timer", command=start_custom_timer,width=50, height=2)
custom_start_button.pack()

app.mainloop()
