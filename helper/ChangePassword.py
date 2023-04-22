from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import undetected_chromedriver as uc
from constants import URL
import time
import os
from dotenv import load_dotenv
from helper.Login import Login
from exceptions import *


class ChangePassword(Login):
    driver: uc.Chrome
    username: str
    password: str

    def __init__(self, _driver: uc.Chrome):
        """Initialize Chrome webdriver and load the configuration environment variables"""
        super().__init__(_driver)
    

    def login_account(self):
        login_res = self.login_run(username=self.username, password=self.password) # Timeout exception
        return login_res

    def change_password(self, current_password : str, new_password : str) -> None: # Make sure are in change password page
        self.driver.get(URL.CHANGEPASS_URL)

        current_password_form = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[3]/div[2]/input')
        new_password_form = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[4]/div[2]/input')
        new_password_again_form = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[5]/div[2]/input')

        current_password_form.send_keys(current_password)
        new_password_form.send_keys(new_password)
        new_password_again_form.send_keys(new_password)

        save_changes_button = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/div[2]/div[2]/fieldset/div/div[1]/span/input')
        save_changes_button.click()
    
    def handle_error(self): pass

    def changepwd_run(self, new_password: str, changepwd_timeout: float = 5., stay: bool = False) -> bool:
        login_res = self.login_account()
        if login_res:
            print("Login successful")
        else:
            print("Login failed!! Recheck the username and password in .env file")
            raise Exception("Login failed!! Recheck the username and password in .env file")
        
        
        self.change_password(self.password, new_password)

        response = None
        try: # Success
            WebDriverWait(self.driver, changepwd_timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[1]')))
            print(">> Change password successfully!!")
            # Post-processing: return the password into original password
            self.change_password(new_password, self.password)
            print(">> Re-Changed Password successfully")
            response = True
            
        except TimeoutException: # Waiting failed -> Timeout-Internet | Change password failed
            try:
                self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/div[2]/div[2]/fieldset/div/div[1]/span/input')
                print(">> Change password failed!!")
                # TODO: Which type of error
                response = False
            except NoSuchElementException:
                print(">> Change password loading page timeout! Check your Internet connection")
                raise Exception("Change password loading page timeout! Check your Internet connection")
            
        if stay:
            time.sleep(1000)
        return response



# driver = uc.Chrome(use_subprocess=True)
# changepassword = ChangePassword(driver)
# newpassword = os.getenv('newpassword')
# changepwd_res = changepassword.changepwd_run(newpassword)
# print(changepwd_res)

# time.sleep(1000)