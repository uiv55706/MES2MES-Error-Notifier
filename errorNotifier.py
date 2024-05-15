import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from win10toast import ToastNotifier  # Install this package using pip

# Specify the folders to monitor for new directories
folders_to_monitor_directories = [
    r"C:\Users\uiv55706\Desktop\notif_test1",
    r"C:\Users\uiv55706\Desktop\notif_test2",
    r"C:\Users\uiv55706\Desktop\notif_test3"
]

# Specify the folders to monitor for 10 txt files
folders_to_monitor_txt_files = [
    r"C:\Users\uiv55706\Desktop\notif_txt1",
    r"C:\Users\uiv55706\Desktop\notif_txt2",
    r"C:\Users\uiv55706\Desktop\notif_txt3"
]

# Initialize the toast notifier
toaster = ToastNotifier()

# Define the event handler for directory creation
class DirectoryCreationHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            show_toast_notification(event.src_path, "New error")

# Define the event handler for txt file counting
class TxtFileCountHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            check_txt_files(event.src_path)

def show_toast_notification(folder_path, event_type):
    parent_folder = os.path.dirname(folder_path)
    message = f"ALERT {event_type}: {os.path.basename(folder_path)} in {parent_folder}"
    toaster.show_toast("Error Monitor", message, icon_path="error.ico", duration=5)

def check_txt_files(file_path):
    folder = os.path.dirname(file_path)
    txt_files = [f for f in os.listdir(folder) if f.endswith('.txt')]
    if len(txt_files) == 10:
        show_toast_notification(folder, "10 .txt files")

if __name__ == "__main__":
    directory_creation_handler = DirectoryCreationHandler()
    txt_file_count_handler = TxtFileCountHandler()
    observer = Observer()
    
    # Schedule the observer for directory creation
    for folder in folders_to_monitor_directories:
        observer.schedule(directory_creation_handler, path=folder, recursive=True)
    
    # Schedule the observer for txt file counting
    for folder in folders_to_monitor_txt_files:
        observer.schedule(txt_file_count_handler, path=folder, recursive=True)
    
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
