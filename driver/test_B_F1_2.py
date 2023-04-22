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
        expect = False

        assert login_func(username,password) == expect

    def test_B_F1_2_003(self):
        username = 'testing1'
        password = os.getenv('password')
        expect = False

        assert login_func(username,password) == expect

    def test_B_F1_2_004(self):
        username = 'testing1'
        password = 'testing2*'
        expect = False

        assert login_func(username,password) == expect


