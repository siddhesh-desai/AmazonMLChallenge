# from PIL import Image

# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# # Replace with your path
# print(pytesseract.image_to_string(Image.open(
#     'C:/Users/Siddhesh/Desktop/ML Challenge/b.jpg')))


import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set the path to the Tesseract executable (only required for Windows)
# For example: r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"  # Update this path if required
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def enhance_image_for_ocr(image_path):
    """
    Enhances the image to make it suitable for OCR by applying techniques like grayscale conversion,
    thresholding, and noise reduction.

    Parameters:
        image_path (str): Path to the local image file.

    Returns:
        enhanced_image (numpy.ndarray): Enhanced image ready for OCR.
    """
    # Load image from file
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to remove noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply adaptive thresholding for binarization
    enhanced_image = cv2.adaptiveThreshold(
        blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # cv2.imshow('Hi', enhanced_image)

    return enhanced_image


def ocr_from_image(image):
    """
    Performs OCR using Tesseract on the provided image.

    Parameters:
        image (numpy.ndarray): Image on which OCR is to be performed.

    Returns:
        extracted_text (str): The text extracted from the image.
    """
    # Convert image from OpenCV format to PIL format for pytesseract
    pil_image = Image.fromarray(image)

    # Perform OCR on the image using Tesseract
    extracted_text = pytesseract.image_to_string(pil_image)

    return extracted_text


def process_image_for_ocr(image_path):
    """
    Main function to process the image and extract text using Tesseract OCR.

    Parameters:
        image_path (str): Path to the local image file.

    Returns:
        extracted_text (str): The text extracted from the image.
    """
    # Step 1: Enhance image for OCR
    enhanced_image = enhance_image_for_ocr(image_path)

    cv2.imshow('Enhanced Image', enhanced_image)

    # Step 2: Perform OCR on the enhanced image
    extracted_text = ocr_from_image(enhanced_image)

    return extracted_text


# Example Usage
if __name__ == "__main__":
    # Provide the path to the image
    image_path = "b.jpg"

    # Extract text from the image
    extracted_text = process_image_for_ocr(image_path)

    # Output the extracted text
    print("Extracted Text:", extracted_text)
