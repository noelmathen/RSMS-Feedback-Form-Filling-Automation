from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def select_feedback_options(driver):
    for question_number in range(1, 18):
        radio_name = f"{10887 + question_number}"  
        if question_number in range(1, 16):
            driver.find_element(By.CSS_SELECTOR, f"input[name='{radio_name}'][value='4']").click()
        elif question_number == 16 or question_number == 17:
            text_area_name = f"{10887 + question_number}"  
            driver.find_element(By.CSS_SELECTOR, f"textarea[name='{text_area_name}']").send_keys('-')
        time.sleep(0.07)

    driver.find_element(By.NAME, "B1").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Subject_Code")))
    time.sleep(2)


username = input("Enter your username: ")
password = input("Enter your password: ")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.rajagiritech.ac.in/stud/ktu/student/")
driver.find_element(By.NAME, "Userid").send_keys(username)
driver.find_element(By.NAME, "Password").send_keys(password)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.LINK_TEXT, "2023 END Semester Feedback ODD").click()
time.sleep(2)

while True:
    try:
        dropdown = Select(driver.find_element(By.NAME, "Subject_Code"))
        first_option = dropdown.first_selected_option.text
        dropdown.select_by_visible_text(first_option)
        select_feedback_options(driver)
    except:
        break

driver.quit()
