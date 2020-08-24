import os
import sys
import time
import logging
import subprocess 
from watchdog.observers import Observer
# from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

def on_modified(event):
	print("restart debugger")
	print event.src_path
	child = subprocess.Popen(['pgrep', '-f', "__debug_bin"], stdout=subprocess.PIPE, shell=False)
	pid = int(child.communicate()[0])
	os.kill(int(pid), 9)


logging.basicConfig(level=logging.INFO,
					format='%(asctime)s - %(message)s',
					datefmt='%Y-%m-%d %H:%M:%S')
path = sys.argv[1] if len(sys.argv) > 1 else '.'
# event_handler = LoggingEventHandler()
event_handler = PatternMatchingEventHandler(patterns=["*.go"],
                ignore_patterns=[],
                ignore_directories=True)
event_handler.on_modified = on_modified
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()
observer.join()