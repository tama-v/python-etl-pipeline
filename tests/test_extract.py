import pandas as pd
from unittest.mock import patch

from app.extract import extract

@patch("pandas.read_csv")
def test_extract_calls_read_csv(mock_read_csv):
    dummy_df = pd.DataFrame({
        "Nama": ["Aldi", "Budi"]
    })
    mock_read_csv.return_value = dummy_df

    hasil = extract()

    mock_read_csv.assert_called_once()

    assert hasil.equals(dummy_df)

    

    