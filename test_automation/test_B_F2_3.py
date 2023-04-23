import undetected_chromedriver as uc
from helper.utils import *

def changepass_func(current_password: str, new_password: str, new_password_again: str) -> tuple[bool,tuple[str,str,str]]: 
    changepassword_ins = ChangePassword(uc.Chrome(use_subprocess=True))
    changepwd_res = changepassword_ins.changepwd_run(current_password, new_password, new_password_again)
    changepassword_ins.stop()
    return changepwd_res

class Test_B_F2_3():
    def test_B_F2_3_001(self):
        current_password: str = os.getenv('password')
        new_password: str = '1234567***-#'
        new_password_again: str = '1234567***-#'

        expect_res: bool = True
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = ''
        expect_newpwdagain_msg: str = ''

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_3_002(self):
        current_password: str = os.getenv('password')
        new_password: str = '1234567891**'
        new_password_again: str = '1234567891**'

        expect_res: bool = True
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = ''
        expect_newpwdagain_msg: str = ''

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_3_003(self):
        current_password: str = os.getenv('password')
        new_password: str = '12345678910*'
        new_password_again: str = '12345678910*'

        expect_res: bool = True
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = ''
        expect_newpwdagain_msg: str = ''

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_3_004(self):
        current_password: str = os.getenv('password')
        new_password: str = '123456789101'
        new_password_again: str = '123456789101'

        expect_res: bool = False
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = 'The password must have at least 1 special character(s) such as as *, -, or #.'
        expect_newpwdagain_msg: str = 'The password must have at least 1 special character(s) such as as *, -, or #.'

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_3_005(self):
        current_password: str = os.getenv('password')
        new_password: str = '1234*****'
        new_password_again: str = '1234*****'

        expect_res: bool = True
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = ''
        expect_newpwdagain_msg: str = ''

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_3_006(self):
        current_password: str = os.getenv('password')
        new_password: str = '123*****'
        new_password_again: str = '123*****'

        expect_res: bool = True
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = ''
        expect_newpwdagain_msg: str = ''

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_3_007(self):
        current_password: str = os.getenv('password')
        new_password: str = '12#####'
        new_password_again: str = '12#####'

        expect_res: bool = False
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = 'Passwords must be at least 8 characters long.'
        expect_newpwdagain_msg: str = 'Passwords must be at least 8 characters long.'

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg