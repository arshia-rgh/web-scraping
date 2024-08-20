import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()

base_url: Final = "https://bama.ir/"  # currently only for bama website

# Only "car", "motorcycle", "truck" allowed
CATEGORIES = os.getenv("CATEGORIES", "")

BRANDS = os.getenv("BRANDS", "")

categories_list = CATEGORIES.split(",") if CATEGORIES else []
brands_list = BRANDS.split(",") if BRANDS else []

if not isinstance(categories_list, list):
    raise ValueError("CATEGORIES must be an array")
if not isinstance(brands_list, list):
    raise ValueError("BRANDS must be an array")
