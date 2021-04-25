import os
from os import path
import subprocess
import shlex
from pathlib import Path


def sub_audio_merge():
    output_dir = "Sub-Audio-Merge-Out"
    current_dir = os.getcwd()

    # when changing this directory be sure to keep both sets of quotes!
    mkv_tools_location = "'C:\\Program Files\\MKVToolNix\\mkvmerge.exe'"

    # check and make sure mkv tools exits in the correct location
    if path.exists(mkv_tools_location.replace("'", "")) is False:
        print("No mkv tools found. check directory")
        print(f"currently configured directory {mkv_tools_location} ")
        exit()

    print("Note: be sure that the subtitle files/audio files and video file have THE SAME NAME (besides the extension)")
    print("ex. 'Attack on Titan - S01E01.mkv' 'Attack on Titan - S01E01.srt'")
    print("if using mp4, this script will convert the files to .mkv")
    vid_input_format = input("Enter video format extension ex. .mp4 .mkv\n")
    sub_audio_input_format = input("Enter subtitle or audio format extension ex. .srt .ass .flac .aac\n")
    sub_audio_input_lang = input("Enter the language code for the sub/audio file ex. eng jpn rus spa\n ")
    sub_audio_track_name = input("Enter the track name you want ex. english fansubs\n")

    # create our output dir if it does not exist
    try:
        os.mkdir(output_dir)
        print(f"Output directory '{output_dir}' created.")
    except FileExistsError:
        print(f"Output directory '{output_dir} exists, skipping creation.")

    # process the files
    for file in os.listdir(current_dir):
        filename = os.fsdecode(file)
        if filename.endswith(vid_input_format):
            print(f"Processing File {file}...")

            # removes the video extension and replaces it with the user supplied audio extension
            file_sub_audio = Path(file).stem + sub_audio_input_format

            file_to_mkv = Path(file).stem + ".mkv"

            mkv_tools_cmd = f"{mkv_tools_location}  -o '{output_dir}/{file_to_mkv}' '{file}'\
             --language 0:{sub_audio_input_lang} --track-name 0:{sub_audio_track_name} '{file_sub_audio}'"

            output = subprocess.run(shlex.split(mkv_tools_cmd), capture_output=True, text=True)
            output_str = str(output)
            print(output_str)
            print(f"Finished Processing {file}")
            continue
        else:
            continue


sub_audio_merge()
