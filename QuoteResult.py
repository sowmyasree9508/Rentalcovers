from locators import QuoteSearchResultPageLocators

class PolicyInformationAndPayment(object):

    def __init__(self, driver):
        self.driver = driver

    def check_if_policy_information_and_payment_page_is_loaded(self) -> bool:
        if len(self.driver.find_elements(*QuoteSearchResultPageLocators.POLICYINFORMATIONANDPAYMENT_ELEMENT)) > 0:
            return True
        else:
            return False    

    def get_quote_id(self) -> str:
        return self.driver.current_url.split('/')[5]