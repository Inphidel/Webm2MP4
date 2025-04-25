# WebM to MP4 Converter

A simple Python script to convert WebM video files to MP4 format using FFmpeg.

## Requirements
- Python 3.x
- FFmpeg installed and added to system PATH
- Input file must be in WebM format

## Installation
1. Install Python 3.x from python.org
2. Install FFmpeg from ffmpeg.org and add it to your system PATH
3. Save the script as `convert_webm_to_mp4.py`

## Usage
1. Run the script: python convert_webm_to_mp4.py
2. Enter the WebM filename (e.g., thisfile.webm or C:\path\to\thisfile.webm)
3. The script will convert the file to MP4 with the same name in the same directory

## Features
- Converts WebM to MP4 with H.264 video and AAC audio
- Supports both simple filenames and full file paths
- Checks for input file existence and output file conflicts
- Balances quality and file size (CRF 23, 128kbps audio)

## Notes
- If no path is provided, the script looks for the file in the same directory as the script
- Ensure you have permission to convert the content
- Requires an active FFmpeg installation

## License
MIT
