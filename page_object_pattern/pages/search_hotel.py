import allure
from allure_commons.types import AttachmentType


class serachHotelPage:



    def __init__(self,driver):
        self.driver = driver
        self.serach_hotel_span_xpatch = "//span[text()='Search by Hotel or City Name']"
        self.serach_hotel_input_xpatch ="//div[@id='select2-drop']//input"
        self.location_match_xpatch = "//span[text()='Dubai']"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.children_input_id = "childInput"
        self.serach_button_xpatch = "//button[@type='submit']"


    @allure.step("Setting city name to '(1)'")
    def set_city(self,city):
        self.driver.find_element_by_xpath(self.serach_hotel_span_xpatch).click()
        self.driver.find_element_by_xpath(self.serach_hotel_input_xpatch).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_xpatch).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set city", attachment_type=AttachmentType.PNG)

    @allure.step("Setting date range from '(1)' to '(2)'")
    def set_day_range(self,chec_in, check_out):
       self.driver.find_element_by_name(self.check_in_input_name).send_keys(chec_in)
       self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_out)
       allure.attach(self.driver.get_screenshot_as_png(), name="set date range", attachment_type=AttachmentType.PNG)

    @allure.step("Setting travellers - adults '(1)' and kids  '(2)'")
    def set_travellers(self, adults, child):
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send.keys(adults)
        self.driver.find_element_by_id(self.children_input_id).clear()
        self.driver.find_element_by_id(self.children_input_id).send.keys(child)
        allure.attach(self.driver.get_screenshot_as_png(), name="set travellers", attachment_type=AttachmentType.PNG)


    def perform_serach(self):
        self.driver.find_element_by_xpath(self.serach_button_xpatch).click()








