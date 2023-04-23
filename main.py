# from helper.utils import *
# from argparse import ArgumentParser

# # Run: python3 test_data_driven_input/main.py --id F1 --file excel/B_F1.xlsx --sheet 1

# parser = ArgumentParser()
# parser.add_argument('--id', metavar='path', type=str, required=True, help='ID of testsuite such as F1 or F2 or NF')
# parser.add_argument('--file', metavar='path', type=str, required=True, help='Input the file excel of data')
# parser.add_argument('--sheet', metavar='path', type=str, required=True, help='Sheet name of excel file')

# args = parser.parse_args()

# if args.id == 'F1':
#     @pytest.mark.parametrize(B_F1_title, load_excel(args.file,args.sheet))
#     def test_B_F1_general(_username, _password, _expect):    
#         username =  os.getenv('username') if _username == 'username' else _username
#         password = os.getenv('password') if _password == 'password' else _password
#         expect = bool(_expect)

#         assert login_func(username,password) == expect
# elif args.id == 'F2':
#     @pytest.mark.parametrize(B_F2_title, load_excel(args.file,args.sheet))
#     def test_B_F2_general(_current_password: str, _new_password: str, _new_password_again: str,
#                         _expect_res:bool,_expect_currentpwd_msg:str,_expect_newpwd_msg:str,_expect_newpwdagain_msg:str):
#         current_password: str = os.getenv('password') if _current_password == 'password' else _current_password
#         new_password: str = os.getenv('password') if _new_password == 'password' else _new_password
#         new_password_again: str = os.getenv('password') if _new_password_again == 'password' else _new_password_again

#         expect_res: bool = bool(_expect_res)
#         expect_currentpwd_msg: str = _expect_currentpwd_msg
#         expect_newpwd_msg: str = _expect_newpwd_msg
#         expect_newpwdagain_msg: str = _expect_newpwdagain_msg

#         changepwd_res: tuple[bool,tuple[str,str,str]] = changepass_func(current_password, new_password, new_password_again)
#         result, (currentpwd_msg, newpwd_msg, newpwdagain_msg) = changepwd_res

#         assert result == expect_res
#         assert currentpwd_msg == expect_currentpwd_msg
#         assert newpwd_msg == expect_newpwd_msg
#         assert newpwdagain_msg == expect_newpwdagain_msg

