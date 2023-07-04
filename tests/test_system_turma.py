# https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/
# https://realpython.com/python-web-scraping-practical-introduction/#interact-with-html-forms
# https://www.devmedia.com.br/teste-de-integracao-na-pratica/31877#1
import pytest
import requests

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
#lambdatest setup and opening the desired website
from bs4 import BeautifulSoup

def _test_adicionar_turma():

    browser = webdriver.Chrome()

    url = "http://127.0.0.1:8000/"

    browser.get(url)
    browser.maximize_window()

    turma_id_input = browser.find_element(By.NAME, "turma_id")
    turma_id_input.send_keys("388777")

    time_slot_input = browser.find_element(By.NAME, "time_slot")
    time_slot_input.send_keys("156")

    #initial_segment_count = browser.find_element(By.CSS_SELECTOR, 'time_slot_list')

    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> elements with class name 'uisegment'
    divs = soup.find_all('div', class_='ui segment')

    # Count the number of <div> elements found
    count = len(divs)

    ## https://selenium-python.readthedocs.io/locating-elements.html

    #continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
    continue_button = browser.find_element(By.XPATH, '//button')
    continue_button.click()


    response = requests.get(url)
    #updated_segment_count = len(browser.find_element(By.CLASS_NAME, "uisegment"))
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> elements with class name 'uisegment'
    new_divs = soup.find_all('div', class_='ui segment')

    # Count the number of <div> elements found
    new_count = len(new_divs)
    #asserting that the browser title is correct
      # Assert that the number of elements with "ui segment" class has increased
    assert new_count == count + 1

    #closing the browser
    browser.quit()
