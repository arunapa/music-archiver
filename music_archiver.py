#!/usr/bin/env python3

'''
music_archiver.py
Python utility script for effortlessly retrieving track, album,
and artist information from your local music library.
'''

import csv
import os

from config import DEBUG_MODE_ON, METADATA_CONTENTS, OUTPUT_FILEPATH, SUPPORTED_FORMATS
from tinytag import TinyTag

__version__ = "1.1.0"

if __name__ == "__main__":

    print("\n".join([
        "",
        "Welcome to Music Archiver v" + __version__ + "!",
        "--------------------------------------------------------------------",
        "This is a Python script for effortlessly retrieving track, album",
        "and artist information from your local music library.",
        "Simplify music organization and enhance your playlist creation",
        "with this efficient metadata extraction tool.",
        "",
        "- Metadata is stored in a .csv files within the current directory",
        "- Default metadata includes Title, Artist(s), Album, Filepath info",
        "- You can tweak default script configuration by modifying config.py",
        "",
        "Disclaimer: This script uses tinytag library to read the ID3 metadata.",
        "If your audio files have missing metadata, this script will not be able",
        "to automatically recover it.",
        "--------------------------------------------------------------------",
        ""
    ]))

    path = input(f"Enter folder path containing audio files: ")

    if not os.path.exists(path):
        print(f"\nERROR: File path does not exist! Exiting...")
        exit(-1)

    print("")

    try:
        with open(OUTPUT_FILEPATH, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=METADATA_CONTENTS)
            writer.writeheader()

            i = 1

            for root, dirs, files in os.walk(path):
                for file in files:
                    full_file_path = os.path.join(root, file)
                    # filename, file_extension = os.path.splitext(full_file_path)

                    if file.endswith(SUPPORTED_FORMATS):
                        try:
                            row = {}
                            tag = TinyTag.get(full_file_path)
                            
                            if "#" in METADATA_CONTENTS:
                                row["#"] = i
                            
                            if "Filepath" in METADATA_CONTENTS:
                                row["Filepath"] = full_file_path

                            if "Title" in METADATA_CONTENTS:
                                row["Title"] = tag.title

                            if "Album" in METADATA_CONTENTS:
                                row["Album"] = tag.album

                            if "Artist(s)" in METADATA_CONTENTS:
                                row["Artist(s)"] = tag.artist

                            if "Track #" in METADATA_CONTENTS:
                                row["Track #"] = tag.track

                            if "Disc #" in METADATA_CONTENTS:
                                row["Disc #"] = tag.track

                            if "Duration" in METADATA_CONTENTS:
                                row["Duration"] = round(tag.duration)

                        except:
                            print(f"WARN: Some metadata may be missing for {full_file_path}")
                            
                            if DEBUG_MODE_ON:
                                print(tag)
                                print("")
                        
                        finally:
                            writer.writerow(row)
                            i = i + 1
        
    except Exception as e:
        print(f"ERROR: Unknown error occured. {e}")

    print(f"\nCompleted writing metadata to {OUTPUT_FILEPATH}!")
            
