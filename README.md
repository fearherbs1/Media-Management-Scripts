# Media-Management-Scripts
A collection of scripts I use to manage my media.

## python/mkvtoolnix-batch-py
Based Serde's Batch Script Here: https://github.com/Serede/mkvtoolnix-batch  

Windows Script to batch process the renaming and taging of mkv tracks.  

It has a few improvements such as:
* Python so it could work on other os's with some small modifications
* Error Checking for extra track instructions and default flagging
* automates the removal of the `--output` and `()` lines

### Useage:
1. Download [MKVToolNix](https://mkvtoolnix.download/downloads.html)
2. Open `mkvtoolnix-gui.exe`.
3. Add any of the MKV files to be processed (drag-and-drop works just fine).
4. Perform your changes within the GUI (disable tracks, rename tracks, set default tracks, etc.).
5. Go to `Menu Bar > Multiplexer > Create option file`, and save it as 'options.json' in the same directory where all MKV files to be processed are. You can then close the GUI.
6. Download The script and place it where your media files and optioms.json is.
7. If your mkvmerge.exe is not in `C:\Program Files\MKVToolNix` Edit the script and replace the value of the variable `mkv_tools_location` with your path to `mkvmerge.exe`
NOTE: Be sure to leave both sets of quotes and escape your backslashes!! ex.) `mkv_tools_location = "'C:\\Program Files\\MKVToolNix\\mkvmerge.exe'"`
8. Run `mkvtoolnix-batch-py.py` by running `python3 mkvtoolnix-batch-py.py` in a command prompt within your directory.
9. Go grab yourself a cup of coffee and wait for the multiplexing process to complete. Processed MKV files will appear inside the `Mkv-Merge-Out` directory.
