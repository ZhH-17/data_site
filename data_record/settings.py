import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = "data_record/static/data_record"
DATA_BASEPATH = os.path.join(BASE_DIR, MEDIA_ROOT)
