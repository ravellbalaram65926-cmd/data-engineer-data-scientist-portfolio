import pathlib


def test_project_scaffold():
    assert pathlib.Path("src/main.py").exists()
