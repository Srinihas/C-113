import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

main = "C:"

class FileEventHandler(FileSystemEventHandler):

  def on_created(self, event):
    print(f"Hey, {event.src_path} has been created!")
  
  def on_deleted(self, event):
    print(f"Oops, someone deleted {event.src_path}!")
  
  def on_modified(self, event):
    print(f"Hey there! {event.src_path} has been modified!")
  
  def on_moved(self, event):
    print(f"Hey, someone moved {event.src_path} to {event.dest_path}!")

# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, main, recursive=True)


# Start the Observer
observer.start()

try:
  while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
  print("Stopping!")
  observer.stop()






