"""
Names subtitles the same as their parent folder and copies the files to a folder of your choice
"""
import os
import shutil


def main():
    """Automatic subtitle name and copier program."""
    path_to_subs = get_valid_directory("Path to subtitle folder: ")
    path_to_media_files = get_valid_directory("Path to media folder: ")
    parent_dirs = os.listdir(path_to_subs)
    copy_subtitles(parent_dirs, path_to_media_files, path_to_subs)


def copy_subtitles(parent_dirs, path_to_media_files, path_to_subs):
    """Copies English subtitle with the largest file size to designated media file path."""
    log_file = f"{os.getcwd()}/auto_subtitler.log"
    out_file = open(log_file, 'a')
    for directory in parent_dirs:
        subtitles = os.listdir(f"{path_to_subs}/{directory}")
        sub_to_copy = ""
        file_size_compare = 0
        for subtitle in subtitles:
            if "eng" in subtitle.lower() and ".srt" in subtitle.lower():
                file_stats = os.stat(f"{path_to_subs}/{directory}/{subtitle}")
                file_size = file_stats.st_size
                if file_size > file_size_compare:
                    sub_to_copy = subtitle
        try:
            source = f"{path_to_subs}/{directory}/{sub_to_copy}"
            destination = f"{path_to_media_files}/{directory}.eng.srt"
            shutil.copyfile(source, destination)
            print(f"Successfully copied {source} --> {destination}", file=out_file)
        except PermissionError:
            print(f"ERROR: Unable to access file {source}, or no matching subtitle found in {directory} directory",
                  file=out_file)
    out_file.close()


def get_valid_directory(prompt):
    """Gets a valid directory input from user."""
    user_directory = input(prompt)
    user_directory = os.path.abspath(user_directory)
    while not os.path.isdir(user_directory):
        print("Could not verify path, please provide a new path.")
        user_directory = input(prompt)
        user_directory = os.path.abspath(user_directory)
    return user_directory


if __name__ == '__main__':
    main()
