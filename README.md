# Github Trends

the script finds all the repositories created in the last week,
selects 20 with the largest number of stars,
and for each counts the number of open issues. And displays them
in the terminal along with the links.

# Example run

Open the terminal, go to the directory where the file is located and
run "python github_trending.py", if python 3 as not default try
"python3 github_trending.py"

```bash
$ python github_trending.py
Stars: 2526
Open issues: 6
Repo url: https://github.com/luanfujun/deep-painterly-harmonization
Stars: 678
Open issues: 6
Repo url: https://github.com/hannob/snallygaster
Stars: 647
Open issues: 1
Repo url: https://github.com/itchyny/bed

. . .

```

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there
is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
