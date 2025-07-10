import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)


def load_data(file_path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Loaded data with shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        raise
