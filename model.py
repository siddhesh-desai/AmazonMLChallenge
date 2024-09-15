import pytesseract
import cv2
import re
import pandas as pd
from constants import allowed_units, entity_unit_map

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def extract_text_from_image(image_path):
    """Extract text from an image using OCR."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray)


def extract_entity_value(text, entity_name):
    """Extract the entity value (e.g., weight, volume) from the OCR-extracted text."""
    unit_list = entity_unit_map.get(entity_name, [])

    # Regex for extracting numeric values with possible decimal points
    pattern = r"(\d+\.?\d*)\s*(" + '|'.join(unit_list) + ")"
    match = re.search(pattern, text.lower())

    if match:
        value, unit = match.groups()
        return f"{float(value)} {unit}"
    return ""


def process_image(image_path, entity_name):
    """Extract the entity value from the image."""
    text = extract_text_from_image(image_path)
    return extract_entity_value(text, entity_name)
