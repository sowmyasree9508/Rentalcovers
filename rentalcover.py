import unittest
import ast
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

import QuoteResult
import QuoteSearch

class InstantQuote(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.rentalcover.com/en/")

        file = open("test_data.txt", "r")
        contents = file.read()
        self.test_data = ast.literal_eval(contents)
        file.close()        
    
    def test_country_vehicletype_date_based_quote(self):
        CAR = 'Car'
        FOURBYFOUR = '4x4'
        getinstquotesrchpage = QuoteSearch.GetInstantQuote(self.driver)
        plcyinfpymntpage = QuoteResult.PolicyInformationAndPayment(self.driver)

        getinstquotesrchpage.enter_country_and_select_from_suggestions(self.test_data['country'])
        getinstquotesrchpage.click_on_from_date_picker()
        getinstquotesrchpage.selectdate(self.test_data['fromDate'])

        # Allowing a slight delay (if any) for the calendar to refresh
        self.driver.implicitly_wait(1)
        getinstquotesrchpage.selectdate(self.test_data['toDate'])
        isCarPresent = False
        isFourByFourPresent = False
        if len(getinstquotesrchpage.is_fourbyfour_vehicle_preselected()) == 0:
            getinstquotesrchpage.change_vehicle_type_button()
            print('Length is: '+ str(len(getinstquotesrchpage.get_vehicle_type_select_list().options)))
            # Post clicking on the Change icon the select drop down at times is taking a slight delay to refresh and retrieve the text values of the list. 
            # This wait is to check if the first select value is loaded properly which will most certainly guarantee that the entire list is loaded properly.
            WebDriverWait(self.driver, 10).until(lambda wd: len(getinstquotesrchpage.get_vehicle_type_select_list().options[0].accessible_name)>0)
            for index in range(0, len(getinstquotesrchpage.get_vehicle_type_select_list().options)):
                if getinstquotesrchpage.get_vehicle_type_select_list().options[index].accessible_name == FOURBYFOUR:
                    isFourByFourPresent = True
                    getinstquotesrchpage.select_vehicle_type_by_value(FOURBYFOUR)
                    print(FOURBYFOUR+' is selected')
                elif getinstquotesrchpage.get_vehicle_type_select_list().options[index].accessible_name == CAR:
                    isCarPresent = True
        if isFourByFourPresent==False and isCarPresent == True:
            getinstquotesrchpage.select_vehicle_type_by_value(CAR)
            print(CAR+' is selected')
        getinstquotesrchpage.click_on_get_quote_button()
        assert plcyinfpymntpage.check_if_policy_information_and_payment_page_is_loaded() is True
        print("Quote ID: " + plcyinfpymntpage.get_quote_id())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()