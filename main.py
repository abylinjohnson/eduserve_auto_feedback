from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def feedback(driver):
    rows = driver.find_element(By.TAG_NAME, "tr")
    row_length = int(int(rows.size['height'])/5)
    for i in range(1, row_length+1):
        driver.find_element(By.XPATH, f'/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[{i}]/td[5]/div/ul/li[5]').click()
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/div/input').click()
    return driver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://eduserve.karunya.edu/")
driver.find_element(By.ID, 'mainContent_Login1_UserName').send_keys("Your User Name")
driver.find_element(By.ID, 'mainContent_Login1_Password').send_keys("Your Password")
driver.find_element(By.ID, 'mainContent_Login1_LoginButton').click()
if(driver.title == "Hourly Feedback"):
    driver = feedback(driver)
class_atd = driver.find_element(By.ID, 'mainContent_LBLCLASS').text
assem_atd = driver.find_element(By.ID, 'mainContent_LBLCLASS').text
print("Class Attendance: " + class_atd)
print("Assembly Attendance: " + assem_atd)