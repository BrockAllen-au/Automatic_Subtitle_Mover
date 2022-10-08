"""
Names subtitles the same as their parent folder and copies the files to the root directory where media is located
Structure of folders:
Media_Files/Subs/Episode_Sub_Folders/episode.srt
"""
import os
import shutil


def main():
    path_to_subs = get_valid_directory("Path to subtitle folder: ")
    path_to_media_files = get_valid_directory("Path to media folder: ")
    parent_dirs = os.listdir(path_to_subs)
    for directory in parent_dirs:
        subtitles = os.listdir(f"{path_to_subs}/{directory}")
        print(f"subtitles found in {directory} {subtitles}")
        sub_to_copy = ""
        file_size_compare = 0
        for subtitle in subtitles:
            if "eng" in subtitle.lower() and ".srt" in subtitle.lower():
                file_stats = os.stat(f"{path_to_subs}/{directory}/{subtitle}")
                file_size = file_stats.st_size
                if file_size > file_size_compare:
                    sub_to_copy = subtitle
        source = f"{path_to_subs}/{directory}/{sub_to_copy}"
        destination = f"{path_to_media_files}/{directory}.eng.srt"
        shutil.copyfile(source, destination)


def get_valid_directory(prompt):
    """Gets a valid directory input from user."""
    user_directory = input(prompt)
    user_directory = os.path.abspath(user_directory)
    while not os.path.isdir(user_directory):
        print("Could not verify path, please provide a new path.")
        user_directory = input(prompt)
        user_directory = os.path.abspath(user_directory)
    return user_directory


main()
