## Separate Unit and Integration Tests

- **`Unit Tests`**: Isolated, fast tests that check individual functions/models.
    - Unit Test Example (Forecasting Models)
    - Tests Prophet, Holt’s, BSTS models for correctness
    - Mocks external dependencies to keep tests isolated.
- **`Integration Tests`**: Verify if components (e.g., database, APIs) work together.
    - Integration Test Example (Database Connection)
    - Tests if a database connection works and checks if data exists.
    - Uses pytest fixtures for setting up a database session.

## Naming Conventions

- Use test_*.py filenames.
- Functions should start with test_ for pytest to detect them.

## Fixture

✅ Pytest automatically injects sample_data into the test function.
✅ No need to call it manually!

## Run Tests

```sh
$ cd /mnt/Local/Git_Repo/PythonCodeHub

# Activate poetry venv
$ poetry shell

# Add Pytest lib
$ poetry add pytest

# Run all tests
$ poetry run pytest

# Run only unit tests:
$ poetry run pytest tests/unit/

(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub$ poetry run pytest tests/unit/test_module.py 
============================================================================================ test session starts =============================================================================================
platform linux -- Python 3.11.10, pytest-8.3.4, pluggy-1.5.0
rootdir: /mnt/Local/Git_Repo/PythonCodeHub
configfile: pyproject.toml
collected 1 item                                                                                                                                                                                             

tests/unit/test_module.py .                                                                                                                                                                            [100%]

============================================================================================= 1 passed in 0.08s ==============================================================================================
(pythoncodehub-py3.11) rga@rgavm:/mnt/Local/Git_Repo/PythonCodeHub$ pytest tests/unit/test_module.py 
============================================================================================ test session starts =============================================================================================
platform linux -- Python 3.11.10, pytest-8.3.4, pluggy-1.5.0
rootdir: /mnt/Local/Git_Repo/PythonCodeHub
configfile: pyproject.toml
collected 1 item                                                                                                                                                                                             

tests/unit/test_module.py .                                                                                                                                                                            [100%]

============================================================================================= 1 passed in 0.09s ==============================================================================================

# Run only integration tests
$ poetry run pytest tests/integration/
```