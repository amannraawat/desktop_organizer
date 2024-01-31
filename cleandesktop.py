from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

class Myhandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'aman':
                new_name = filename
                split_name = filename.split('.')
                file_exists = os.path.isfile(folder_destination + '/' + new_name)
                while file_exists:
                    i += 1
                    new_name = os.path.splittext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.split
                    new_name = new_name.split('/')[4]
                    file_exists = os.path.isfile(folder_destination + '/' + new_name)
                    
                src = folder_to_track + '/' + filename
                new_name = folder_destination + '/' + new_name
                os.rename(src, new_name)
                
                
folder_to_track = '/Users/hp/desktop/example'
folder_destination = '/Users/hp/desktop/example/aman'
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
