# Data Driven Testing method

## Authors 
**Quach Minh Tuan - Nguyen Phu Quy**

## Version
1.0.0

## Requirements
+ `Python` >= 3.10.9
+ `Pip` >= 23.0.1
+ Create an account at https://moodle.org/demo. Make sure the password is different from **`testing2*`** and **`password`**, the username must be different from **`username`**

## Installation
1. Clone our source code
```sh
$ git clone https://github.com/nh0znoisung/Data-Driven-Testing
$ cd Data-Driven-Testing
```

2. Install Dependencies
```sh
$ pip install -r requirements.txt
```

3. Create a **.env file** base on the content of **.env.example** contains the password and username
```text
username=abcde
password=1234567
```

## Structure
The main code structure is organized as
```text
| helper
| test_automation
    | test_***
| test_data_driven
    | test ***
| excel

```
The code is used `pytest` lib for testing the program, how many failed and passed testcases when we use `selenium`. The test is trigger when we call `pytest <location of testcases>`. The `helper` dir contains the supporting functions and 2 main processes such as `ChangePassword` and `Login` . The `test_automation` dir contains all testcases with `test_*.py` while `test_data_driven` contains the same testcases and structure as `test_automation` but using loading the data from `excel` folder.

## How to run
Open any CLIs
```sh
pytest test_automation/test_B_F1_1.py
```

<!-- if you use Mac and get the error like this "“chromedriver” cannot be opened because the developer cannot be verified."
xattr -d com.apple.quarantine <name-of-executable> -->
