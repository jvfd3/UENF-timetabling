import requests

def test_website_access():
    url = "http://127.0.0.1:8000/"  # Replace with the URL of the website you want to test
    response = requests.get(url)
    assert response.status_code == 200

