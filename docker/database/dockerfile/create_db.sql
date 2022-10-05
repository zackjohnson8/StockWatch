CREATE TABLE IF NOT EXISTS movers (
  change real NOT NULL,
  description varchar NOT NULL,
  direction varchar NOT NULL,
  last_val real NOT NULL,
  symbol varchar NOT NULL,
  totalVolume integer NOT NULL
);