import re
import constants
import os
import requests
import pandas as pd
import multiprocessing
import time
from time import time as timer
from tqdm import tqdm
import numpy as np
from pathlib import Path
from functools import partial
import requests
import urllib
from PIL import Image


def common_mistake(unit):
    if unit in constants.allowed_units:
        return unit
    if unit.replace('ter', 'tre') in constants.allowed_units:
        return unit.replace('ter', 'tre')
    if unit.replace('feet', 'foot') in constants.allowed_units:
        return unit.replace('feet', 'foot')
    return unit


def parse_string(s):
    s_stripped = "" if s == None or str(s) == 'nan' else s.strip()
    if s_stripped == "":
        return None, None
    pattern = re.compile(r'^-?\d+(\.\d+)?\s+[a-zA-Z\s]+$')
    if not pattern.match(s_stripped):
        raise ValueError("Invalid format in {}".format(s))
    parts = s_stripped.split(maxsplit=1)
    number = float(parts[0])
    unit = common_mistake(parts[1])
    if unit not in constants.allowed_units:
        raise ValueError("Invalid unit [{}] found in {}. Allowed units: {}".format(
            unit, s, constants.allowed_units))
    return number, unit


def create_placeholder_image(image_save_path):
    try:
        placeholder_image = Image.new('RGB', (100, 100), color='black')
        placeholder_image.save(image_save_path)
    except Exception as e:
        return


def download_image(image_link, save_folder, retries=3, delay=3, index=None):
    if not isinstance(image_link, str):
        return

    # filename = Path(image_link).name
    filename = f'image_{index}.jpg'
    image_save_path = os.path.join(save_folder, filename)

    if os.path.exists(image_save_path):
        return

    for _ in range(retries):
        try:
            urllib.request.urlretrieve(image_link, image_save_path)
            return
        except:
            time.sleep(delay)

    # Create a black placeholder image for invalid links/images
    create_placeholder_image(image_save_path)


# def download_images(image_links, download_folder, allow_multiprocessing=False):
#     if not os.path.exists(download_folder):
#         os.makedirs(download_folder)

#     if allow_multiprocessing:
#         download_image_partial = partial(
#             download_image, save_folder=download_folder, retries=3, delay=3)

#         with multiprocessing.Pool(64) as pool:
#             list(tqdm(pool.imap(download_image_partial,
#                  image_links), total=len(image_links)))
#             pool.close()
#             pool.join()
#     else:
#         for image_link in tqdm(image_links, total=len(image_links)):
#             download_image(
#                 image_link, save_folder=download_folder, retries=3, delay=3)

def download_images(image_links, download_folder, allow_multiprocessing=False):
    """Download images and save them in the format of image_{index}.jpg."""
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    if allow_multiprocessing:
        # Prepare the partial function with multiprocessing
        download_image_partial = partial(
            download_image, save_folder=download_folder, retries=3, delay=3)

        with multiprocessing.Pool(64) as pool:
            # Include the index in the list passed to the pool
            args = [(image_links[i], download_folder, 3, 3, i)
                    for i in range(len(image_links))]
            list(tqdm(pool.imap(lambda x: download_image(
                *x), args), total=len(image_links)))
            pool.close()
            pool.join()
    else:
        for i, image_link in enumerate(tqdm(image_links, total=len(image_links))):
            # Pass the index to the download_image function
            download_image(image_link, save_folder=download_folder,
                           retries=3, delay=3, index=i)
