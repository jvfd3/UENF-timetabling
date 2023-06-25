# https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file
# pytest -v  test_main.py::test_read_and_print_string
import requests
import pytest

def test_favicon():
    website_url = "http://127.0.0.1:8000"  # URL of the website

    # Make a request to the website URL
    response = requests.get(website_url)

    # Check if the response is successful (status code 200)
    assert response.status_code == 200, f"Failed to access {website_url}"

    # Check if the favicon exists
    favicon_url = f"{website_url}/static/images/favicon.ico."
    response = requests.head(favicon_url)

    # Check if the favicon URL returns a successful response (status code 200 or 304)
    assert response.status_code in (200, 304), f"Favicon does not exist at {favicon_url}"

    # Ensure it is a valid favicon
    content_type = response.headers.get("Content-Type")
    assert content_type == "image/x-icon", f"Invalid favicon content type: {content_type}"
