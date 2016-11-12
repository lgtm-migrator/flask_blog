# Flask Blog

A blog implemented with flask framework

with 

* Flask 0.11
* SQLite3
* Jinja2
* BootStrap
* Markdown
* Python 3.5


## Quick Start 

If you have docker container, you can run following command line, to build image and run it

```
docker build -t fblog .
docker run -it --rm -p 5000:5000 --name fblog fblog
```

if you dont have docker, following suggestions will help you.

## Install

if you use physical machine to install, recommend use virtualenv

YOU NEED BOWER TO INSTALL FRONTEND DEPENDENCE,you can google or baidu about it,usually you can use```npm i -g bower```to install it, npm can be installed by package managers like ```apt```

Type following commands to install python dependency 

```
pip install -r requirements.txt
```

And frontend libs, like jquery and BootStrap

```
bower install 
```

## Init DB

maybe you have to install sqlite3 first in your os, like ```sudo apt install sqlite3```

then migrate the sql to db, do not modify the db file name, unless you known how to configure the webapp.py file

```
sqlite3 fblog.db < db.sql
```

default user is ```admin``` , password also is ```admin```

## Start

```
python webapp.py
```

## Other

Under MIT.

No more.

Suntao, 2016.