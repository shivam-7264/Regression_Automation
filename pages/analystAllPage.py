from time import sleep

from lib.action import EventsPage


class AnalystAllQueue(EventsPage):
    def __init__(self, driver):
        super().__init__(driver)

    Assign_to_me_button_css = "nz-option-item[title='Assign to me']"
    Action_dropDown_css = "div[class*=action-dropDown-text] nz-select"
    files_list_xpath = "//div[@class='project-list-main']/div[2]/div"
    All_tab_xpath = "//div[@class='counts-analyst']//div[contains(text(),'All')]"

    def assign_file_to_inbox(self):
        no_of_files = self.verify_element_in_dom("xpath", self.files_list_xpath)
        for i in range(len(no_of_files)):
            self.click_the_element("css", self.Action_dropDown_css)
            self.click_the_element("css", self.Assign_to_me_button_css)
            sleep(2)
            self.click_the_element("xpath", self.All_tab_xpath)
            sleep(1)
