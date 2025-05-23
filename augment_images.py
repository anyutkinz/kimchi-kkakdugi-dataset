import os
from PIL import Image, ImageEnhance, ImageOps
import random

def augment_image(image):
    """
    Apply random augmentation to an input PIL Image
    Returns a modified image with randomized transformations
    """
    
    # Random rotation between -45 and 45 degrees (50% probability)
    if random.random() > 0.5:
        angle = random.randint(-45, 45)
        image = image.rotate(angle)  # Fill empty areas with black

    # Horizontal flip with 50% probability
    if random.random() > 0.5:
        image = ImageOps.mirror(image)

    # Vertical flip with 50% probability
    if random.random() > 0.5:
        image = ImageOps.flip(image)

    # Random brightness adjustment (50% probability)
    # Factor <1 darkens, >1 brightens (range: 0.8-1.5)
    if random.random() > 0.5:
        enhancer = ImageEnhance.Brightness(image)
        factor = random.uniform(0.8, 1.5)
        image = enhancer.enhance(factor)

    # Random contrast adjustment (50% probability)
    # Factor <1 reduces contrast, >1 increases (range: 0.7-1.4)
    if random.random() > 0.5:
        enhancer = ImageEnhance.Contrast(image)
        factor = random.uniform(0.7, 1.4)
        image = enhancer.enhance(factor)

    # Random zoom/crop (50% probability)
    # Simulates zoom-in by cropping and resizing back to original dimensions
    if random.random() > 0.5:
        zoom_factor = random.uniform(1.1, 1.5)  # 10-50% zoom
        width, height = image.size
        # Calculate new dimensions after zoom
        new_w = int(width / zoom_factor)
        new_h = int(height / zoom_factor)
        # Center crop coordinates
        left = (width - new_w) // 2
        right = left + new_w
        top = (height - new_h) // 2
        bottom = top + new_h
        # Crop and resize back to original size
        image = image.crop((left, top, right, bottom))
        image = image.resize((width, height), Image.LANCZOS)  # High-quality resampling

    return image

def save_augmented_images(folder_path, target_count):
    """
    Augments images in a folder until reaching target_count images
    Preserves original images and adds new augmented versions
    """
    
    # Get list of image files in the folder
    files = [f for f in os.listdir(folder_path) 
            if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

    if len(files) == 0:
        print("No images found in folder - cannot augment")
        return

    print(f"Found {len(files)} images. Augmenting to {target_count}...")

    current_count = len(files)
    
    # Continue augmenting until we reach target count
    while current_count < target_count:
        # Randomly select an original image to augment
        img_name = random.choice(files)
        img_path = os.path.join(folder_path, img_name)
        
        try:
            # Open and augment the image
            with Image.open(img_path) as img:
                augmented_img = augment_image(img)
                
                # Generate new filename with incrementing counter
                new_img_name = f"augmented_{current_count + 1}.jpg"
                new_img_path = os.path.join(folder_path, new_img_name)
                
                # Save as JPG to maintain quality
                augmented_img.save(new_img_path)
                print(f"Created: {new_img_name}")
                current_count += 1
                
        except Exception as e:
            print(f"Error processing {img_name}: {str(e)}")

    print(f"Augmentation complete! Total images: {current_count}")
