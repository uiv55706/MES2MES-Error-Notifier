import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from win10toast import ToastNotifier  # Install this package using pip

# Specify the folders to monitor
folders_to_monitor = [
    r"C:\Users\uiv55706\Desktop\notif_test1",
    r"C:\Users\uiv55706\Desktop\notif_test2",
    r"C:\Users\uiv55706\Desktop\notif_test3"
]

# Initialize the toast notifier
toaster = ToastNotifier()

# Define the event handler
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            show_toast_notification(event.src_path, "New error")

def show_toast_notification(folder_path, event_type):
    parent_folder = os.path.dirname(folder_path)
    message = f"ALERT {event_type}: {os.path.basename(folder_path)} in {parent_folder}"
    toaster.show_toast("Error Monitor", message, icon_path="error.ico", duration=5)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    
    # Schedule the observer for each folder
    for folder in folders_to_monitor:
        observer.schedule(event_handler, path=folder, recursive=True)
    
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()