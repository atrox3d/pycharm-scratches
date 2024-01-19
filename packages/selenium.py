# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox(
<<<<<<< HEAD
    executable_path=r"c:\Users\nigga\code\python\100-days-of-code\geckodrivers\geckodriver.0.29.1.exe")
=======
    executable_path=r"c:\Users\{USERNAME}\code\python\100-days-of-code\geckodrivers\geckodriver.0.29.1.exe")
>>>>>>> 4d6ca05982cde937099bc6474b5ded44ef05898e

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# write script
script = "alert('Alert via selenium')"

# generate a alert via javascript
driver.execute_script(script)
