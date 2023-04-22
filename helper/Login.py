from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import undetected_chromedriver as uc
from constants import URL
import time
import os
from dotenv import load_dotenv
load_dotenv()

class Login():
    driver: uc.Chrome
    username: str
    password: str

    def __init__(self, _driver: uc.Chrome):
        """Initialize Chrome webdriver and load the configuration environment variables"""
        self.driver = _driver
        self.load_env()

    def load_env(self):
        load_dotenv()
        self.username = os.getenv('username')
        self.password =  os.getenv('password')
        print("Loaded environment variable")

    def fill_login_form(self, username: str, password: str):
        """Enter the username and password into the form"""
        username_form = self.driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/section/div/div/div/div/form/div[1]/input')
        password_form = self.driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/section/div/div/div/div/form/div[2]/input')
        
        username_form.send_keys(username)
        password_form.send_keys(password)


    def login_processing(self, captcha_timeout: float = 20.) -> bool:
        """Login processing - clicking and waiting for the response from the server

        :Args:
            - captcha_timeout (float, Default: 20.) - A float about the waiting time for processing bypass Cloudflare captcha

        1. We click the login button
        2. We follow on the TAG_NAME attribute named table for determine the captcha page is visible
            + If the captcha still visible during captcha timeout, we return Exception error
            + Else:
                - If the page is still in https://moodle.org/login, the login process will failed and return False
                - If the page redirects to https://moodle.org/, the login process will succeed and return True

        :rtype: bool
        """
        login_button = self.driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/section/div/div/div/div/form/div[4]/button')
        login_button.click()
        try:
            start = time.time()
            WebDriverWait(self.driver, captcha_timeout).until(EC.invisibility_of_element_located((By.TAG_NAME, 'table')))
            end  = time.time()
            print("Bypass captcha processing in {:.5f}s".format(end - start))
            
            if self.driver.current_url == URL.MAIN_URL:
                print("Login successful")
                return True
            else:
                print("Login failed")
                return False
        except TimeoutException:
            raise Exception(f"Timed out {captcha_timeout}s waiting for page to bypass captcha")

    def __del__(self):
        """Destructor quit the webdriver"""
        self.driver.close()
    
    def login_run(self, username: str, password: str, captcha_timeout: float = 20.) -> None:
        """Run the whole process for login
        
        :Args:
            - username (str, Default: "abcdef") - The username that we entered into form
            - password (str, Default: "123456") - The password that we entered into form
            - captcha_timeout (float, Default: 20.) - A float about the waiting time for processing bypass Cloudflare captcha
            - stay (bool, Default: False) - A boolean indicating whether we want to continue show the website

        1. Entered the username and password into form
        2. Login processing with captcha timeout using login_processing() function
        3. Config sleep to 1000 seconds if we want to show the website
        :rtype: None
        """
        self.driver.get(URL.LOGIN_URL)
        self.fill_login_form(username, password)
        response = self.login_processing(captcha_timeout)
        return response

    def stop(self):
        """Activate quit the webdriver"""
        self.driver.quit()


# driver = uc.Chrome(use_subprocess=True)
# login_ins = Login(driver)
# login_res = login_ins.login_run(username='abc', password='as')
# print(login_res)

# time.sleep(1000)