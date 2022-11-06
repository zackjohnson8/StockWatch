CREATE TABLE IF NOT EXISTS movers (
  id serial primary key,
  change real not null,
  description varchar not null,
  direction varchar not null,
  last_val real not null,
  symbol varchar not null ,
  totalVolume integer not null
);

CREATE TABLE IF NOT EXISTS accounts (
  id serial primary key,
  username text unique not null,
  password text not null
);

CREATE TABLE IF NOT EXISTS posts (
  id serial primary key,
  author_id integer not null,
  created timestamp not null default now(),
  title text not null,
  body text not null,
  foreign key (author_id) references accounts (id)
);