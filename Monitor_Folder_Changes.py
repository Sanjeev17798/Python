# Start
# Import required modules
# Import file monitoring classes and time module
# Create event handler
# Define actions for events (e.g., file created, modified)
# Initialize observer
# Create an observer object to watch the directory
# Schedule monitoring
# Attach the event handler to the target folder (recursive if needed)
# Start observer
# Begin monitoring for file system changes
# Keep program running
# Use an infinite loop to continuously listen for events
# Handle termination
# Stop observer safely when interrupted (e.g., Ctrl+C)
# End

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path}")

    def on_modified(self, event):
        print(f"Modified: {event.src_path}")

def monitor_folder(path):
    observer = Observer()
    observer.schedule(Watcher(), path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

monitor_folder("/Users/sanjeevkumaryadav/Documents")