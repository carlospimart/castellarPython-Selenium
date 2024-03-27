import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "edge":
        service = Service(executable_path="/home/domin/Desktop/Castellar/CastellarTestAutomation/drivers/msedgedriver")
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)

    driver.get("http://localhost:3000/")
    driver.maximize_window()
    request.cls.driver = driver

    yield # everything before this would be execute it at the beggining of the class,
          # everything after this at the end
    driver.close()


