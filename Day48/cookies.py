from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for language selection to load and select English
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
).click()

# Wait for the big cookie to load
cookie_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

# Click the cookie repeatedly (just for fun)
for _ in range(100):
    cookie_button.click()
