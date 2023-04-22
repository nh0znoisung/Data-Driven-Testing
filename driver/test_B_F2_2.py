import undetected_chromedriver as uc
import sys
import os
sys.path.append(os.path.abspath('../helper'))
from helper.ChangePassword import ChangePassword
from helper.exceptions import *
from dotenv import load_dotenv
load_dotenv()

# def login_func(username: str, password: str) -> bool: 
#     login_ins = Login(uc.Chrome(use_subprocess=True))
#     login_res = login_ins.login_run(username=username, password=password)
#     return login_res

class Test_B_F2_2():
    def test_B_F2_2_001(self):
        changepwd_ins = ChangePassword(uc.Chrome(use_subprocess=True))
        newpass = 'hello' #os.getenv('newpassword')
        changepwd_res = changepwd_ins.changepwd_run(newpass)

        assert changepwd_res == False
