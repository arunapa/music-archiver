# music-archiver
Python utility script for effortlessly retrieving track, album, and artist information from your local music library.
Simplify music organization and enhance your playlist creation with this efficient metadata extraction tool.
i.e. I realized I needed a workflow to archive all my physical media one day and decided to automate it.

### Notes:

- Metadata is stored in a .csv files within the current directory
- Default metadata includes Title, Artist(s), Album, Filepath info
- You can tweak default script configuration by modifying `config.py`

## Disclaimer
This script uses the [`tinytag`](https://pypi.org/project/tinytag/) python library to read the ID3 metadata. If your audio files have missing metadata, this script will not be able to automatically recover it.

## Installation
You can directly execute the python script by cloning this git repo.

```
git clone https://github.com/arunapa/music-archiver.git
cd music-archiver
pip install -r requirements.txt
```
Note: you may need to use pip3 instead of pip

## Config
You can configure some parameters for the script, detailed below

### Options
- `SUPPORTED_FORMATS`: Allows you to specify which audio formats you want to archive. Note: tinytag does not support all audio formats. Please refer to [the tinytag docs](https://pypi.org/project/tinytag/) for the exact list of supported formats

- `METADATA_CONTENTS`: Allows you to specify what information should be contained in the generated metadata file

- `OUTPUT_FILEPATH`: Allows you to customize the name and location of the output file path

- `DEBUG_MODE_ON`: Allows you to toggle debug mode on ("True") or off ("False")

## Running the script
Run the script from the command line

```
python3 music_archiver.py
```
Note: you may need to use python3 instead of python

## License
Licensed under [GNU GPL](LICENSE)
