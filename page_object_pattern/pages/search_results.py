import allure
from allure_commons.types import AttachmentType

class SearchResultsPage:


    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpatch = "//h4[contains(@class,'list_title')]//b"
        self.hotel_prices_xpatch = "//div[contains(@class,'price_tab')]//b"

    @allure.step("Checking reasults")
    def get_hotel_names(self):
       hotels = self.driver.find_elements_by_xpath(self.hotel_names_xpatch)
       return [hotel.get_attribute("textContent") for hotel in hotels]
       allure.attach(self.driver.get_screenshot_as_png(), name="Resualts", attachment_type=AttachmentType.PNG)




    def get_hotel_prices(self):
        prices = self.driver.find_elements_by_xpath(self.hotel_prices_xpatch)
        return [price.get_attribute("textContent") for price in prices]






#
# prices = driver.find_elements_by_xpath("//div[contains(@class,'price_tab')]//b")
# price_values = [price.get_attribute("textContent") for price in prices]