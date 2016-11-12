drop table if exists blog;
drop table if exists user;
create table blog (
  id integer primary key autoincrement,
  title text not null,
  content text,
  userid integer,
  createdate text
);

create table user (
  id integer primary key autoincrement,
  username text not null,
  password text not null,
  createdate text
);

insert into user values(null,'admin','admin',date('now'));

