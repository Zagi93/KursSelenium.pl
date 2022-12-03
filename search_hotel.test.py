from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.kurs-selenium.pl/demo/")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys("Dubai")
driver.find_element_by_xpath("//span[text()='Dubai']").click()

driver.find_element_by_name("checkin").send_keys("25/09/2022")
driver.find_element_by_name("checkout").send_keys("29/09/2022")
# driver.find_element_by_name("travellers").clear()
# driver.find_element_by_name("travellers").send_keys("3 Adult 1 Child")

driver.find_element_by_id("travellersInput").click()
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys("3")
driver.find_element_by_id("childInput").clear()
driver.find_element_by_id("childInput").send_keys("2")
driver.find_element_by_xpath("//button[@type='submit']").click()


# driver.find_element_by_name("checkin").click()
# driver.find_element_by_xpath("//td[@class='day ' and text()='26']").click()
# elementy = driver.find_elements_by_xpath("//td[@class='day ' and text()='28']")
# for element in elementy:
#     if element.is_displayed():
#         element.click()
#         break


# //h4[contains(@class,'list_title')]//b
hotels = driver.find_elements_by_xpath("//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)


prices = driver.find_elements_by_xpath("//div[contains(@class,'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Do zapłaty " + price)


assert hotel_names[0] == "Jumeirah Beach Hotel"
assert hotel_names[1] == "Oasis Beach Tower"
assert hotel_names[2] == "Rose Rayhaan Rotana"
assert hotel_names[3] == "Hyatt Regency Perth"


assert price_values[0] == "$22"
assert price_values[1] == "$50"
assert price_values[2] == "$80"
assert price_values[3] == "$150"

driver.quit()


