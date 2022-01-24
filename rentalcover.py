import datetime
import unittest
import ast
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import allure

import QuoteResult
import QuoteSearch

class InstantQuote(unittest.TestCase):

    def setUp(self):
        options = Options()
        #options.headless = True
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.rentalcover.com/en/")

        file = open("test_data.txt", "r")
        contents = file.read()
        self.test_data = ast.literal_eval(contents)
        file.close()

    allure.step
    def enter_country_fromdate_and_todate(self):
        self.getinstquotesrchpage = QuoteSearch.GetInstantQuote(self.driver)
        self.plcyinfpymntpage = QuoteResult.PolicyInformationAndPayment(self.driver)

        self.getinstquotesrchpage.enter_country_and_select_from_suggestions(self.test_data['country'])
        self.getinstquotesrchpage.click_on_from_date_picker()
        self.getinstquotesrchpage.selectdate(self.test_data['fromDate'])

        # Allowing a slight delay (if any) for the calendar to refresh
        self.driver.implicitly_wait(1)
        self.getinstquotesrchpage.selectdate(self.test_data['toDate'])

    allure.step
    def select_vehicle_type(self):
        CAR = 'Car'
        FOURBYFOUR = '4x4'
        isCarPresent = False
        isFourByFourPresent = False
        if len(self.getinstquotesrchpage.is_fourbyfour_vehicle_preselected()) == 0:
            self.getinstquotesrchpage.change_vehicle_type_button()
            print('Length is: '+ str(len(self.getinstquotesrchpage.get_vehicle_type_select_list().options)))
            # Post clicking on the Change icon the select drop down at times is taking a slight delay to refresh and retrieve the text values of the list. 
            # This wait is to check if the first select value is loaded properly which will most certainly guarantee that the entire list is loaded properly.
            WebDriverWait(self.driver, 10).until(lambda wd: len(self.getinstquotesrchpage.get_vehicle_type_select_list().options[0].accessible_name)>0)
            for index in range(0, len(self.getinstquotesrchpage.get_vehicle_type_select_list().options)):
                if self.getinstquotesrchpage.get_vehicle_type_select_list().options[index].accessible_name == FOURBYFOUR:
                    isFourByFourPresent = True
                    self.getinstquotesrchpage.select_vehicle_type_by_value(FOURBYFOUR)
                    print(FOURBYFOUR+' is selected')
                elif self.getinstquotesrchpage.get_vehicle_type_select_list().options[index].accessible_name == CAR:
                    isCarPresent = True
        if isFourByFourPresent==False and isCarPresent == True:
            self.getinstquotesrchpage.select_vehicle_type_by_value(CAR)
            print(CAR+' is selected')
    
    def test_country_vehicletype_date_based_quote(self):
        self.getinstquotesrchpage = QuoteSearch.GetInstantQuote(self.driver)
        self.plcyinfpymntpage = QuoteResult.PolicyInformationAndPayment(self.driver)
        self.enter_country_fromdate_and_todate()
        self.select_vehicle_type()
        searchpagescreenshot = str(datetime.datetime.now()).replace(' ','_').replace('/','')+'.png'    
        self.driver.save_screenshot(searchpagescreenshot)
        allure.attach.file('./'+searchpagescreenshot,'Search Page Screenshot',attachment_type=allure.attachment_type.PNG)    
        self.getinstquotesrchpage.click_on_get_quote_button()
        assert self.plcyinfpymntpage.check_if_policy_information_and_payment_page_is_loaded() is True
        print("Quote ID: " + self.plcyinfpymntpage.get_quote_id())
        policyquotepagescreenshot = str(datetime.datetime.now()).replace(' ','_').replace('/','')+'.png'
        self.driver.save_screenshot(policyquotepagescreenshot)
        allure.attach.file('./'+policyquotepagescreenshot,'Policy Page Screenshot',attachment_type=allure.attachment_type.PNG)    



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()