# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox(
    executable_path=r"c:\Users\nigga\code\python\100-days-of-code\geckodrivers\geckodriver.0.29.1.exe")

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# write script
script = "alert('Alert via selenium')"

# generate a alert via javascript
driver.execute_script(script)
