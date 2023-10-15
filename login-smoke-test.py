from selenium import webdriver

#opening Chrome browser and opening the Brain Bucket URL
driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

#making the window on full size screen
driver.maximize_window()


#Enter Email
username_input = driver.find_element_by_id("input-email")
username_input.clear()
username_input.send_keys("Anastasia@test.com")

#Enter Password
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("Qwerty123")

#Clicking the Login button
login_btn = driver.find_element_by_xpath("//input[@value='Login']")
login_btn.click()