import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("smarttrip")
logger.setLevel(logging.INFO)

# Evităm să adăugăm handler-ul de mai multe ori la reload
if not logger.handlers:
    file_handler = logging.FileHandler(LOG_DIR / "app.log")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)