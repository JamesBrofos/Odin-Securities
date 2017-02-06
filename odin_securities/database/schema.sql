-- The "symbols" table stores information about individual companies usch as
-- their ticker, their sector, and the company's official business name. We also
-- store information about when the company was added to the database and when
-- it was that information about the company was last updated.
CREATE TABLE IF NOT EXISTS symbols (
       id SERIAL PRIMARY KEY,
       symbol varchar(15) NOT NULL UNIQUE
);
CREATE INDEX IF NOT EXISTS symbol_index ON symbols (symbol);

-- Odin may derive securities data from many sources. As such, the "vendors"
-- table is responsible for representing the various data sources that could be
-- employed.
CREATE TABLE IF NOT EXISTS vendors (
       id SERIAL PRIMARY KEY,
       vendor varchar(100) UNIQUE NOT NULL
);
CREATE INDEX IF NOT EXISTS vendor_index ON vendors (vendor);

-- We keep track fo which vendors are responsible for serving particular
-- symbols.
CREATE TABLE IF NOT EXISTS symbol_vendor (
       id SERIAL PRIMARY KEY,
       symbol_id int REFERENCES symbols (id),
       vendor_id int REFERENCES vendors (id),
       updated timestamp NOT NULL,
       UNIQUE (symbol_id, vendor_id)
);

-- The "prices" table is where the day-by-day price of the equities is stored.
-- In addition to storing the OHLCV raw data, the divident and stock split
-- adjusted prices and volumes are also stored.
CREATE TABLE IF NOT EXISTS prices (
       id SERIAL PRIMARY KEY,
       symbol_id int REFERENCES symbols (id),
       vendor_id int REFERENCES vendors (id),
       datetime timestamp NOT NULL,
       price_open float NOT NULL,
       price_high float NOT NULL,
       price_low float NOT NULL,
       price_close float NOT NULL,
       volume bigint NOT NULL,
       adj_price_open float NOT NULL,
       adj_price_high float NOT NULL,
       adj_price_low float NOT NULL,
       adj_price_close float NOT NULL,
       adj_volume bigint NOT NULL,
       UNIQUE (symbol_id, vendor_id, datetime)
);
CREATE INDEX IF NOT EXISTS price_datetime_index ON prices (datetime);
CREATE INDEX IF NOT EXISTS price_datetime_vendor_symbol_index ON prices (
       datetime, vendor_id, symbol_id
);

-- The "funds" table stores funds and can be leveraged to identify which
-- portfolios are associated with a given fund.
CREATE TABLE IF NOT EXISTS funds (
       id SERIAL PRIMARY KEY,
       fund varchar(100) UNIQUE NOT NULL,
       entry_date timestamp NOT NULL,
       rebalance_period varchar(20),
       manage_period varchar(20)
);
CREATE INDEX IF NOT EXISTS fund_index ON funds (fund);

-- The "portfolios" table stores portfolio identifiers that can be used to query
-- filled positions from the database.
CREATE TABLE IF NOT EXISTS portfolios (
       id SERIAL PRIMARY KEY,
       portfolio varchar(100) UNIQUE NOT NULL,
       fund_id int REFERENCES funds (id),
       maximum_capacity int NOT NULL,
       capital float NOT NULL,
       updated timestamp NOT NULL
);
CREATE INDEX IF NOT EXISTS portfolio_index on portfolios (portfolio);

-- The "positions" table stores filled positions associated with individual
-- portfolios.
CREATE TABLE IF NOT EXISTS positions (
       id SERIAL PRIMARY KEY,
       symbol_id int REFERENCES symbols (id),
       portfolio_id int REFERENCES portfolios (id),
       direction varchar(10) NOT NULL,
       trade_type varchar(10) NOT NULL,
       date_entered timestamp NOT NULL,
       avg_price float NOT NULL,
       buys int NOT NULL,
       sells int NOT NULL,
       avg_buys_price float NOT NULL,
       avg_sells_price float NOT NULL,
       tot_buys_price float NOT NULL,
       tot_sells_price float NOT NULL,
       tot_commission float NOT NULL,
       UNIQUE (portfolio_id, symbol_id)
);

-- For compliance purposes, create a table to store closed positions. These can
-- be reviewed at a later date if required.
CREATE TABLE IF NOT EXISTS closed_positions (
       LIKE positions EXCLUDING CONSTRAINTS
);

-- The "actions" table stores information regarding corporate actions that may
-- affect the stock price. In particular, information about dividends and stock
-- splits are stored, along with the corresponding date of the action.
CREATE TABLE IF NOT EXISTS actions (
       id SERIAL PRIMARY KEY,
       symbol_id int REFERENCES symbols (id),
       vendor_id int REFERENCES vendors (id),
       datetime timestamp NOT NULL,
       split_ratio float NOT NULL,
       dividend float NOT NULL,
       UNIQUE (symbol_id, vendor_id, datetime)
);
CREATE INDEX IF NOT EXISTS action_datetime_index ON actions (datetime);
CREATE INDEX IF NOT EXISTS action_datetime_vendor_symbol_index ON actions (
       datetime, vendor_id, symbol_id
);
