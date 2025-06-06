from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_div = driver.find_element(By.ID, "articlecount")
article_number = article_div.find_elements(By.TAG_NAME, "a")[1].text

# Print the number of English articles
print(article_number)

# Clean up
driver.quit()