import pytest

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_data(sample_data):
    assert sample_data["age"] == 30  # Uses fixture data