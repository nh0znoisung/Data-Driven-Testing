from helper.utils import *


@pytest.mark.parametrize(B_F2_title, load_excel("excel/B_F2.xlsx","3"))
def test_B_F2_general(_current_password: str, _new_password: str, _new_password_again: str,
                     _expect_res:bool,_expect_currentpwd_msg:str,_expect_newpwd_msg:str,_expect_newpwdagain_msg:str):
    current_password: str = os.getenv('password') if _current_password == 'password' else _current_password
    new_password: str = os.getenv('password') if _new_password == 'password' else _new_password
    new_password_again: str = os.getenv('password') if _new_password_again == 'password' else _new_password_again

    expect_res: bool = bool(_expect_res)
    expect_currentpwd_msg: str = _expect_currentpwd_msg
    expect_newpwd_msg: str = _expect_newpwd_msg
    expect_newpwdagain_msg: str = _expect_newpwdagain_msg

    changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
    result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

    assert result == expect_res
    assert currentpwd_msg == expect_currentpwd_msg
    assert newpwd_msg == expect_newpwd_msg
    assert newpwdagain_msg == expect_newpwdagain_msg