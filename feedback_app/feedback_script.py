from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

def select_feedback_options(driver):
    feedback_messages = []

    for question_number in range(1, 18):
        try:
            radio_name = f"{10904 + question_number}"  
            if question_number in range(1, 16):
                driver.find_element(By.CSS_SELECTOR, f"input[name='{radio_name}'][value='4']").click()
            elif question_number == 16 or question_number == 17:
                text_area_name = f"{10904 + question_number}"  
                driver.find_element(By.CSS_SELECTOR, f"textarea[name='{text_area_name}']").send_keys('-')
            time.sleep(0.07)
        except NoSuchElementException:
            feedback_messages.append(f"Element for question {question_number} not found.")

    try:
        driver.find_element(By.NAME, "B1").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Subject_Code")))
        time.sleep(2)
    except NoSuchElementException:
        feedback_messages.append("Button or Subject Code input not found.")

    return feedback_messages

def run_feedback_script(username, password):
    feedback_messages = []

    try:
        print("Logging in to your rsms account...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.rajagiritech.ac.in/stud/ktu/student/")
        driver.find_element(By.NAME, "Userid").send_keys(username)
        driver.find_element(By.NAME, "Password").send_keys(password)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        try:
            driver.find_element(By.LINK_TEXT, "2024 Mid Semester Feedback Even").click()
        except NoSuchElementException:
            feedback_messages.append("Incorrect credentials")
            return feedback_messages
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Subject_Code")))
        feedback_messages.append("Successfully logged in...\n")

        while True:
            try:
                dropdown = Select(driver.find_element(By.NAME, "Subject_Code"))
                first_option = dropdown.first_selected_option.text
                feedback_messages.append(f"Feedback for {first_option} completed")
                dropdown.select_by_visible_text(first_option)
                feedback_messages.extend(select_feedback_options(driver))
            except NoSuchElementException:
                feedback_messages.append("Feedback submission completed!.")
                break
            except Exception as e:
                feedback_messages.append(f"An unexpected error occurred: {e}")
                break
    finally:
        driver.quit()

    return feedback_messages
