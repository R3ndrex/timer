from plyer import notification
import os

def notify(time, title = "Timer", msg="Time has ended"):
    for root, dirs, files in os.walk(os.getcwd()):
        if "timer" in dirs:
            folder_path = os.path.join(root, "timer")
            break
    app_icon = f"{folder_path}/timer_icon.ico"
    app_icon = app_icon.replace("\\", "/")

    notification.notify(
        title = title,
        message = msg,
        app_icon = app_icon,
        timeout = int(time),
        )