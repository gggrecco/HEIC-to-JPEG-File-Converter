# HEIC-to-JPEG-File-Converter
This repository contains a Python script that converts HEIC images to JPEG format using ImageMagick. 

## Prerequisites

1. **Python 3.x**: Make sure Python is installed and added to your PATH.
2. **ImageMagick**: Install ImageMagick and ensure it is added to your PATH. You can download it from [ImageMagick](https://imagemagick.org/script/download.php).
3. **Wand**: Python binding for ImageMagick. Install it using pip:
    ```sh
    pip install wand
    ```

    Usage

1. **Update the Directories**:
    - Open `convert_heic_to_jpeg.py`.
    - Replace `input_directory` with the path to your directory containing HEIC files.
    - Replace `output_directory` with the path to your desired output directory for JPEG files.

2. **Run the Script**:
    ```sh
    python convert_heic_to_jpeg.py
    ```

The script will convert all HEIC files in the input directory to JPEG files and save them in the output directory.
