import pdb
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v106.indexed_db import Key
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
pdb.set_trace()
driver.find_element(By.NAME,("q")).send_keys("Shivam")
sleep(2)
driver.find_element(By.XPATH,"(//input[@value='Google Search'])[1]").click()
print("hjdd")
ele = driver.find_elements(By.TAG_NAME, "a")
ActionChains(driver).key_down(Keys.CONTROL).click(ele[1]).perform()
sleep(5)