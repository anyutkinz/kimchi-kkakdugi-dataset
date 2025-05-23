import os
import os
from PIL import Image, ImageOps

def preprocess_images(input_folder, output_folder, target_size=(64, 64)):
    """
    Preprocess all images in the input_folder and save them to output_folder
    Steps include resizing, normalization (autocontrast), and color conversion
    Args:
        input_folder (str): Path to the folder containing original images
        output_folder (str): Path to the folder where processed images will be saved
        target_size (tuple): Desired image size as (width, height)
    """

    # Create the output folder if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    # List all image files in the input folder with supported extensions
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if len(image_files) == 0:
        # Print a message if no images are found and exit the function
        print("No images found in the input folder :(")
        return

    print(f"Processing {len(image_files)} images...")

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        # Open the image using PIL
        with Image.open(image_path) as img:
            # Resize the image to the target size while keeping the aspect ratio and center cropping
            img = ImageOps.fit(img, target_size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))

            # Apply autocontrast for normalization (improves contrast and dynamic range)
            img = ImageOps.autocontrast(img)

            # Convert the image to RGB mode if it is not already (ensures consistency)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Save the processed image to the output folder
            img.save(output_path)

    print(f"Processed {len(image_files)} images and saved to {output_folder}!")