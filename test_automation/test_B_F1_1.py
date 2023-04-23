import undetected_chromedriver as uc
from helper.utils import *


def login_func(username: str, password: str) -> bool: 
    login_ins = Login(uc.Chrome(use_subprocess=True))
    login_res = login_ins.login_run(username=username, password=password)
    login_ins.stop()
    return login_res


class Test_B_F1_1():
    def test_B_F1_1_001(self):
        username = os.getenv('username')
        password = os.getenv('password')
        expect = True

        assert login_func(username,password) == expect

    def test_B_F1_1_002(self):
        username = os.getenv('username')
        password = 'testing2*'
        assert login_func(username,password) == False

        username = os.getenv('username')
        password = os.getenv('password')
        assert login_func(username,password) == True




