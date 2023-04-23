from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import undetected_chromedriver as uc
from helper.constants import URL
import time
from helper.Login import Login



class ChangePassword(Login):
    driver: uc.Chrome
    username: str
    password: str

    def __init__(self, _driver: uc.Chrome):
        """Initialize Chrome webdriver and load the configuration environment variables"""
        super().__init__(_driver)
    

    def login_account(self):
        """Login to account using right username and password using function in Login class"""
        login_res = self.login_run(username=self.username, password=self.password) # Timeout exception
        return login_res

    def change_password(self, current_password : str, new_password : str, new_password_again : str) -> None: # Make sure are in change password page
        """Fill these form in change password page and click save changes button"""
        self.driver.get(URL.CHANGEPASS_URL)

        current_password_form = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[3]/div[2]/input')
        new_password_form = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[4]/div[2]/input')
        new_password_again_form = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[5]/div[2]/input')

        current_password_form.send_keys(current_password)
        new_password_form.send_keys(new_password)
        new_password_again_form.send_keys(new_password_again)

        save_changes_button = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/div[2]/div[2]/fieldset/div/div[1]/span/input')
        save_changes_button.click()
    
    def handle_error(self) -> tuple[str,str,str]:
        """We need to know the specific error that caused the failure"""
        pass_ele = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[3]/div[2]/div')
        newpass_ele = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[4]/div[2]/div')
        newpassagain_ele = self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/fieldset/div[2]/div[5]/div[2]/div')

        return (pass_ele.text, newpass_ele.text, newpassagain_ele.text)

    def changepwd_run(self, current_password: str, new_password: str, new_password_again: str, changepwd_timeout: float = 5., stay: bool = False) -> bool:
        """Main function change password"""
        login_res = self.login_account()
        if login_res:
            print("Login successful")
        else:
            print("Login failed!! Recheck the username and password in .env file")
            raise Exception("Login failed!! Recheck the username and password in .env file")
        
        
        self.change_password(current_password, new_password, new_password_again)

        response = None
        try: # Success
            WebDriverWait(self.driver, changepwd_timeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/div[1]')))
            print(">> Change password successfully!!")
            # Post-processing: return the password into original password
            self.change_password(new_password, self.password, self.password)
            print(">> Post-processing: Re-Changed Password successfully")
            response = (True, ("","",""))
            
        except TimeoutException: # Waiting failed -> Timeout-Internet | Change password failed
            try:
                self.driver.find_element('xpath', '/html/body/div[2]/div[3]/div/div[2]/div/section/div/form/div[2]/div[2]/fieldset/div/div[1]/span/input')
                print(">> Change password failed!!")
                # TODO: Which type of error
                msg = self.handle_error()
                response = (False, msg)
            except NoSuchElementException:
                print(">> Change password loading page timeout! Check your Internet connection")
                raise Exception("Change password loading page timeout! Check your Internet connection")
            
        if stay:
            time.sleep(1000)
        return response
