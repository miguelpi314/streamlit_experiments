from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


def test_user_interface():
    options = Options()
    options.add_argument("--headless")
    with webdriver.Firefox(options=options) as driver:
        url = "http://127.0.0.1:8501"
        driver.get(url)
        time.sleep(5)
        html = driver.page_source

    assert "Add numbers" in html
    assert "First Number" in html
    assert "Second Number" in html
