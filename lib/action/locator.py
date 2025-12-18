import pdb
from time import sleep

from selenium.common.exceptions import \
    ElementNotVisibleException as ENVE, \
    ElementNotSelectableException as ENSE, \
    TimeoutException as TE, NoSuchElementException as NSEE, \
    StaleElementReferenceException as SERE, \
    ElementClickInterceptedException as ECIE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def time_wait(self):
        """
        Wait the time given to click for the next element
        """
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[ENVE, NSEE,
                                                 ENSE, TE, ECIE, SERE])
        return wait

    def explicity_wait(self):
        """
        select existing address for delivery
        """
        wait = WebDriverWait(self.driver, 20, poll_frequency=5,
                             ignored_exceptions=[ENVE, NSEE,
                                                 ENSE, TE, SERE])
        return wait

    def return_element_locator(self, by, element):

        """
        Basing on the type of element locator returns it
        """
        if by in "css":
            self.time_wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            element = self.driver.find_element(By.CSS_SELECTOR, element)
        elif by in "xpath":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.XPATH, element))))
            element = self.driver.find_element(By.XPATH, element)
        elif by in "name":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.NAME, element))))
            element = self.driver.find_element(By.NAME, element)
        elif by in "id":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.ID, element)),
                                             EC.visibility_of_element_located((By.ID, element))))
            element = self.driver.find_element(By.ID, element)
        elif by in "class":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.CLASS_NAME, element)),
                                             EC.visibility_of_element_located((By.CLASS_NAME, element))))
            element = self.driver.find_element(By.CLASS_NAME, element)
        return element

    def return_clickable_element_locator(self, by, element):
        """
        Basing on the type of element locator returns it
        """
        try:
            if by in "css":
                self.time_wait().until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
                element = self.driver.find_element(By.CSS_SELECTOR, element)
            elif by in "xpath":
                self.time_wait().until(EC.element_to_be_clickable((By.XPATH, element)))
                element = self.driver.find_element(By.XPATH, element)
            elif by in "name":
                self.time_wait().until(EC.visibility_of_element_located((By.NAME, element)))
                element = self.driver.find_element(By.NAME, element)
            elif by in "id":
                self.time_wait().until(EC.visibility_of_element_located((By.ID, element)))
                element = self.driver.find_element(By.ID, element)
            elif by in "class":
                self.time_wait().until(EC.visibility_of_element_located((By.CLASS_NAME, element)))
                element = self.driver.find_element(By.CLASS_NAME, element)
            return element
        except Exception:
            if by in "css":
                self.time_wait().until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
                element = self.driver.find_element(By.CSS_SELECTOR, element)
            elif by in "xpath":
                self.time_wait().until(EC.element_to_be_clickable((By.XPATH, element)))
                element = self.driver.find_element(By.XPATH, element)
            elif by in "name":
                self.time_wait().until(EC.element_to_be_clickable((By.NAME, element)))
                element = self.driver.find_element(By.NAME, element)
            elif by in "id":
                self.time_wait().until(EC.element_to_be_clickable((By.ID, element)))
                element = self.driver.find_element(By.ID, element)
            elif by in "class":
                self.time_wait().until(EC.element_to_be_clickable((By.CLASS_NAME, element)))
                element = self.driver.find_element(By.CLASS_NAME, element)
            return element

    def find_elements_in_dom(self, by, element):
        """
        To find elements in DOM
        """
        if by in "css":
            self.time_wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            element = self.driver.find_elements(By.CSS_SELECTOR, element)
        elif by in "xpath":
            self.time_wait().until(EC.presence_of_element_located((By.XPATH, element)))
            element = self.driver.find_elements(By.XPATH, element)
        elif by in "name":
            self.time_wait().until(EC.presence_of_element_located((By.NAME, element)))
            element = self.driver.find_elements(By.NAME, element)
        elif by in "id":
            self.time_wait().until(EC.presence_of_element_located((By.ID, element)))
            element = self.driver.find_elements(By.ID, element)
        elif by in "class":
            self.time_wait().until(EC.presence_of_element_located((By.CLASS_NAME, element)))
            element = self.driver.find_elements(By.CLASS_NAME, element)
        return element

    def find_elements_not_in_dom(self, by, element):
        """
        To find elements not in DOM
        """
        if by in "css":
            self.time_wait().until(EC.invisibility_of_element_located
                                   ((By.CSS_SELECTOR, element)))
            element = self.driver.find_elements(By.CSS_SELECTOR, element)
        elif by in "xpath":
            self.time_wait().until(EC.invisibility_of_element_located
                                   ((By.XPATH, element)))
            element = self.driver.find_elements(By.XPATH, element)
        elif by in "name":
            self.time_wait().until(EC.invisibility_of_element_located
                                   ((By.NAME, element)))
            element = self.driver.find_elements(By.NAME, element)
        elif by in "id":
            self.time_wait().until(EC.invisibility_of_element_located
                                   ((By.ID, element)))
            element = self.driver.find_elements(By.ID, element)
        elif by in "class":
            self.time_wait().until(EC.invisibility_of_element_located
                                   ((By.CLASS_NAME, element)))
            element = self.driver.find_elements(By.CLASS_NAME, element)
        return element

    def verify_element_in_dom(self, by, element):
        """
        Basing on the type of element locator returns it
        """
        if by in "css":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.CSS_SELECTOR, element)),
                                             EC.visibility_of_element_located((By.CSS_SELECTOR, element))))
            element = self.driver.find_elements(By.CSS_SELECTOR, element)
        elif by in "xpath":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.XPATH, element)),
                                             EC.visibility_of_element_located((By.XPATH, element))))
            element = self.driver.find_elements(By.XPATH, element)
        elif by in "name":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.NAME, element)),
                                             EC.visibility_of_element_located((By.NAME, element))))
            element = self.driver.find_elements(By.NAME, element)
        elif by in "id":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.ID, element)),
                                             EC.visibility_of_element_located((By.ID, element))))
            element = self.driver.find_elements(By.ID, element)
        elif by in "class":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.CLASS_NAME, element)),
                                             EC.visibility_of_element_located((By.CLASS_NAME, element))))
            element = self.driver.find_elements(By.CLASS_NAME, element)
        return element

    def verify_element_not_in_dom(self, by, element):
        """
        Basing on the type of element locator returns it
        """
        if by in "css":
            element = self.driver.find_element(By.CSS_SELECTOR, element)
        elif by in "xpath":
            element = self.driver.find_element(By.XPATH, element)
        elif by in "name":
            element = self.driver.find_element(By.NAME, element)
        elif by in "id":
            element = self.driver.find_element(By.ID, element)
        elif by in "class":
            element = self.driver.find_element(By.CLASS_NAME, element)
        return element

    def verify_elements_not_in_dom(self, by, element):
        """
        Basing on the type of element locator returns it
        """
        if by in "css":
            element = self.driver.find_elements(By.CSS_SELECTOR, element)
        elif by in "xpath":
            element = self.driver.find_elements(By.XPATH, element)
        elif by in "name":
            element = self.driver.find_elements(By.NAME, element)
        elif by in "id":
            element = self.driver.find_elements(By.ID, element)
        elif by in "class":
            element = self.driver.find_elements(By.CLASS_NAME, element)
        return element

    def return_visible_element_locator(self, by, element):

        """
        Basing on the type of element locator returns it
        """
        if by in "css":
            self.time_wait().until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
            element = self.driver.find_element(By.CSS_SELECTOR, element)
        elif by in "xpath":
            self.time_wait().until(EC.all_of(EC.visibility_of_element_located((By.XPATH, element))))
            element = self.driver.find_element(By.XPATH, element)
        elif by in "name":
            self.time_wait().until(EC.all_of(EC.visibility_of_element_located((By.NAME, element))))
            element = self.driver.find_element(By.NAME, element)
        elif by in "id":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.ID, element)),
                                             EC.visibility_of_element_located((By.ID, element))))
            element = self.driver.find_element(By.ID, element)
        elif by in "class":
            self.time_wait().until(EC.all_of(EC.presence_of_element_located((By.CLASS_NAME, element)),
                                             EC.visibility_of_element_located((By.CLASS_NAME, element))))
            element = self.driver.find_element(By.CLASS_NAME, element)
        return element
