import os
from apnggif import apnggif

def convert_apng_to_gif(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.png'):
            # Construct full file path
            png_path = os.path.join(source_folder, filename)
            gif_path = os.path.join(destination_folder, os.path.splitext(filename)[0] + '.gif')

            try:
                # Convert APNG to GIF using apnggif
                apnggif(png_path, gif_path)
                print(f'Converted {png_path} to {gif_path}')
            except Exception as e:
                print(f'Failed to convert {png_path}: {e}')

# Example usage
source_folder = os.getcwd()
destination_folder = os.path.join(source_folder, 'gifs')
convert_apng_to_gif(source_folder, destination_folder)
