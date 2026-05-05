# iTunes API Test Suite

This API test suite tests the iTunes API endpoints using Python, pytest, and the requests library. Built as a portfolio project to demonstrate practical Python testing skills in a real-world context. Tests cover valid inputs, edge cases like empty strings and special characters, error conditions, schema validation, and parameter behavior. The repo demonstrates important concepts like DRY, AAA pattern test cases, boundary conditions, error handling, and offline mock testing.

---

## Prerequisites

- Python 3.9+
- pip
- Git

---

## Setup

**1. Clone the repository:**
```bash
git clone https://github.pie.apple.com/nicholas-w-burt/itunes-api-test-suite.git
cd itunes-api-test-suite
```

**2. Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## Running the Tests

**Run all tests (live + offline):**
```bash
python3 -m pytest -v
```

**Run only offline mock tests (no internet required):**
```bash
python3 -m pytest tests/test_search_mock.py -v
```

**Run only live integration tests:**
```bash
python3 -m pytest tests/test_search.py tests/test_lookup.py tests/test_error_handling.py -v
```

**Run a specific test file:**
```bash
python3 -m pytest tests/test_search.py -v
python3 -m pytest tests/test_lookup.py -v
python3 -m pytest tests/test_error_handling.py -v
```

**Run a specific test:**
```bash
python3 -m pytest tests/test_search.py::test_valid_search_returns_200 -v
```

**Generate an HTML report:**
```bash
python3 -m pytest --html=report.html -v
```

---

## Project Structure

```
itunes-api-test-suite/
├── .github/
│   └── workflows/
│       └── tests.yml           # GitHub Actions CI workflow
├── tests/
│   ├── test_search.py          # Search endpoint tests (live)
│   ├── test_lookup.py          # Lookup endpoint tests (live)
│   ├── test_error_handling.py  # Error handling and edge case tests (live)
│   └── test_search_mock.py     # Offline mock tests (no internet required)
├── utils/
│   └── api_client.py           # Reusable API client wrapper
├── conftest.py                 # Shared fixtures and constants
├── requirements.txt
└── README.md
```

---

## Test Coverage

### `test_search.py` (6 tests) — Live Integration
Tests the iTunes Search API endpoint (`/search`) against the live API.

| Test | What it validates |
|---|---|
| `test_valid_search_returns_200` | Valid search returns a 200 status code |
| `test_results_contain_expected_fields` | Response contains expected fields across all results |
| `test_limit_param_caps_results` | `limit` parameter correctly caps the number of results |
| `test_media_param_filters_correctly` | `media` parameter filters results to the correct type |
| `test_special_characters_handled` | Special characters and accented characters are URL encoded correctly |
| `test_empty_search_term` | Empty search term returns zero results gracefully |

### `test_lookup.py` (3 tests) — Live Integration
Tests the iTunes Lookup API endpoint (`/lookup`) against the live API.

| Test | What it validates |
|---|---|
| `test_valid_lookup_returns_correct_entity` | Valid artist ID returns the correct entity with matching fields |
| `test_response_schema_matches_expected` | Track lookup response contains all expected schema fields |
| `test_invalid_id_returns_expected_response` | Invalid ID returns a 200 with empty results |

### `test_error_handling.py` (2 tests) — Live Integration
Tests error conditions and API robustness against the live API.

| Test | What it validates |
|---|---|
| `test_overly_long_id_raises_exception` | An overly long ID triggers a 400 error and raises an exception |
| `test_response_time_within_threshold` | Search response time is within a 5 second acceptable threshold |

### `test_search_mock.py` (5 tests) — Offline Unit Tests
Tests using `pytest-mock` to intercept `requests.get()` -- no internet connection required. Covers scenarios impossible to trigger with a live API.

| Test | What it validates |
|---|---|
| `test_search_returns_200_offline` | Client correctly handles and returns a 200 response |
| `test_search_returns_500_offline` | Client raises an exception when server returns a 500 error |
| `test_search_connection_error_offline` | Client raises an exception when connection fails |
| `test_search_timeout_offline` | Client raises an exception when request times out |
| `test_results_not_contain_expected_fields` | Missing fields in response are correctly detected |

---

## Key Concepts Demonstrated

- **DRY (Don't Repeat Yourself)** -- Shared API client, fixtures, and constants eliminate duplication across test files
- **Encapsulation** -- HTTP logic is hidden inside `ApiClient`, test files interact only through clean public methods
- **AAA Pattern** -- All tests follow Arrange, Act, Assert structure
- **Boundary Conditions** -- Deliberate use of `<=` vs `==` for result count assertions
- **Exception Handling** -- Specific to broad exception ordering with exception chaining (`from e`)
- **pytest Fixtures** -- Shared `client` fixture auto-injected by pytest via `conftest.py`
- **pytest.raises** -- Used to assert expected exceptions for error conditions
- **Mocking (pytest-mock)** -- `requests.get()` intercepted at `utils.api_client` scope to enable offline testing and simulate error scenarios
- **Integration vs Unit Tests** -- Live tests validate real API behavior; mock tests validate client logic in isolation

---

## CI/CD

A GitHub Actions workflow is configured at `.github/workflows/tests.yml`. It runs the full test suite automatically on every push using Python 3.9 on `ubuntu-latest`.

> **Note:** GitHub Actions must be enabled on the GitHub Enterprise instance by an administrator for the workflow to execute automatically. The workflow file is committed and ready to run once enabled.

To run manually:
```bash
python3 -m pytest -v
```

---

## Notes

- **Live integration tests** require an active internet connection to reach `itunes.apple.com`
- **Offline mock tests** (`test_search_mock.py`) run without any network connection
- Response time tests may vary depending on network conditions and DNS cache state
- The `venv/` directory is excluded from version control via `.gitignore`
- Generate `report.html` locally -- it is also excluded from version control
