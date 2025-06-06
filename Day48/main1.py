from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()  # Open browser in full screen

driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = driver.find_element(By.NAME, "search")
search.send_keys("Python (programming language)", Keys.ENTER)

driver.quit()
