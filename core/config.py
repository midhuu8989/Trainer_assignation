import os
from datetime import datetime

BASE_DATA_PATH = os.getenv("DATA_PATH", "./data")
CURRENT_QUARTER = os.getenv("CURRENT_QUARTER", None)

def get_current_quarter() -> str:
    if CURRENT_QUARTER:
        return CURRENT_QUARTER

    m = datetime.now().month
    y = datetime.now().year % 100

    if m <= 3:
        q = "JFM"
    elif m <= 6:
        q = "AMJ"
    elif m <= 9:
        q = "JAS"
    else:
        q = "OND"

    return f"{q}{y}"
