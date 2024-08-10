from typing import Final
import os
from dotenv import load_dotenv

load_dotenv()

base_url: Final = "https://bama.ir/"  # currently only for bama website

# Only "car", "motorcycle", "truck" allowed
CATEGORIES = os.getenv("CATEGORIES")

BRANDS = os.getenv("BRANDS")
