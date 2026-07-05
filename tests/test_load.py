import pandas as pd
from unittest.mock import patch

from  app.load import load

@patch("pandas.DataFrame.to_sql")

def test_load_to_sql(mock_to_sql):
    df = pd.DataFrame({
        "nama": ["Aldi"]
    })

    load(df)

    mock_to_sql.assert_called_once()
    