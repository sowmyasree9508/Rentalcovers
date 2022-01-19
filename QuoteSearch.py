from locators import QuoteSearchPageLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GetInstantQuote(object):

    def __init__(self, driver):
        self.driver = driver

    def enter_country_and_select_from_suggestions(self, country):
        countryElement = self.driver.find_element(*QuoteSearchPageLocators.COUNTRYFIELD_TEXTBOX)
        countryElement.send_keys(country)
        countryElement.send_keys(Keys.ENTER)

    def click_on_from_date_picker(self):
        self.driver.find_element(*QuoteSearchPageLocators.FROMDATE_PICKER).click()

    def click_on_to_date_picker(self):
        self.driver.find_element(*QuoteSearchPageLocators.TODATE_PICKER).click()

    def is_fourbyfour_vehicle_preselected(self):
        return self.driver.find_elements(*QuoteSearchPageLocators.ISFOURBYFOURVEHICLE_PRESELECTED_ELEMENT)

    def change_vehicle_type_button(self):
        self.driver.find_element(*QuoteSearchPageLocators.CHANGEVEHICLETYPE_OPTION).click()

    def get_vehicle_select_list_element(self):
        return self.driver.find_element(*QuoteSearchPageLocators.VEHICLE_SELECT_LIST)

    def get_vehicle_type_select_list(self):
        return Select(self.get_vehicle_select_list_element())

    def select_vehicle_type_by_value(self, vehicletype):
        self.get_vehicle_type_select_list().select_by_value(vehicletype)        

    def click_on_get_quote_button(self):
        getQuoteButton = self.driver.find_element(*QuoteSearchPageLocators.GETQUOTE_BUTTON)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(getQuoteButton))
        getQuoteButton.click()

    def selectdate(self, date):
        monthIndex = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7,'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
        desireddate = date.split("-")[0]
        desiredmonth = int(monthIndex[date.split("-")[1]])
        currentmonth = self.driver.find_element(*QuoteSearchPageLocators.CURRENTMONTH_ELEMENT).text
        currentyear = self.driver.find_element(*QuoteSearchPageLocators.CURRENTYEAR_ELEMENT).text
        calendarpaginationcounter = (desiredmonth - monthIndex[currentmonth.lower()]) + (int(date.split("-")[2]) - int(currentyear)) * 12
        for i in range(0, calendarpaginationcounter):
            self.driver.find_element(*QuoteSearchPageLocators.NEXTCALENDARMONTH_BUTTON).click()
        dateelement = self.driver.find_element(By.XPATH, '//td[@data-month=\'' + str(desiredmonth-1) + '\']//a[contains(@class,\'ui-state-default\') and text()=\'' + desireddate + '\']')
        dateelement.click()                


