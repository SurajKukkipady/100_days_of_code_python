from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

#driver.close()  # This will close the current window, but the browser will remain open if detach is set to True
driver.quit()  # This will close the browser and end the session

