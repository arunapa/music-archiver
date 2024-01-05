#!/usr/bin/env python3

'''
music_archiver.py
Python utility script for effortlessly retrieving track, album,
and artist information from your local music library.
'''

import csv
import mutagen
import os

from config import DEBUG_MODE_ON, METADATA_CONTENTS, OUTPUT_FILEPATH, SUPPORTED_FORMATS

__version__ = "1.0.0"

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
        "Disclaimer: This script uses mutagen library to read the ID3 metadata.",
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
                        m = mutagen.File(full_file_path, easy=True)

                        row = {}
                        row["#"] = i
                        row["Filepath"] = full_file_path
                        row["Title"] = m["title"][0]
                        row["Album"] = m["album"][0]
                        row["Artist(s)"] = m["artist"][0]
                        row["Track Number"] = m["tracknumber"][0]

                    except:
                        print(f"WARN: Some metadata may be missing for {full_file_path}")
                        
                        if DEBUG_MODE_ON:
                            print(m)
                            print("")
                    
                    finally:
                        writer.writerow(row)
                        i = i + 1

    print(f"\nCompleted writing metadata to {OUTPUT_FILEPATH}!")
            
