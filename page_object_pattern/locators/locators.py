class SearchHotelLocators:


    serach_hotel_span_xpatch = "//span[text()='Search by Hotel or City Name']"
    serach_hotel_input_xpatch = "//div[@id='select2-drop']//input"
    location_match_xpatch = "//span[text()='Dubai']"
    check_in_input_name = "checkin"
    check_out_input_name = "checkout"
    travellers_input_id = "travellersInput"
    adult_input_id = "adultInput"
    children_input_id = "childInput"
    serach_button_xpatch = "//button[@type='submit']"

class SearchResultLocators:


    hotel_names_xpatch = "//h4[contains(@class,'list_title')]//b"
    hotel_prices_xpatch = "//div[contains(@class,'price_tab')]//b"

