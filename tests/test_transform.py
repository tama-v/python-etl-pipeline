import pandas as pd

from app.transform import transform




def test_remove_duplicates():
    df = pd.DataFrame({
        "Nama": ["Aldi", "Aldi", "Budi", "Citra"]
    })

    hasil = transform(df)

    assert hasil.shape[1] == 1


def test_column_lowercase():
    df = pd.DataFrame({
        "Nama": ["Aldi", "Budi"]
    })

    hasil = transform(df)

    assert hasil.columns.tolist() == ["nama"]

def test_return_dataframe():

    df = pd.DataFrame({
        "Nama": ["Aldi", "Budi"]
    })

    hasil = transform(df)

    assert isinstance(hasil, pd.DataFrame)


def test_column_count():

    df = pd.DataFrame({
        "Nama": ["Aldi", "Budi"]
    })

    hasil = transform(df)

    assert len(hasil.columns) == 1