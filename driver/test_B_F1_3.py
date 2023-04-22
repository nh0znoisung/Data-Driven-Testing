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


class Test_B_F1_3():
    def test_B_F1_3_001(self):
        username = 'abcde'
        password = '012345678910'
        expect = False

        assert login_func(username,password) == expect

    def test_B_F1_3_002(self):
        username = 'ab'
        password = '012345678910'
        expect = False

        assert login_func(username,password) == expect

    def test_B_F1_3_003(self):
        username = 'a'
        password = '012345678910'
        expect = False

        assert login_func(username,password) == expect

    def test_B_F1_3_004(self):
        username = 'abcde'
        password = '123456789'
        expect = False

        assert login_func(username,password) == expect

    def test_B_F1_3_005(self):
        username = 'abcde'
        password = '12345678'
        expect = False

        assert login_func(username,password) == expect
    

