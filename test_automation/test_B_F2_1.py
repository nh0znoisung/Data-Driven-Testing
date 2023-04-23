import undetected_chromedriver as uc
from helper.utils import *

def changepass_func(current_password: str, new_password: str, new_password_again: str) -> tuple[bool,tuple[str,str,str]]: 
    changepassword_ins = ChangePassword(uc.Chrome(use_subprocess=True))
    changepwd_res = changepassword_ins.changepwd_run(current_password, new_password, new_password_again)
    changepassword_ins.stop()
    return changepwd_res

class Test_B_F2_1():
    def test_B_F2_1_001(self):
        current_password: str = os.getenv('password')
        new_password: str = 'testing2*'
        new_password_again: str = 'testing2*'

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

    def test_B_F2_1_002_1(self):
        """Test empty field in current password field"""
        current_password: str = ''
        new_password: str = 'temp'
        new_password_again: str = 'temp'

        expect_res: bool = False
        expect_currentpwd_msg: str = '- Required'
        expect_newpwd_msg: str = ''
        expect_newpwdagain_msg: str = ''

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_1_002_2(self):
        """Test empty field in new password field"""
        current_password: str = 'temp'
        new_password: str = ''
        new_password_again: str = 'temp'

        expect_res: bool = False
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = '- Required'
        expect_newpwdagain_msg: str = ''

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_1_002_3(self):
        """Test empty field in new password again field"""
        current_password: str = 'temp'
        new_password: str = 'temp'
        new_password_again: str = ''

        expect_res: bool = False
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = ''
        expect_newpwdagain_msg: str = '- Required'

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_1_003(self):
        """Test invalid login"""
        current_password: str = "testing2*"
        new_password: str = 'temp'
        new_password_again: str = 'temp'

        expect_res: bool = False
        expect_currentpwd_msg: str = 'Invalid login, please try again'
        expect_newpwd_msg: str = ''
        expect_newpwdagain_msg: str = ''

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_1_004(self):
        """Test password and password again do not match"""
        current_password: str = os.getenv('password')
        new_password: str = 'temp'
        new_password_again: str = 'temp1'

        expect_res: bool = False
        expect_currentpwd_msg: str = ''
        expect_newpwd_msg: str = 'These passwords do not match'
        expect_newpwdagain_msg: str = 'These passwords do not match'

        changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
        result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

        assert result == expect_res
        assert currentpwd_msg == expect_currentpwd_msg
        assert newpwd_msg == expect_newpwd_msg
        assert newpwdagain_msg == expect_newpwdagain_msg

    def test_B_F2_1_005(self):
        current_password: str = os.getenv('password')
        new_password: str = 'test2*'
        new_password_again: str = 'test2*'

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

    def test_B_F2_1_006(self):
        current_password: str = os.getenv('password')
        new_password: str = 'testing2'
        new_password_again: str = 'testing2' #os.getenv('newpassword')

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