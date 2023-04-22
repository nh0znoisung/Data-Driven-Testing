# Data Driven Testing method

## Authors 
**Quach Minh Tuan - Nguyen Phu Quy**

## Version
1.0.0

## Requirements
+ `Python` >= 3.10.9
+ `Pip` >= 23.0.1
+ Download `Chrome Webdriver` version >= 112.0.5615.49 at [Webdriver](https://chromedriver.storage.googleapis.com/index.html?path=112.0.5615.49/)

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

3. Create a **.env file** base on **.env.example** contains the password and username


## How to run
Open any CLIs
```sh
python main.py --feature <required testing feature> --io <required xlsx testcase file> --sheet <required sheetname> --skiprows <optional skiprows>
```
For example
```sh
python main.py --feature <required testing feature> --io <required xlsx testcase file> --sheet <required sheetname> --skiprows <optional skiprows>
```

if you use Mac and get the error like this "“chromedriver” cannot be opened because the developer cannot be verified."
xattr -d com.apple.quarantine <name-of-executable>