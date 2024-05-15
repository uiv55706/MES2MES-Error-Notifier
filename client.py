import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from win10toast import ToastNotifier  # Install this package using pip

# Specify the folder to monitor
folder_to_monitor = r"C:\Users\uiv55706\Desktop\notif_test"

# Initialize the toast notifier
toaster = ToastNotifier()

# Define the event handler
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            show_toast_notification(event.src_path, "New error")

def show_toast_notification(folder_path, event_type):
    message = f"ALERT {event_type}: {os.path.basename(folder_path)}"
    toaster.show_toast("Error Monitor", message, duration=5)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_monitor, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()