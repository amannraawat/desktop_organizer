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
            if filename != 'Cleaned Up' and filename != 'Recycle Bin' and filename != 'desktop_organizer':
                try:
                    extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                    new_name = filename
                    try:
                        path = extensions[extension]
                    except Exception:
                        extension = 'noname'
                    file_exists = os.path.isfile(extensions[extension] + '/' + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.split
                        new_name = new_name.split('/')[4]
                        file_exists = os.path.isfile(extensions[extension] + '/' + new_name)
                    
                    src = folder_to_track + '/' + filename
                    new_name = extensions[extension] + '/' + new_name
                    os.rename(src, new_name)
                except Exception:
                    print(filename)
                
extensions = {
    #no name formats
    'noname' : "/Users/hp/desktop/Cleaned Up/Other/Folders",
    
    #audio formats
    '.wav' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.midi' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.mp3' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.cda' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.aiff' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.wma' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.aac' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.ogg' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.flac' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    '.alac' : "/Users/hp/desktop/Cleaned Up/Media/Audio",
    
    #video formats
    '.mkv' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.flv' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.webm' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.ogv' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.gif' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.wmv' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.mp4' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.m4v' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.3gp' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.rm' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    '.mpeg' : "/Users/hp/desktop/Cleaned Up/Media/Video",
    
    #text formats
    '.txt' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.doc' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.docx' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.odt' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.pdf' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.wps' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.wpd' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.rtf' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.tex' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents",
    '.wks' : "/Users/hp/desktop/Cleaned Up/Media/Text Documents", 
    
    #image formats
    '.bmp' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.jpg' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.jpeg' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.png' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.ps' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.tiff' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.tif' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.cr2' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.ai' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.svg' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.psd' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    '.svg' : "/Users/hp/desktop/Cleaned Up/Media/Images",
    
    #presentations
    '.key' : "/Users/hp/desktop/Cleaned Up/Presentations",
    '.ppt' : "/Users/hp/desktop/Cleaned Up/Presentations",
    '.pptx' : "/Users/hp/desktop/Cleaned Up/Presentations",
    '.odp' : "/Users/hp/desktop/Cleaned Up/Presentations",
    '.pps' : "/Users/hp/desktop/Cleaned Up/Presentations",
    
    #programming
    '.c' : "/Users/hp/desktop/Cleaned Up/Programming",
    '.py' : "/Users/hp/desktop/Cleaned Up/Programming",
    '.class' : "/Users/hp/desktop/Cleaned Up/Programming",
    '.java' : "/Users/hp/desktop/Cleaned Up/Programming",
    '.h' : "/Users/hp/desktop/Cleaned Up/Programming",
    '.sh' : "/Users/hp/desktop/Cleaned Up/Programming",
    
    #spreadsheets
    '.ods' : "/Users/hp/desktop/Cleaned Up/Spreadsheets",
    '.xlr' : "/Users/hp/desktop/Cleaned Up/Spreadsheets",
    '.xls' : "/Users/hp/desktop/Cleaned Up/Spreadsheets",
    '.xlsx' : "/Users/hp/desktop/Cleaned Up/Spreadsheets",
    
    #system
    '.bak':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.cab':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.cfg':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.cpl':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.cur':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.dll':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.dmp':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.drv':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.icns' :   '/Users/hp/desktop/Cleaned Up/Other/System',
    '.ico':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.ini':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.lnk':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.msi':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.sys':    '/Users/hp/desktop/Cleaned Up/Other/System',
    '.tmp':    '/Users/hp/desktop/Cleaned Up/Other/System',
    
    #internet file formats
    '.php' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.html' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.xhtml' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.rss' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.asp' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.aspx' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.cer' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.cfm' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.pl' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.css' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.js' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.part' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.jsp' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    '.cgi' : "/Users/hp/desktop/Cleaned Up/Other/Internet",
    
    #disc formats
    '.bin' : "/Users/hp/desktop/Cleaned Up/Other/Disc",
    '.dmg' : "/Users/hp/desktop/Cleaned Up/Other/Disc",
    '.iso' : "/Users/hp/desktop/Cleaned Up/Other/Disc",
    '.toast' : "/Users/hp/desktop/Cleaned Up/Other/Disc",
    '.vcd' : "/Users/hp/desktop/Cleaned Up/Other/Disc",
    
    #compression formats
    '.7z' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    '.arj' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    '.deb' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    '.pkg' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    '.rar' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    '.z' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    '.zip' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    '.tar.gz' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    '.rpm' : "/Users/hp/desktop/Cleaned Up/Other/Compressed",
    
    #data foramts
    '.csv' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.dat' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.db' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.dbf' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.log' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.mdb' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.sav' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.sql' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.tar' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.xml' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    '.json' : "/Users/hp/desktop/Cleaned Up/Programming/Data",
    
    #executables
    '.apk' : "/Users/hp/desktop/Cleaned Up/Other/Executables",
    '.bat' : "/Users/hp/desktop/Cleaned Up/Other/Executables",
    '.com' : "/Users/hp/desktop/Cleaned Up/Other/Executables",
    '.exe' : "/Users/hp/desktop/Cleaned Up/Other/Executables",
    '.gadget' : "/Users/hp/desktop/Cleaned Up/Other/Executables",
    '.jar' : "/Users/hp/desktop/Cleaned Up/Other/Executables",
    '.wsf' : "/Users/hp/desktop/Cleaned Up/Other/Executables",
    
    #fonts
    '.fnt' : "/Users/hp/desktop/Cleaned Up/Other/Fonts",
    '.fon' : "/Users/hp/desktop/Cleaned Up/Other/Fonts",
    '.otf' : "/Users/hp/desktop/Cleaned Up/Other/Fonts",
    '.ttf' : "/Users/hp/desktop/Cleaned Up/Other/Fonts",
    
} 
 
 
 
                
folder_to_track = '/Users/hp/desktop'
folder_destination = '/Users/hp/desktop/Cleaned Up'
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
