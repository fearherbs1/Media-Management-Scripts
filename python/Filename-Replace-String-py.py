# strips a specific string from the filename for all files in the directory the script is run in.
import os


def process_files():
    # Gather info
    current_dir = os.getcwd()
    target_string = input("Enter the string you want to remove: ")
    print(f"You Entered: {target_string}")

    # iterate through our files and rename them
    for count, filename in enumerate(os.listdir(current_dir)):
        if target_string in filename:
            new_filename = filename.replace(target_string, "")
            print(f"Processing {filename} ---> {new_filename}")
            os.rename(filename, new_filename)
    print("Done")


process_files()
