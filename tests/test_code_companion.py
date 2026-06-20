import pytest
from code_companion import create_code_companion, FileExplanation

@pytest.fixture
def files():
    return [
        FileExplanation("file1", "This is file 1", "Technical details for file 1"),
        FileExplanation("file2", "This is file 2", "Technical details for file 2"),
    ]

def test_get_file_explanation(files):
    code_companion = create_code_companion(files)
    assert code_companion.get_file_explanation("file1") == "This is file 1"
    assert code_companion.get_file_explanation("file2") == "This is file 2"
    assert code_companion.get_file_explanation("file3") is None

def test_get_technical_details(files):
    code_companion = create_code_companion(files)
    assert code_companion.get_technical_details("file1") == "Technical details for file 1"
    assert code_companion.get_technical_details("file2") == "Technical details for file 2"
    assert code_companion.get_technical_details("file3") is None

def test_update_progress(files):
    code_companion = create_code_companion(files)
    code_companion.update_progress()
    assert code_companion.progress == 1
    code_companion.update_progress()
    assert code_companion.progress == 2

def test_get_progress_percentage(files):
    code_companion = create_code_companion(files)
    assert code_companion.get_progress_percentage() == 0
    code_companion.update_progress()
    assert code_companion.get_progress_percentage() == 50
    code_companion.update_progress()
    assert code_companion.get_progress_percentage() == 100
