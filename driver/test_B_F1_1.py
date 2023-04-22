import undetected_chromedriver as uc
import sys
import os
sys.path.append(os.path.abspath('../helper'))
from helper.Login import Login
from dotenv import load_dotenv
load_dotenv()


def login_func(username: str, password: str) -> bool: 
    login_ins = Login(uc.Chrome(use_subprocess=True))
    login_res = login_ins.login_run(username=username, password=password)
    return login_res


class Test_B_F1_2():
    def test_B_F1_2_001(self):
        username = os.getenv('username')
        password = os.getenv('password')
        expect = True

        assert login_func(username,password) == expect

    def test_B_F1_2_002(self):
        username = os.getenv('username')
        password = 'testing2*'
        assert login_func(username,password) == False

        username = os.getenv('username')
        password = os.getenv('password')
        assert login_func(username,password) == True




