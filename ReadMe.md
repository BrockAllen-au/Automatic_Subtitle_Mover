# Auto Subtitler
Created to copy a subtitle file from a folder to another file being named the same as it's parent folder.
Useful for media that has subtitles stored in sub-folders that are named the same as the media file.\
Currently the program looks for **English** subtitles only.

## Requirements
Python 3.x

## Usage
python.exe auto_subtitler.py

This will prompt you for the source of your subtitle folders:
```
Path to subtitle folder: C:\Temp\Media\Subtitles
```
& prompt for your desired destination of the subtitle file:
```
Path to media folder: C:\Temp\Media
```

All copy activity is logged to the same directory as the auto_subtitler.py to a log file 
"auto_subtitler.log"
```
Successfully copied C:\Temp\Media\Subs\TV_EP_S01E01/3_English.srt --> C:\Temp\Media\TV_EP_S01E01.eng.srt
Successfully copied C:\Temp\Media\Subs\TV_EP_S01E02/4_English.srt --> C:\Temp\Media\TV_EP_S01E02.eng.srt
```