from helper.utils import *


@pytest.mark.parametrize(B_F1_title, load_excel("excel/B_F1.xlsx","2"))
def test_B_F1_general(_username, _password, _expect):    
    username =  os.getenv('username') if _username == 'username' else _username
    password = os.getenv('password') if _password == 'password' else _password
    expect = bool(_expect)

    assert login_func(username,password) == expect