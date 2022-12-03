from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.kurs-selenium.pl/demo/")
bottom = driver.find_element_by_id("li_myaccount")
webdriver.ActionChains(driver).move_to_element(bottom).preform()




