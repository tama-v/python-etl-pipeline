from app.utils.path import DATA_DIR, LOG_DIR, TEST_DIR


def test_data_dir_name():
    assert DATA_DIR.name == "data"

def test_log_dir_name():
    assert LOG_DIR.name == "logs"

def test_test_dir_name():
    assert TEST_DIR.name == "tests"