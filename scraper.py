from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests
import uuid

# This function scrapes images from Google Images using Selenium and saves them to a specified folder
def scrape_google_images_selenium(query, folder_name, num_images, usage_rights="cc_publicdomain"):
    """
    Scrape images from Google Images using Selenium and save them to a specified folder.
    Args:
        query (str): Search term for Google Images.
        folder_name (str): Name of the folder to save images.
        num_images (int): Number of images to download.
        usage_rights (str): Usage rights filter for Google Images (default is "cc_publicdomain").
    """
    # Set up Chrome browser options for Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run browser in headless mode (no GUI).

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=options)

    # Prepare the search query and construct the Google Images URL
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?tbm=isch&q={query}&tbs=sur:{usage_rights}"

    print(f"Opening browser for URL: {url}")
    driver.get(url)
    time.sleep(5)  # Wait for the page to load (otherwise images may not load)

    # Scroll down the page to load more images (simulate user scrolling)
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)

    # Find all <img> tags on the page.
    img_tags = driver.find_elements(By.TAG_NAME, 'img')
    print(f"Found {len(img_tags)} images on the page.")

    # Create the target folder if it does not exist
    os.makedirs(folder_name, exist_ok=True)

    count = 0  # Counter for downloaded images

    # Iterate over all found image tags
    for img_tag in img_tags:
        try:
            # Get the image URL from the 'src' attribute
            img_url = img_tag.get_attribute('src')

            # Skip if the URL is invalid or not a real image
            if not img_url or "http" not in img_url:
                print("Invalid image URL, skipping...")
                continue

            print(f"Downloading image {count + 1} from: {img_url}")

            # Download the image content using requests
            img_data = requests.get(img_url).content

            # Generate a random unique filename for each image to avoid overwriting
            random_name = f"{uuid.uuid4().hex}.jpg"
            file_path = os.path.join(folder_name, random_name)

            # Save the image to disk
            with open(file_path, 'wb') as f:
                f.write(img_data)

            count += 1
            print(f"Saved image {count}: {file_path}")

            # Stop if we've reached the desired number of images
            if count >= num_images:
                break

        except Exception as e:
            # Handle any errors during download and continue with the next image
            print(f"Error downloading image: {e}")

    # Close the Selenium browser session
    driver.quit()
    print(f"Scraping completed! {count} images saved in '{folder_name}'.")
