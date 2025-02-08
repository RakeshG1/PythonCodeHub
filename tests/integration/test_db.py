@pytest.fixture
def db_connection():
    conn = setup_database()  # Some function that sets up DB
    yield conn  # Return the connection to the test
    conn.close()  # Cleanup after test
