import pandas as pd
from unittest.mock import patch, MagicMock

from  app.load import load

@patch("app.load.postgres.get_engine")
@patch("pandas.DataFrame.to_sql")

def test_load_to_sql(mock_to_sql, mock_get_engine):

    mock_get_engine.return_value = MagicMock()

    df = pd.DataFrame({
        "nama": ["Aldi"]
    })

    load(df)

    mock_get_engine.assert_called_once()

    mock_to_sql.assert_called_once()
    