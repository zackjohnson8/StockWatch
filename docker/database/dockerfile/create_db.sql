CREATE TABLE IF NOT EXISTS mover (
  change double precision NOT NULL,
  description character NOT NULL,
  direction character NOT NULL,
  last_val real NOT NULL,
  symbol character NOT NULL,
  totalVolume integer NOT NULL
);