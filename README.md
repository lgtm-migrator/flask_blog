# Flask Blog

A blog implemented with flask framework

with 

* Flask 0.11
* SQLite3
* Jinja2
* BootStrap
* Markdown
* Python 3.5

# Install

recommend use virtualenv

YOU NEED BOWER TO INSTALL FRONTEND DEPENDENCE,you can google or baidu about it,usually you can use```npm i -g bower```to install it

```
pip install -r requirements.txt
bower install 
```

# Init DB

maybe you have to install sqlite3 first in your os, like ubuntu ```sudo apt install sqlite3```

```
sqlite3 fblog.db < db.sql
```

default user is ```admin``` , password also is ```admin```

# Start

```
python webapp.py
```