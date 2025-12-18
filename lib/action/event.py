import pdb
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from lib.action import BasePage


class EventsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def send_keys(self, by, element, value):
        """
        Click on element locator and send the keys
        """
        keys = self.return_element_locator(by, element)
        keys.send_keys(value)

    def click_the_element(self, by, element):
        """
        Click on element locator
        """
        try:
            key = self.return_visible_element_locator(by, element)
            self.move_to_find(by, element)
            self.move_to_find_click(by, element)
        except Exception:
            self.javascript_click(by, element)

    def double_click_on_element(self, by, ele):
        """
        To double-click on the said element
        """

        key = self.return_element_locator(by, ele)
        ActionChains(self.driver).double_click(key).perform()

    def define_sleep(self, time):
        """
        To make wait as user request
        """
        sleep(time)

    def clear_the_element(self, by, element):
        """
        Clear the element locator
        """
        keys = self.return_element_locator(by, element)
        ActionChains(self.driver).click(keys).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
            Keys.BACKSPACE).perform()

    def zoom_out(self):
        """ To zoom out the browser window"""
        sleep(3)
        self.driver.execute_script("document.body.style.zoom='70%'")
        sleep(2)
        # self.driver.execute_script("document.body.style.zoom='80%'")
        # sleep(2)

    def element_is_displayed(self, by, element):
        """
        Verify the element is displayed or not
        """
        element = self.return_element_locator(by, element)
        result = element.is_displayed()
        return result

    def get_element_text(self, by, element):
        """
        Verify the element is send the text
        """
        keys = self.return_element_locator(by, element)
        result = keys.text.strip()
        return result

    def send_keys_with_clear(self, by, element, value):
        """
        It will send the keys with clear the element
        """
        keys = self.return_element_locator(by, element)
        keys.click()
        self.clear_the_element(by, element)
        keys.send_keys(value)

    def javascript_click(self, by, element):
        keys = self.return_element_locator(by, element)
        self.driver.execute_script("arguments[0].click()", keys)

    def click_and_drag(self, by, element):
        # pdb.set_trace()
        keys = self.return_element_locator(by, element)
        actions = ActionChains(self.driver)
        source = self.driver.find_element(By.XPATH, "//body[@class='mat-typography']")
        actions.move_by_offset(5, 5).click().drag_and_drop_by_offset(source, 200, 10).release().perform()

    def click_and_send_keys(self, by, element, value):
        """
        Click on element locator and send the keys
        """
        keys = self.return_element_locator(by, element)
        keys.click()
        sleep(0.5)
        keys.send_keys(value)

    def move_to_find(self, by, element):
        """
        It will scroll to find the given element in the webpage
        """
        keys = self.return_element_locator(by, element)
        actions = ActionChains(self.driver)
        actions.move_to_element(keys).perform()

    def move_to_find_click(self, by, element):
        """
        It will scroll to find the given element in the page
         and click that element
        """
        try:
            key = self.return_clickable_element_locator(by, element)
            ActionChains(self.driver).move_to_element(key).click().perform()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            sleep(5)
            self.javascript_click(by, element)

    def move_to_find_click_option(self, by, element, by2, element2):
        """
        It will scroll to find the given element in the page
         and click that element
        """
        self.move_to_find(by, element)
        self.move_to_find_click(by2, element2)

        # //li[text()='Edit']
        # def cancel_print_window(self):
        #     """
        #     To close the kot print window and kot copy
        #     """
        #     sleep(5)
        #     win_bef = self.driver.window_handles[0]
        #     win_aft = self.driver.window_handles[1]
        #     self.driver.switch_to_window(win_aft)
        #     shadow_root = self.driver.execute_script('return arguments[0].shadowRoot',
        #                                              self.driver.find_element_by_tag_name("print-preview-app"))
        #     root1 = shadow_root.find_element_by_css_selector('print-preview-sidebar')
        shadow_root1 = self.driver.execute_script('return arguments[0].shadowRoot', root1)

    #     try:
    #         root2 = shadow_root1.find_element_by_css_selector('print-preview-button-strip')
    #     except:
    #         root2 = shadow_root1.find_element_by_css_selector('print-preview-header')
    #     shadow_root2 = self.driver.execute_script('return arguments[0].shadowRoot', root2)
    #     cancel_button = shadow_root2.find_element_by_css_selector(".cancel-button")
    #     cancel_button.click()
    #     sleep(3)
    #     self.driver.switch_to_window(win_bef)

    def press_tab_key(self):
        """
        To press Tab button in keyboard keys
        """
        try:
            ActionChains(self.driver).send_keys(Keys.TAB).perform()
        except:
            self.driver.find_element_by_css_selector("html body").send_keys(Keys.TAB)

    def press_escape_key(self):
        """
        To press Escape button in keyboard keys
        """
        sleep(2)
        try:
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except:
            self.driver.find_element_by_css_selector("html body").send_keys(Keys.ESCAPE)
        sleep(2)

    def press_enter_key(self):
        """
        To press Enter button keyboard keys
        """
        sleep(1)
        try:
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        except:
            self.driver.find_element_by_css_selector("html body").send_keys(Keys.ENTER)
        sleep(1)

    def press_home_key(self):
        """
        To press Home button in keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector("html body").send_keys(Keys.HOME)
        sleep(2)

    def press_end_key(self):
        """
        To press END button keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector("html body").send_keys(Keys.END)
        sleep(2)

    # def zoom_out(self):
    #     """ To accept the alert """
    #     pyautogui.hotkey('ctrl', 'subtract')
    #     pyautogui.hotkey('ctrl', 'subtract')

    def accept_alert(self):
        """ To accept the alert """
        sleep(2)
        a = self.driver.switch_to.alert
        a.accept()

    def press_page_down_key(self):
        """
        To press Page Down button in keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector("html body").send_keys(Keys.PAGE_DOWN)
        sleep(2)

    def press_arrow_down_key(self):
        """
        To press down button in keyboard keys
        """
        try:
            ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
        except:
            self.driver.find_element_by_css_selector("html body").send_keys(Keys.ARROW_DOWN)

    def press_arrow_up_key(self):
        """
        To press down button in keyboard keys
        """
        try:
            ActionChains(self.driver).send_keys(Keys.ARROW_UP).perform()
        except:
            self.driver.find_element_by_css_selector("html body").send_keys(Keys.ARROW_UP)

    def press_arrow_right_key(self):
        """
        To press down button in keyboard keys
        """
        try:
            ActionChains(self.driver).send_keys(Keys.ARROW_RIGHT).perform()
        except:
            self.driver.find_element_by_css_selector("html body").send_keys(Keys.ARROW_RIGHT)

    def press_ctrl_shift_home_key(self):
        """
        To press CTRL + Shift + Home button keyboard keys
        """
        sleep(2)
        self.driver.find_element_by_css_selector(
            "html body").send_keys(Keys.CONTROL, Keys.SHIFT, Keys.HOME)
        sleep(2)

    def verify_element_is_available(self, by, element):
        """
        To check element available in DOM
        """
        elemnt = self.find_elements_in_dom(by, element)
        if len(elemnt) != 0:
            return True
        else:
            return False

    def verify_element_is_not_available(self, by, element):
        """
        To check element available in DOM
        """
        elemnt = self.find_elements_not_in_dom(by, element)
        if len(elemnt) != 0:
            return True
        else:
            return False
