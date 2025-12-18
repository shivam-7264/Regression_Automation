import json
import os
import pdb
import sys
import time
from datetime import datetime
from time import sleep

import pyautogui
from numpy.core.defchararray import lower
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.chrome.options import Options as chrmOption
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as edgeOption
from selenium.webdriver.firefox.options import Options as ffOption
from selenium.webdriver.ie.options import Options as ieOption
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from lib.action import EventsPage


class Key_Word_World(EventsPage):
    TAN = ""

    def open_browser(self, path, val):
        """To Launch the browser"""
        if val == "firefox" or val == "fire fox":
            try:
                options = ffOption()
                # options.add_argument("--headless")
                dr = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
            except:
                os.environ["HTTP_PROXY"] = "http://172.24.175.125:9090/"
                os.environ["HTTPS_PROXY"] = "http://172.24.175.125:9090/"
                dr = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        elif val == "ie":
            ie_options = ieOption()
            ie_options.ignore_protected_mode_settings = True
            dr = webdriver.Ie(options=ie_options, executable_path=path)
        elif val == "edge":
            options = edgeOption()
            # options.add_argument("headless")
            dr = webdriver.Edge(options=options, executable_path=path)
        else:
            # chromedriver_autoinstaller.install()
            # Check if the current version of chromedriver exists
            # and if it doesn't exist, download it automatically,
            # then add chromedriver to path
            options = chrmOption()
            prefs = {"credentials_enable_service": False,
                     "profile.password_manager_enabled": False}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
            options.add_argument("--start-maximized")
            options.add_argument("--log-level=3")
            # options.add_argument("--headless")  # Runs Chrome in headless mode.
            try:
                dr = webdriver.Chrome(options=options, executable_path=path)
            except:
                try:
                    dr = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
                except:
                    os.environ["HTTP_PROXY"] = "http://172.24.175.125:9090/"
                    os.environ["HTTPS_PROXY"] = "http://172.24.175.125:9090/"
                    dr = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

        dr.set_window_position(-8, -3)
        dr.set_window_size(1400, 735)
        self.driver = dr

    def kill_browser(self):
        """To close the browser"""
        self.driver.quit()

    # noinspection PyMethodMayBeStatic
    def wait_to_load(self, val):
        """To wait for loading"""
        time.sleep(val)

    def load_url(self, url):
        """To load the given url"""
        self.driver.get(url)

    def save_snap_shot(self, path):
        """To save the screenshot in the said path"""
        self.driver.save_screenshot(path)

    def enter_text(self, by, ele, value):
        """To enter the given value in the said element"""
        self.send_keys_with_clear(by, ele, value)

    def move_to_the_element(self, by, ele):
        """To hover on element"""
        key = self.return_element_locator(by, ele)
        self.driver.execute_script("arguments[0].scrollIntoView();", key)

    def click_on_element(self, by, ele):
        """To click on the said element"""
        self.check_element_present(by, ele)
        self.click_the_element(by, ele)

    def verify_value_true(self, by, ele, val):
        """To verify whether given data is present in the element"""
        result = self.get_element_text(by, ele)
        assert lower(str(val)) in lower(
            result.strip()), "Value/ Data mismatch - required is " + val + " data/ value available is " + result

    def verify_value_false(self, by, ele, val):
        """To verify whether given data is not present in the element"""
        result = self.get_element_text(by, ele)
        assert val != result.strip(), "Value/ Data matches - required is " + val + " data/ value available is " + result

    def check_element_present(self, by, element):
        """
         To return if the element is present in DOM
        """
        result = self.verify_element_is_available(by, element)
        assert result == True, "Element is not present in DOM"

    def check_element_not_present(self, by, element):
        """
         To return if the element is not present in DOM
        """
        result = self.verify_element_is_not_available(by, element)
        assert result is False, "Element is present in DOM"

    def wait_till_loading_ends(self):
        """
        Wait till the spin icon disappears from the screen
        """
        sleep(2)
        by = "css"
        element1 = "div.ant-spin"
        try:
            elemt1 = self.verify_elements_not_in_dom(by, element1)
            if len(elemt1) == 0:
                pass
                # print("No loading found")
            else:
                count = 120
                for i in range(count):
                    ele1 = self.verify_elements_not_in_dom(by, element1)
                    if len(ele1) == 0:
                        break
                    else:
                        sleep(0.5)
                # print("Loading completed")
        except (NoSuchElementException, StaleElementReferenceException):
            pass
            # print("Page is already loaded")
        sleep(1)

    # noinspection PyMethodMayBeStatic
    def pyautogui_to_upload_a_file(self, value):
        sleep(2)
        pyautogui.write(value)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('backspace')
        pyautogui.press('down')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        sleep(3)
        pyautogui.press('left')
        pyautogui.press('enter')
        sleep(3)
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')

    # noinspection PyMethodMayBeStatic
    def prepare_sample_file(self, name=None, filename=None):
        """
         To prepare the sample file to upload in AWS S3 bucket
        """
        if "C:" in filename:
            filepath = filename
        else:
            sys_path = sys.path[0]
            filepath = os.path.join(sys_path, "Sample files\\", filename)
        p = os.listdir(filepath)[0]
        path = os.path.join(filepath, p)
        # Extract the zip file
        file_number = None
        file_number_last = None
        file_name = None
        if name != "NA":
            a = list(name)
            temp = ["".join(a[0:8])]
            temp2 = ["".join(a[8:10])]
            file_number = str(temp[0])
            file_number_last = temp2[0]
            file_name = file_number + file_number_last
            print(file_name)
        elif name == "NA":
            pth = path.split("\\")
            raw_file_name = pth[-1]
            a = list(raw_file_name)
            temp = ["".join(a[0:8])]
            temp2 = ["".join(a[8:10])]
            file_number = int(temp[0]) + 1
            file_number_last = temp2[0]
            file_name = str(file_number) + file_number_last
            print(file_name)
        else:
            print("Invalid argument passed")
        dir_path = path
        # z = []
        # for file in os.listdir(dir_path):
        #     if file.endswith(".zip"):
        #         z.append(file)
        # zip = z[-1]
        #
        # zip_path = os.path.join(dir_path, zip)
        # with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        #     zip_ref.extractall(dir_path)

        # Rename the extracted pdf file
        # a = []
        # for file in os.listdir(dir_path):
        #     if file.endswith(".pdf"):
        #         a.append(file)
        # pdf = a[-1]
        # new_pdf = file_name + "_oi-patent.pdf"
        # initial = os.path.join(dir_path, pdf)
        # final = os.path.join(dir_path, new_pdf)
        # os.rename(initial, final)
        #
        # # Create the new zip file
        #
        # os.chdir(dir_path)
        # new_zip_name = file_name + ".zip"
        # zf = zipfile.ZipFile(new_zip_name, "w")
        # zf.write(new_pdf, compress_type=zipfile.ZIP_DEFLATED)
        # zf.close()
        #
        # # Remove pdf and old zip files
        # os.remove(os.path.join(dir_path, new_pdf))
        # os.remove(os.path.join(dir_path, zip))

        # Update metadata file
        jsn = []
        for file in os.listdir(dir_path):
            if file.endswith(".json"):
                jsn.append(file)
        jsn_file_name = jsn[-1]
        metadata_file_path = os.path.join(dir_path, jsn_file_name)
        af = open(metadata_file_path, "r")
        js = json.load(af)
        af.close()
        js["tan"] = file_name
        af = open(metadata_file_path, "w")
        json.dump(js, af)
        af.close()
        print("File edited")

        # Rename the parent folder
        os.chdir(dir_path)
        os.chdir('..')
        initial_folder_name = dir_path
        temp = dir_path.split("\\")
        temp[-1] = file_name
        final_folder_name = "\\".join(temp)
        os.rename(initial_folder_name, final_folder_name)

    # noinspection PyMethodMayBeStatic
    def update_metadata_file(self, key, value, path):
        """
         To update the metadata file
        """

        af = open(path, "r")
        js = json.load(af)
        af.close()
        js[key] = value
        af = open(path, "w")
        json.dump(js, af)
        af.close()
        print("File edited")

    def click_three_dots(self, value):
        file_three_dots_xpath = "//*[contains(text(),'" + value + "')]/../../../..//*[contains(@class,'ant-dropdown-link')]"
        page_no_css = "div.header-myproject li[class*=pagination]>a"
        page_button = "(//nz-select[contains(@class,'ant-pagination')])[1]"
        pagination = self.verify_elements_not_in_dom("xpath", page_button)
        try:
            sleep(1)
            self.click_on_element("xpath", file_three_dots_xpath)
        except TimeoutException:
            if len(pagination) != 0:
                self.select_pagination(100)
                pages = self.find_elements_in_dom("css", page_no_css)
                flag = False
                for i in pages[1:]:
                    ActionChains(self.driver).move_to_element(i).click().perform()
                    self.wait_till_loading_ends()
                    try:
                        self.click_on_element("xpath", file_three_dots_xpath)
                        flag = True
                        break
                    except TimeoutException:
                        pass
                if flag is True:
                    pass
                else:
                    raise Exception("Given file is not present")
            else:
                raise Exception("Given file is not present")

    def verify_file_count_in_queue(self, role, queue):
        if lower(role)=="sorter":
            queue_count_text_xpath = "//*[normalize-space(text())='"+queue+"']/../../div[2]/*"
        else:
            queue_count_text_xpath = "//*[normalize-space(text())='" + queue + "']/*"
        page_no_css = "div.header-myproject li[class*=pagination]>a"
        page_button = "(//nz-select[contains(@class,'ant-pagination')])[1]"
        files_css = "div.scroll-css>div"
        pagination = self.verify_elements_not_in_dom("xpath", page_button)
        count = 0
        if len(pagination) == 0:
            file_count = len(self.find_elements_in_dom("css", files_css))
            queue_count = self.return_element_locator("xpath", queue_count_text_xpath).text.strip()
            assert str(file_count) == queue_count, "File count does not match"
        else:
            self.select_pagination(100)
            file_count = len(self.find_elements_in_dom("css", files_css))
            count = count + file_count
            pages = self.find_elements_in_dom("css", page_no_css)
            if len(pages)>1:
                for i in pages[1:]:
                    ActionChains(self.driver).move_to_element(i).click().perform()
                    self.wait_till_loading_ends()
                    file_count = len(self.find_elements_in_dom("css", files_css))
                    count = count + file_count
            assert str(count) == queue_count_text_xpath

    def click_project_three_dots(self, value):
        project_three_dots_xpath = "//a[text()='" + value + "']/../../../..//span[text()='more_vert']"
        page_no_css = "div.header-myproject li[class*=pagination]>a"
        page_button = "(//nz-select[contains(@class,'ant-pagination')])[1]"
        pagination = self.verify_elements_not_in_dom("xpath", page_button)
        try:
            sleep(1)
            key = self.return_element_locator("xpath", project_three_dots_xpath)
            ActionChains(self.driver).move_to_element(key).click().perform()
        except TimeoutException:
            if len(pagination) != 0:
                self.select_pagination(100)
                pages = self.find_elements_in_dom("css", page_no_css)
                flag = False
                for i in pages[1:]:
                    ActionChains(self.driver).move_to_element(i).click().perform()
                    self.wait_till_loading_ends()
                    try:
                        key = self.return_element_locator("xpath", project_three_dots_xpath)
                        ActionChains(self.driver).move_to_element(key).click().perform()
                        sleep(2)
                        flag = True
                        break
                    except TimeoutException:
                        pass
                if flag is True:
                    pass
                else:
                    raise Exception("Given file is not present")
            else:
                raise Exception("Given file is not present")

    def click_file_check_box(self, filename):
        checkbox_xpath = "//*[contains(text(),'" + filename + "')]/../../..//input/.."
        page_no_css = "div.header-myproject li[class*=pagination]>a"
        page_button = "(//nz-select[contains(@class,'ant-pagination')])[1]"
        pagination = self.verify_elements_not_in_dom("xpath", page_button)
        try:
            self.click_on_element("xpath", checkbox_xpath)
            sleep(2)
        except TimeoutException:
            if len(pagination) != 0:
                self.select_pagination(100)
                pages = self.find_elements_in_dom("css", page_no_css)
                flag = False
                for i in pages[1:]:
                    ActionChains(self.driver).move_to_element(i).click().perform()
                    self.wait_till_loading_ends()
                    try:
                        self.click_on_element("xpath", checkbox_xpath)
                        sleep(2)
                        flag = True
                        break
                    except TimeoutException:
                        pass
                if flag is True:
                    pass
                else:
                    raise Exception("Given file is not present")
            else:
                raise Exception("Given file is not present")

    def click_tan_number(self, filename):
        tan_xpath = "(//*[contains(text(),'" + filename + "')])[1]"
        key = self.return_element_locator("xpath", tan_xpath)
        ActionChains(self.driver).move_to_element(key).click().perform()

    def click_on_project(self, project_name):
        project_name_xpath = "//div[@class='project-list-main']/following::a[text()='" + project_name + "']"
        key = self.return_element_locator("xpath", project_name_xpath)
        ActionChains(self.driver).move_to_element(key).click().perform()

    def get_TAN_status(self, status, tan_number):
        tan_status_xpath = "//*[contains(text(),'" + tan_number + "')]/../../../..//div[starts-with(@class,'status')]//*[contains(text(),'" + status + "')]"
        status_text = self.return_element_locator("xpath", tan_status_xpath)
        assert status_text.text.strip() == status, "Status mismatch"

    def verify_value_in_list(self, by, element, value):
        """
        To verify given value in list
        """
        el = self.verify_element_in_dom(by, element)
        lst = []
        for txt in el:
            lst.append(lower(txt.text.strip()))
        assert lower(value) in lst, "Given value is not present"

    def match_value_in_list(self, by, element, value):
        """
        To verify given piece of text in the list or not
        """
        el = self.verify_element_in_dom(by, element)
        lst = []
        flag = False
        for txt in el:
            lst.append(lower(txt.text.strip()))
        for i in lst:
            if lower(value) in i:
                flag = True
                break
        assert flag is True, "list does not have the given text"

    def select_pagination(self, num):
        page_button = "(//nz-select[contains(@class,'ant-pagination')])[1]"
        page = self.verify_elements_not_in_dom("xpath", page_button)
        if len(page) != 0:
            self.click_the_element("xpath", page_button)
            page_number_select = "//nz-option-item/div[text()='" + str(num) + " / page']"
            self.click_the_element("xpath", page_number_select)
            self.wait_till_loading_ends()
        else:
            print("Pagination is not applicable")

    def choose_value_from_element_list(self, by, element, value):
        """
        To choose given value from said drop down
        """
        el = self.find_elements_in_dom(by, element)
        try:
            for option in el:
                if lower(str(option.text.strip())) == lower(str(value)):
                    option.click()
                    sleep(1)
                    break
        except StaleElementReferenceException:
            self.choose_value_from_element_list(by, element, value)

    def check_element_enabled(self, by, element):
        """
         To return if the element is enabled or not
        """
        keys = self.return_element_locator(by, element)
        result = keys.is_enabled()
        assert result == True, "Element is not enabled"

    def check_element_disabled(self, by, element):
        """
         To return if the element is enabled or not
        """
        keys = self.return_element_locator(by, element)
        result = keys.is_enabled()
        assert result == False, "Element is enabled"

    def click_by_coordinates(self, x_cor, y_cor):
        """
        Click on screen with respective to x and y coordinates
        """
        pyautogui.leftClick(x=x_cor, y=y_cor)

    def upload_file(self, by, element, file_name):
        """
        This method is used to upload the attachment images
        """
        if "C:" in file_name:
            file_path = file_name
        else:
            sys_path = sys.path[0]
            file_path = os.path.join(sys_path, str(file_name))
        self.driver.execute_script("""var elements = document.getElementsByTagName('input');
                                    for (var i=0;i < elements.length;i += 1){
                                    elements[i].style.display = 'block';
                                    }""")
        key = self.return_element_locator(by, element)
        key.send_keys(file_path)

    def verify_audit_due_date(self):
        """
        This method is used to verify whether the difference of Audit Due Date (ADD) and Sampled Date (SD)
        in Audit form
        """
        ADD_css = "div.date-wise-section>div:nth-child(3)>div:nth-child(2)"
        SD_css = "div.date-wise-section>div:nth-child(2)>div:nth-child(2)"
        ADD_text = (self.return_element_locator("css", ADD_css)).text.strip()
        SD_text = (self.return_element_locator("css", SD_css)).text.strip()
        audit_date = datetime.strptime(ADD_text, "%m/%d/%Y")
        sampled_date = datetime.strptime(SD_text, "%m/%d/%Y")
        assert (audit_date - sampled_date).days == 14, "Audit due Date and Sampled Date are not matching"

    def verify_generification_flag(self):
        """
        This method is used to verification of Generification flag in Audit form
        """
        # locator for all generification status in all structure diagram
        generification_status_css = "div.generification>div.justify-space-btn>div+div"

        # locator for Gen flag in top of audit form
        gen_flag_xpath = "//div[@class='font-bold' and normalize-space()='Gen']/following-sibling::div"
        gen_status_list = []
        gen_status = self.find_elements_in_dom("css", generification_status_css)
        gen_flag = self.return_element_locator("xpath", gen_flag_xpath).text.strip()
        for i in gen_status:
            gen_status_list.append(i.text.strip())
        if "Yes" in gen_status_list and gen_flag == "G":
            pass
        elif "Yes" in gen_status_list and gen_flag == "-":
            raise Exception("Generification is Yes but Gen flag is not G")
        elif "Yes" not in gen_status_list and gen_flag == "G":
            raise Exception("Generification is Not Yes but Gen flag is G")

    def select_specialty_as(self, value):
        """
        This method is used to select the specialty in annotation screen
        """
        specialty_filed_css = "div.specialtyHeading+div>nz-select"
        specialty_dropdown_css = "nz-option-item>div"
        drop_down_close_button_xpath = "//button/span[normalize-space()='Close']"
        self.click_on_element("css", specialty_filed_css)
        drop_d = self.find_elements_in_dom("css", specialty_dropdown_css)
        for i in drop_d:
            if i.text.strip() == str(value):
                i.click()
                break
        self.click_the_element("xpath", drop_down_close_button_xpath)

    def delete_specialty(self, value=None):
        """
        This method is used to delete the specialty in annotation screen
        """
        present_specialty = "//div[normalize-space()='" + value + "']/i"
        delete_button_css = "div.example-list i>svg"
        if value != "NA":
            try:
                self.click_the_element("xpath", present_specialty)
            except Exception:
                raise Exception("Given specialty is not available to delete")
        else:
            try:
                dl_btns = self.find_elements_in_dom("css", delete_button_css)
                for i in dl_btns:
                    i.click()
                    sleep(1)
            except (StaleElementReferenceException, NoSuchElementException):
                print("No specialty was present")

    def verify_download_report_button(self):
        download_btn_css = "a.export-dropdown>img[src*=download]"
        no_data_css = "nz-table#graphTable table>tbody>tr>td:nth-child(1) p"
        empty_table_css = "nz-table#graphTable table>tbody>tr>td:nth-child(1)"

        no_data_list = self.verify_elements_not_in_dom("css", no_data_css)
        empty_table_list = self.verify_elements_not_in_dom("css", empty_table_css)
        if len(no_data_list) > 1:
            buffer = []
            for i in no_data_list:
                buffer.append(i.text.strip())
            if "No Data" in buffer:
                if len(self.verify_elements_not_in_dom("css", download_btn_css)) == 0:
                    print("Data is not present in report")
            else:
                raise Exception("Data is not on screen, still Download button is present")
        elif len(empty_table_list) > 1:
            buffer = []
            for i in empty_table_list:
                buffer.append(i.text.strip())
            if 0 in buffer:
                if len(self.verify_elements_not_in_dom("css", download_btn_css)) == 0:
                    print("Data is not present in report")
            else:
                self.check_element_present("css", download_btn_css)

    def verify_report_download_options(self, value):
        download_btn_css = "a.export-dropdown>img[src*=download]"
        no_data_css = "nz-table#graphTable table>tbody>tr>td:nth-child(1) p"
        empty_table_css = "nz-table#graphTable table>tbody>tr>td:nth-child(1)"
        report_dropdown_options_css = "ul.ant-dropdown-menu>li"

        no_data_list = self.verify_elements_not_in_dom("css", no_data_css)
        empty_table_list = self.verify_elements_not_in_dom("css", empty_table_css)
        if len(no_data_list) > 0:
            buffer = []
            for i in no_data_list:
                buffer.append(i.text.strip())
            if "No Data" in buffer:
                if len(self.verify_elements_not_in_dom("css", download_btn_css)) == 0:
                    print("Data is not present in report")
            else:
                raise Exception("Data is not on screen, still Download button is present")
        elif len(empty_table_list) > 0:
            buffer = []
            for i in empty_table_list:
                buffer.append(i.text.strip())
            if 0 in buffer:
                if len(self.verify_elements_not_in_dom("css", download_btn_css)) == 0:
                    print("Data is not present in report")
            else:
                self.click_the_element("css", download_btn_css)
                self.verify_value_in_list("css", report_dropdown_options_css, value)

    def click_download_report_button(self):
        download_btn_css = "a.export-dropdown>img[src*=download]"
        no_data_css = "nz-table#graphTable table>tbody>tr>td:nth-child(1) p"
        empty_table_css = "nz-table#graphTable table>tbody>tr>td:nth-child(1)"

        no_data_list = self.verify_elements_not_in_dom("css", no_data_css)
        empty_table_list = self.verify_elements_not_in_dom("css", empty_table_css)
        if len(no_data_list) > 0:
            buffer = []
            for i in no_data_list:
                buffer.append(i.text.strip())
            if "No Data" in buffer:
                if len(self.verify_elements_not_in_dom("css", download_btn_css)) == 0:
                    print("Data is not present in report")
            else:
                raise Exception("Data is not on screen, still Download button is present")
        elif len(empty_table_list) > 0:
            buffer = []
            for i in empty_table_list:
                buffer.append(i.text.strip())
            if 0 in buffer:
                if len(self.verify_elements_not_in_dom("css", download_btn_css)) == 0:
                    print("Data is not present in report")
            else:
                self.click_the_element("css", download_btn_css)

    def download_reports_as(self, value):
        download_btn_css = "a.export-dropdown>img[src*=download]"
        no_data_css = "nz-table#graphTable table>tbody>tr>td:nth-child(1) p"
        empty_table_css = "nz-table#graphTable table>tbody>tr>td:nth-child(1)"
        report_dropdown_options_css = "ul.ant-dropdown-menu>li"

        no_data_list = self.verify_elements_not_in_dom("css", no_data_css)
        empty_table_list = self.verify_elements_not_in_dom("css", empty_table_css)
        if len(no_data_list) > 0:
            buffer = []
            for i in no_data_list:
                buffer.append(i.text.strip())
            if "No Data" in buffer:
                if len(self.verify_elements_not_in_dom("css", download_btn_css)) == 0:
                    print("Data is not present in report")
            else:
                raise Exception("Data is not on screen, still Download button is present")
        elif len(empty_table_list) > 0:
            buffer = []
            for i in empty_table_list:
                buffer.append(i.text.strip())
            if 0 in buffer:
                if len(self.verify_elements_not_in_dom("css", download_btn_css)) == 0:
                    print("Data is not present in report")
            else:
                self.click_the_element("css", download_btn_css)
                self.verify_value_in_list("css", report_dropdown_options_css, value)
                self.choose_value_from_element_list("css", report_dropdown_options_css, value)
                self.wait_till_loading_ends()

    def select_user_role(self, username):
        role_dropdown_css = "nz-select[nzplaceholder='User Role'] nz-select-item"
        userName_css = "nz-option-container nz-option-item>div"
        self.wait_till_loading_ends()
        self.click_on_element("css", role_dropdown_css)
        self.choose_value_from_element_list("css", userName_css, username)
        sleep(1)
        self.wait_till_loading_ends()
