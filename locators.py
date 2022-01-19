from selenium.webdriver.common.by import By

class QuoteSearchPageLocators(object):
    COUNTRYFIELD_TEXTBOX = (By.CSS_SELECTOR,'[class=\'QuoteForm-destination-select form-control ui-autocomplete-input Field-input\']')
    FROMDATE_PICKER = (By.ID, 'QuoteForm_FromDate-datepicker')
    TODATE_PICKER = (By.ID, 'QuoteForm_ToDate-datepicker')
    ISFOURBYFOURVEHICLE_PRESELECTED_ELEMENT = (By.XPATH,'//div[contains(@class,\'Field form-group\')]//strong[text()=\'4x4\']')
    CHANGEVEHICLETYPE_OPTION = (By.XPATH,'//a[contains(@href,\'#QuoteForm-vehicleType-field\')]/strong[text()=\'change\']')
    VEHICLE_SELECT_LIST = (By.CSS_SELECTOR,'#QuoteForm_VehicleType')
    GETQUOTE_BUTTON = (By.CSS_SELECTOR, '[class=\'QuoteForm-submit Form-submit btn btn-warning btn-lg btn-block\']')

    CURRENTMONTH_ELEMENT = (By.XPATH,'//div[@class=\'ui-datepicker-group ui-datepicker-group-first\']//span[@class=\'ui-datepicker-month\']')
    CURRENTYEAR_ELEMENT = (By.XPATH,'//div[@class=\'ui-datepicker-group ui-datepicker-group-first\']//span[@class=\'ui-datepicker-year\']')
    NEXTCALENDARMONTH_BUTTON = (By.CSS_SELECTOR, '[title=\'Next\']')

class QuoteSearchResultPageLocators(object):
    POLICYINFORMATIONANDPAYMENT_ELEMENT = (By.XPATH, '//h2[contains(text(),\'Policy Information & Payment\')]')    