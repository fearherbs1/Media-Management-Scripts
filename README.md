# Media-Management-Scripts
A collection of scripts I use to manage my media.

## mkvtoolnix-batch-py
Based Serde's Batch Script Here: https://github.com/Serede/mkvtoolnix-batch  

Windows Script to batch process the renaming and taging of mkv tracks.  

It has a few improvements such as:
* Python so it could work on other os's with some small modifications
* Error Checking for extra track insturctions and default flagging
* automates the removal of the `--output` and `()` lines
