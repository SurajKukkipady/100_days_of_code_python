from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = driver.find_elements(By.CSS_SELECTOR, "div.event-widget ul.menu li")

# Extract and print event date and title
event_list = []
for event in events:
    date = event.find_element(By.TAG_NAME, "time").text
    title = event.find_element(By.TAG_NAME, "a").text
    event_list.append((date, title))

# Print the extracted events
for date, title in event_list:
    print(f"{date} - {title}")

driver.quit()  # This will close the browser and end the session