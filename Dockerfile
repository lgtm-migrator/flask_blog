FROM python:3.5-onbuild

RUN apt-get update
RUN apt-get install -y npm sqlite3 nodejs-legacy
RUN npm i -g bower 
RUN bower install --allow-root
RUN sqlite3 fblog.db < db.sql

CMD [ "python", "./webapp.py" ]