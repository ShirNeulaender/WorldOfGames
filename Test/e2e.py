from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scores_service():
    my_driver = webdriver.Chrome(executable_path="C:/Users/Shir/Desktop/project-0109/project/chromedriver.exe")
    wait = WebDriverWait(my_driver, 20)

    my_driver.get("http://127.0.0.1:34567/")
    score = int(wait.until(EC.visibility_of_element_located((By.ID, "score"))).text)
    if 1 <= score <= 100:
        return False
    else:
        return True


def main_function():
    test_scores_service()
    if test_scores_service() == False:
        exit(-1)
    else:

        exit(0)
