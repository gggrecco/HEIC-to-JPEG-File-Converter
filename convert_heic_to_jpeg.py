import os
import subprocess

def convert_heic_to_jpeg(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith('.heic'):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpeg')
                
                # Command to convert HEIC to JPEG using ImageMagick
                command = f'magick convert "{input_path}" "{output_path}"'
                
                try:
                    subprocess.run(command, check=True, shell=True)
                    print(f"Converted {input_path} to {output_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to convert {input_path}: {e}")

input_directory = r'C:\Users\Greg\Dog\all_images'  # Replace with your input directory
output_directory = r'C:\Users\Greg\Dog\all_images_jpeg'  # Replace with your desired output directory

convert_heic_to_jpeg(input_directory, output_directory)
