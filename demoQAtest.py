from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains


service=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def test_case1():
    driver.get("https://demoqa.com/elements")
    time.sleep(5)

    driver.maximize_window()

    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Alex")
    time.sleep(2)

def test_case2():
    driver.get("https://demoqa.com/text-box")
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Alex")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("QAtest@email.com")
    time.sleep(2)

    driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("Street Name, USA")
    time.sleep(2)

    driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Same as Current")
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[@id='submit']").click()
    time.sleep(4)

    #Highlight text :

    element2 = driver.find_element(By.XPATH, "//p[@id='email']")
    driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element2)
    time.sleep(5)

    element3 = driver.find_element(By.XPATH, "//p[@id='currentAddress']")
    driver.execute_script("arguments[0].style.backgroundColor = 'red';", element3)
    time.sleep(5)

    element3 = driver.find_element(By.XPATH, "//p[@id='name']")
    driver.execute_script("arguments[0].style.backgroundColor = 'blue';", element3)
    time.sleep(5)

def test_case3():
    driver.get("https://demoqa.com/checkbox")
    time.sleep(5)

    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/span[1]/label[1]/span[1]/*[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/span[1]/button[1]/*[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/ol[1]/li[3]/span[1]/button[1]/*[1]").click()
    time.sleep(3)

def test_case4():
    driver.get("https://demoqa.com/radio-button")
    time.sleep(5)

    driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//label[contains(text(),'Impressive')]").click()
    time.sleep(2)

def test_case5():
    driver.get("https://demoqa.com/webtables")
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Alex")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Tester")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("testing@email.com")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='age']").send_keys("30")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("300000")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='department']").send_keys("IT")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='submit']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='searchBox']").send_keys("Alex")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, window.scrollY + 250)")
    time.sleep(3)

    element4 = driver.find_element(By.XPATH, "//div[contains(text(),'Alex')]")
    driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element4)
    time.sleep(5)

def test_case6():
    driver.get("https://demoqa.com/buttons")
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, window.scrollY + 250)")
    time.sleep(3)

    element6 = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
    actions = ActionChains(driver)
    actions.double_click(element6).perform()
    time.sleep(5)

    element7 = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
    actions = ActionChains(driver)
    actions.context_click(element7).perform()
    time.sleep(5)

    #driver.find_element(By.XPATH, "//button[@id='I9MMf']").click()
    #time.sleep(2)

def test_case7():
    driver.get("https://demoqa.com/alerts")
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[@id='timerAlertButton']").click()
    time.sleep(6)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, window.scrollY + 250)")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
    time.sleep(3)

    prompt = driver.switch_to.alert

    # Send keys (type text) into the input prompt
    prompt.send_keys("Alex")

    # Accept the input prompt (click "OK")
    prompt.accept()
    time.sleep(5)

    element8 = driver.find_element(By.XPATH, "//span[@id='promptResult']")
    driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element8)
    time.sleep(5)

def test_case8():
    driver.get("https://demoqa.com/accordian")
    time.sleep(5)

    driver.find_element(By.XPATH, "//div[@id='section1Heading']").click()
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, window.scrollY + 250)")
    time.sleep(3)

    driver.find_element(By.XPATH, "//div[@id='section2Heading']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//div[@id='section2Heading']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@id='section3Heading']").click()
    time.sleep(3)




    driver.close()
    driver.quit()