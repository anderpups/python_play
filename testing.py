#!/home/anderpups/repos/python/bin/python3
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

with open('./settings.cfg',"r") as file:
  settings = file.readlines()

for setting in settings:
  setting.split('=')[0] = setting.split('=')[1]
  print(watch_path)
exit()

def read_file(event):
  with open(event.src_path,"r") as file:
    file_contents = file.readlines()
  print(file_contents)

watch_path_recursive=True

if __name__ == "__main__":
    event_handler = PatternMatchingEventHandler(patterns=["*.xml"],
                                    ignore_patterns=[],
                                    ignore_directories=True)
    event_handler.on_created = read_file
    event_handler.on_modified = read_file
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=watch_path_recursive)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
