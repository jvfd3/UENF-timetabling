import pytest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def browser():
    # Configurar o WebDriver para o teste
    driver = webdriver.Chrome()
    yield driver
    # Fechar o navegador após o teste
    driver.quit()

def test_title(browser):
    # Navegar para o URL do sistema
    browser.get("http://127.0.0.1:8000/")

    # Verificar se o título da página é o esperado
    assert browser.title == "TimeTabling App"


def test_check_new_ui_segment_class(browser):
    # Navigate to the website URL
    browser.get("http://127.0.0.1:8000")

    # Fill the "turma_id" field
    turma_id_input = browser.find_element_by_name("turma_id")
    turma_id_input.send_keys("123")

    # Fill the "time_slot" field
    time_slot_input = browser.find_element_by_name("time_slot")
    time_slot_input.send_keys("900")
    time.sleep(10)  # Pause for 10 seconds

    # Get the initial number of elements with "ui segment" class
    initial_segment_count = len(browser.find_elements_by_css_selector(".ui.segment"))

    # Locate and click the "Add" button
    add_button = browser.find_element_by_css_selector(".ui.blue.button")
    add_button.click()

    # Get the updated number of elements with "ui segment" class
    updated_segment_count = len(browser.find_elements_by_css_selector(".ui.segment"))

    # Assert that the number of elements with "ui segment" class has increased
    assert updated_segment_count > initial_segment_count
