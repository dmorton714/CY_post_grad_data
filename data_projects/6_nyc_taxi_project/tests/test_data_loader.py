from src import data_loader, config
import pandas as pd

def test_load_data():
    df = data_loader.load_data(config.DATA_PATH)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty