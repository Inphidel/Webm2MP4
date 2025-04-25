import os
import subprocess

def convert_webm_to_mp4(input_file, output_file):
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' does not exist. Please check the path or filename.")
        return

    # Check if the output file already exists
    if os.path.exists(output_file):
        print(f"Output file '{output_file}' already exists. Please choose a different name.")
        return

    # FFmpeg command to convert WebM to MP4
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,         # Input file
        "-c:v", "libx264",       # Video codec: H.264 (widely compatible with MP4)
        "-crf", "23",            # Constant Rate Factor: 23 balances quality and file size
        "-c:a", "aac",           # Audio codec: AAC (standard for MP4)
        "-b:a", "128k",          # Audio bitrate: 128 kbps
        output_file              # Output file
    ]

    # Execute the FFmpeg command
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Conversion completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during conversion: {e}")
    except FileNotFoundError:
        print("FFmpeg is not installed or not found in system PATH. Please install FFmpeg.")

# Prompt user for input filename
input_file = input("Enter the input WebM filename (e.g., source.webm or C:\\path\\to\\source.webm): ").strip()

# If no path is provided, assume the file is in the script's directory
if not os.path.isabs(input_file) and not os.path.dirname(input_file):
    input_file = os.path.join(os.path.dirname(__file__), input_file)

# Generate output filename by replacing .webm with .mp4
output_file = os.path.splitext(input_file)[0] + ".mp4"

# Call the conversion function
convert_webm_to_mp4(input_file, output_file)
