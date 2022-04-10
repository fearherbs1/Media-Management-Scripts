import subprocess
import shlex
import re
import os
from os import path


def check_for_options_file():
    options_file_exists = os.path.exists("options.json")
    if not options_file_exists:
        print("No options.json file found, Exiting.")
        exit()


def remove_file_lines():
    # open our options file as read only and get the lines
    with open("options.json", "r") as f:
        lines = f.readlines()

    # delete our problematic file lines lines
    with open("options.json", "w") as f:
        for line in lines:
            # removes all file paths --output and the two lines with ) and ( in them using regex matching
            # yep there is probably a better way to do this but this long if statement will do for now
            if re.match(r".*?[\w:][\w:]\\.*\.[\w:]+.*", line.strip("\n")) is None and line.strip("\n") !=\
                    "  \"--output\"," and line.strip("\n") != "  \")\"," and line.strip("\n") != "  \"(\",":
                f.write(line)


def mkv_merge_out():
    output_dir = "Mkv-Merge-Out"
    current_dir = os.getcwd()
    mkv_tools_location = "'C:\\Program Files\\MKVToolNix\\mkvmerge.exe'"
	
	# check and make sure mkv tools exits in the correct location
    if path.exists(mkv_tools_location.replace("'", "")) is False:
        print("No mkv tools found. check directory")
        print(f"currently configured directory {mkv_tools_location} ")
        exit()

    try:
        os.mkdir(output_dir)
        print(f"Output directory '{output_dir}' created.")
    except FileExistsError:
        print(f"Output directory '{output_dir} exists, skipping creation.")

    for file in os.listdir(current_dir):
        filename = os.fsdecode(file)
        if filename.endswith(".mkv"):
            print(f"Processing File {file}...")

            mkv_tools_cmd = f"{mkv_tools_location} @options.json -o \"{output_dir}/{file}\" \"{file}\""

            output = subprocess.run(shlex.split(mkv_tools_cmd), capture_output=True, text=True)
            output_str = str(output)
            # print(output_str)
            errors = ["was requested but not found in the file.",
                      "Another default track for audio tracks has already been set"]

            if any(x in output_str for x in errors):
                print("***WARNING***\n")
                print("It seems that there was an error in MKV tool's track selection / flag setting.")
                print("This is possibly due to there being extra tracks in the file")
                print("The file that encountered this error has been logged to FIXME.txt")
                file1 = open("FIXME.txt", "a")  # append mode
                file1.write(f"{file}\n")
                file1.close()
            else:
                continue
            print(f"Finished Processing {file}")
            continue
        else:
            continue


check_for_options_file()
remove_file_lines()
mkv_merge_out()
