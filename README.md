# Media-Management-Scripts
A collection of scripts I use to manage my media.

## python/mkvtoolnix-batch-py
Based Serde's Batch Script Here: https://github.com/Serede/mkvtoolnix-batch  

Windows Script to batch process the renaming and taging of mkv tracks.  

It has a few improvements such as:
* Python so it could work on other os's with some small modifications
* Error Checking for extra track instructions and default flagging
* automates the removal of the `--output` and `()` lines by usiing part of my script [HERE](https://github.com/fearherbs1/options.json-arg-stripper)

### Dependencies
- [MKVToolNix](https://www.fosshub.com/MKVToolNix.html)
- [python3](https://www.python.org/downloads/)

### Usage:
1. Download [MKVToolNix](https://mkvtoolnix.download/downloads.html)
2. Open `mkvtoolnix-gui.exe`.
3. Add any of the MKV files to be processed (drag-and-drop works just fine).
4. Perform your changes within the GUI (disable tracks, rename tracks, set default tracks, etc.).
5. Go to `Menu Bar > Multiplexer > Create option file`, and save it as 'options.json' in the same directory where all MKV files to be processed are. You can then close the GUI.
6. Download The script and place it where your media files and options.json is.
7. If your mkvmerge.exe is not in `C:\Program Files\MKVToolNix` Edit the script and replace the value of the variable `mkv_tools_location` with your path to `mkvmerge.exe`  
  
**NOTE: Be sure to leave both sets of quotes and escape your backslashes!!** ex:  
`mkv_tools_location = "'C:\\Program Files\\MKVToolNix\\mkvmerge.exe'"`

8. Run `mkvtoolnix-batch-py.py` by running `python3 mkvtoolnix-batch-py.py` in a command prompt within your directory.
9. Wait for the multiplexing process to complete. Processed MKV files will appear inside the `Mkv-Merge-Out` directory.

If an error is detected by the script it will put that filename in a text file named FIXME.txt  
This is mostly caused by unaccounted for media tracks existing in other files besides the first one, audio commentary files are a common example.  

**This is not extensively tested be sure to check your finished files regardless!!**

## python/Filename-Replace-String-py
A very simple script that removes a specific string from a filename for all files in a directory.
This is useful if you only need to remove a part of a filename.

### Dependencies
- [python3](https://www.python.org/downloads/)

### Usage:
1. Download the script and place it in the same directory as the files you want to rename.
2. Run the script with Python3 `python3 Filename-Replace-String-py.py`
3. Enter the string you want to remove in the console
4. profit

## python/sub-audio-merge-py
This script helps you merge audio tracks or subtitle tracks into one mkv file.
It can also append a language code and track description
For example:

`Attack on Titan S01E01 - To you in 200 years.mp4`  
and  
`Attack on Titan S01E01 - To you in 200 years.srt`  

will become:    
`Attack on Titan S01E01 - To you in 200 years.mkv`  
With both tracks included inside the mkv container.  

### Dependencies
- [MKVToolNix](https://www.fosshub.com/MKVToolNix.html)
- [python3](https://www.python.org/downloads/)

### Usage:
1. Download the script and place it in the same directory as the audo or subtitle files.  
2. **BE SURE** the files have the same name besides the extension ex:  
`Attack on Titan S01E01 - To you in 200 years.mp4` and `Attack on Titan S01E01 - To you in 200 years.srt`
   
3. Download [MKVToolNix](https://mkvtoolnix.download/downloads.html)
4. If be sure it installs to: `C:\Program Files\MKVToolNix`
5. run the script with `python3 sub-audio-merge-py.py`
6. follow the prompts
7. profit