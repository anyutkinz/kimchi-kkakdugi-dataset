import os
import uuid

def rename_images(folder_path):
    """
    Renames all images in the specified folder to the format image_{count}.jpg

    Args:
        folder_path (str): The path to the folder containing the images
    """

    # List of valid image file extensions to process
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

    count = 1  # Counter for renaming images

    try:
        # Get a sorted list of files in the folder that are images
        files = sorted([
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f)) and
               any(f.lower().endswith(ext) for ext in image_extensions)
        ])
    except FileNotFoundError:
        # Print error if the folder does not exist and exit the function
        print(f"Error: Folder '{folder_path}' not found")
        return

    for filename in files:
        # Get the file extension in lower case
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in image_extensions:
            # Generate a new filename in the format kimchi__image_{count}.jpg
            # You can change this pattern as needed for your dataset
            new_filename = f"kimchi__image_{count}.jpg"

            # Alternatively, you can use a UUID for unique filenames
            # new_filename = f"{uuid.uuid4().hex}.jpg"

            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)

            try:
                # Rename the file
                os.rename(old_filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")
                count += 1
            except OSError as e:
                # Print error if renaming fails
                print(f"Error renaming '{filename}': {e}")
        else:
            # Skip files that are not recognized image types
            print(f"Skipping non-image file: '{filename}'")

    print("Renaming complete")
