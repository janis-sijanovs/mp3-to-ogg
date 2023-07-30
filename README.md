# MP3 to OGG Converter

This Python script converts all MP3 files in a specified directory to mono OGG format.

## Requirements

- Python 3.7 or newer
- ffmpeg

## Installation

1. Clone this repository or download the script.
2. Install the required Python packages with `pip install -r requirements.txt`.
3. Make sure `ffmpeg` is installed on your system. If it's not, you can install it using a package manager like `apt` (on Ubuntu) or `brew` (on macOS):

    For Ubuntu:
    
    ```sudo apt update
    sudo apt install ffmpeg```

    For macOS:

    ```brew install ffmpeg```

    
## Usage

1. Replace `'/path/to/mp3s/'` and `'/path/to/oggs/'` in the script with the actual paths to the source and target directories.
2. Run the script with `python3 convert_to_ogg.py`.

This will convert all MP3 files in the source directory to mono OGG format and save them in the target directory with names in the format `healing_{id}.ogg`.

