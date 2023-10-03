import tkinter as tk
from tkinter import ttk
from notifications import notify

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


