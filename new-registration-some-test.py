from selenium import webdriver
from selenium.webdriver.support.color import Color

#opening Chrome browser and opening the Brain Bucket URL
driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

#making the window on full size screen
driver.maximize_window()

#verifying the logo is present. If it can't return the web element, it will return an error. Otherwise we won't see anything visually.
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

#Clicking the Continue button
new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")

#getting the background color of the button and clicking it
backround_color = new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'

new_registrant_btn.click()


#Register Account
#EnteringPersonal Details

#FirstName
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class
#entering first name Anastasia in the first name field
firstname_input = driver.find_element_by_id("input-firstname")
#clearing the input field before entering our value
firstname_input.clear()
firstname_input.send_keys("Anastasia")

#LastName
lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class
#entering last name Tskhay in the last name field
lastname_input = driver.find_element_by_id("input-lastname")
#clearing the input field before entering our value
lastname_input.clear()
lastname_input.send_keys("Tskhay")

#Email
email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
#entering email test@test.com in the last name field
email_input = driver.find_element_by_id("input-email")
#clearing the input field before entering our value
email_input.clear()
email_input.send_keys("test@test.com")

#Telephone
telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
#entering telephone 111-222-3333 in the telephone field
telephone_input = driver.find_element_by_id("input-telephone")
#clearing the input field before entering our value
telephone_input.clear()
telephone_input.send_keys("111-222-3333")

#Fax
fax_field = driver.find_element_by_xpath("//fieldset/div[6]")
fax_field_class = fax_field.get_attribute("class")
assert "required" not in fax_field_class
#entering fax 222-333-4444 in the fax field
fax_input = driver.find_element_by_id("input-fax")
#clearing the input field before entering our value
fax_input.clear()
fax_input.send_keys("222-333-4444")

#Company
company_field = driver.find_element_by_xpath("//fieldset[2]/div[1]")
company_field_class = company_field.get_attribute("class")
assert "required" not in company_field_class
company_input = driver.find_element_by_id("input-company")
company_input.clear()
company_input.send_keys("Test Company")

#Address 1
address1_field = driver.find_element_by_xpath("//fieldset[2]/div[2]")
address1_field_class = address1_field.get_attribute("class")
assert "required" in address1_field_class
address1_input = driver.find_element_by_id("input-address-1")
address1_input.clear()
address1_input.send_keys("575 W Madison St")

#Address 2
address2_field = driver.find_element_by_xpath("//fieldset[2]/div[3]")
address2_field_class = address2_field.get_attribute("class")
assert "required" not in address2_field_class
address2_input = driver.find_element_by_id("input-address-2")
address2_input.clear()
address2_input.send_keys("Apt 4304")

#City
city_field = driver.find_element_by_xpath("//fieldset[2]/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class
city_input = driver.find_element_by_id("input-city")
city_input.clear()
city_input.send_keys("Chicago")

#Post Code
postcode_field = driver.find_element_by_xpath("//fieldset[2]/div[5]")
postcode_field_class = postcode_field.get_attribute("class")
assert "required" not in postcode_field_class
postcode_input = driver.find_element_by_id("input-postcode")
postcode_input.clear()
postcode_input.send_keys("60661")

#Country
country_field = driver.find_element_by_xpath("//fieldset[2]/div[6]")
country_field_class = country_field.get_attribute("class")
assert "required" in country_field_class
country_select = driver.find_element_by_id("input-country")
country_select.click()
country_select.send_keys('Kazakhstan')

#Region/State
zone_field = driver.find_element_by_xpath("//fieldset[2]/div[7]")
zone_field_class = zone_field.get_attribute("class")
assert "required" in zone_field_class
zone_select = driver.find_element_by_id("input-zone")
zone_select.click()
zone_select.send_keys('Almaty')

#Password
password_field = driver.find_element_by_xpath("//fieldset[3]/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("Qwerty123")

#Confirm Password
confirm_field = driver.find_element_by_xpath("//fieldset[3]/div[2]")
confirm_field_class = confirm_field.get_attribute("class")
assert "required" in confirm_field_class
confirm_input = driver.find_element_by_id("input-confirm")
confirm_input.clear()
confirm_input.send_keys("Qwerty123")



#to close the browser
#driver.quit()
#to close just the tab use driver.close()