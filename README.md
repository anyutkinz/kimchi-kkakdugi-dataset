# Kimchi-Kkakdugi Image Dataset Creation

*Dataset hosted on [Google Drive]()*

## Overview:
This project demonstrates the creation of a custom image dataset for **kimchi** (fermented cabbage) and **kkakdugi** (cubed radish kimchi), two traditional Korean dishes. The dataset is designed for educational or small-scale machine learning projects, particularly for training CNNs. The final dataset contains **1,000 images per class**, generated through web scraping, augmentation, and preprocessing.

### Key Features:
- **Scraping**: Automated image collection from Google Images using Selenium.
- **Augmentation**: Image diversity expansion using rotations, flips, brightness adjustments, and more.
- **Preprocessing**: Standardization of image sizes (e.g., 64x64) and normalization.
- **Ethical Compliance**: Only images marked as "public domain" were scraped.

---

## Dataset Details:
- **Classes**: `kimchi` and `kkakdugi`.
- **Total Images**: 2,000 (1,000 per class).
- **Format**: JPEG images, preprocessed and augmented.
- **License**: Public domain/Creative Commons (respecting original image rights).
- **Access**: [Download from Google Drive]().

---

## Prerequisites:
- Python 3.6+
- Libraries:
  ```bash
  pip install selenium pillow uuid

## Project Structure:

scripts/                 # Helper scripts
├── scraper.py           # Image scraping from Google
├── augment_images.py    # Image augmentation
├── rename_images.py     # File renaming
└── preprocess_images.py # Image resizing/normalization

data/
├── raw/                 # Raw scraped images
│   ├── kimchi/
│   └── kkakdugi/
├── augmented/           # Augmented images
│   ├── kimchi/
│   └── kkakdugi/
└── splitted/        # Processed images (ready for ML)
    ├── train/
    ├── val/
    └── test/

## Notes:

1) For detaild, refer to scripts - I left detailed comments!
2) Though I used public domain for scraping, I do not claim that this dataset is MINE. This project is created only for educational purposes. 

