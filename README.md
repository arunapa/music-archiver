# music-archiver
Python utility script for effortlessly retrieving track, album, and artist information from your local music library.
Simplify music organization and enhance your playlist creation with this efficient metadata extraction tool.

### Notes:

- Metadata is stored in a .csv files within the current directory
- Default metadata includes Title, Artist(s), Album, Filepath info
- You can tweak default script configuration by modifying `config.py`

### Disclaimer
This script uses mutagen library to read the ID3 metadata. If your audio files have missing metadata, this script will not be able to automatically recover it.
